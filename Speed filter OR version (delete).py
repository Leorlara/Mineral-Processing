import csv
import os

def sanitize_path(path):
    return os.path.normpath(path.strip().strip('"'))

def filter_csv_files_on_columns_8_and_9(folder_path, output_folder):
    try:
        folder_path = sanitize_path(folder_path)
        output_folder = sanitize_path(output_folder)
        
        print(f"Processing files in folder: {folder_path}")
        print(f"Saving filtered files to: {output_folder}")
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        summary_data = []
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if not os.path.isfile(file_path):
                continue
            
            filtered_rows = []
            total_rows = 0
            removed_rows = 0
            
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                header = next(reader, None)
                
                if header:
                    filtered_rows.append(header)
                
                for row in reader:
                    total_rows += 1
                    if len(row) >= 9:
                        try:
                            value8 = float(row[7].replace(',', '.'))
                            value9 = float(row[8].replace(',', '.'))
                            
                            if value8 > 82 or value9 > 82:
                                removed_rows += 1
                                continue
                            
                            filtered_rows.append(row)
                        except ValueError:
                            print(f"Skipping row with invalid numeric values in columns 8 or 9: {row}")
                            removed_rows += 1
                    else:
                        print("Skipping row with insufficient columns")
                        removed_rows += 1
            
            percentage_removed = (removed_rows / total_rows * 100) if total_rows else 0
            
            if percentage_removed <= 50:
                output_file_path = os.path.join(output_folder, file_name)
                with open(output_file_path, mode='w', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerows(filtered_rows)
                print(f"Filtered CSV saved as: {output_file_path}")
            else:
                print(f"Skipping output for {file_name}: {percentage_removed:.2f}% rows removed exceeds 25% threshold")
            
            summary_data.append([
                file_name, 
                total_rows, 
                removed_rows, 
                f"{percentage_removed:.2f}%", 
                "Saved" if percentage_removed <= 25 else "Deleted"
            ])
        
        # Write summary file
        summary_file_path = os.path.join(output_folder, "summary.csv")
        with open(summary_file_path, mode='w', newline='') as summary_file:
            writer = csv.writer(summary_file, delimiter=';')
            writer.writerow(["File Name", "Total Rows", "Removed Rows", "Percentage Removed", "Status"])
            writer.writerows(summary_data)
        
        print(f"Summary file saved as: {summary_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = input("Enter the folder path containing files: ")
output_folder = input("Enter the output folder path: ")

filter_csv_files_on_columns_8_and_9(folder_path, output_folder)
