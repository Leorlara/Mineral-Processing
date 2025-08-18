import csv
import os

def read_last_column(file_path):
    try:
        file_path = file_path.strip('"')  # Remove quotes from copied file paths
        filtered_rows = []
        
        # Below is the range of the filter, if another value different from 30% is used, change it bwelow
        lower_bound = Reference_mass * 0.7  # -30%
        upper_bound = Reference_mass * 1.3  # +30%
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=';')  # # Use semicolon as delimiter (since it's a csv file, if another version is been used, change it here
            header = next(reader, None)  # Read the header if present
            
            if header:
                filtered_rows.append(header)
            
            for row in reader:
                if len(row) >= 10:  # Ensure the row has at least 10 columns
                    try:
                        value = float(row[9])  # Convert 10th column to float
                        if lower_bound <= value <= upper_bound:
                            filtered_rows.append(row)
                    except ValueError:
                        print(f"Skipping row with invalid numeric value in 10th column: {row}")
                else:
                    print("Skipping row with insufficient columns")
        
        output_file_name = os.path.basename(file_path).replace(".csv", "_filtered.csv")
        output_file_path = os.path.join(output_folder, output_file_name)
        
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(filtered_rows)
        
        print(f"Filtered CSV saved as: {output_file_path}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
Reference_mass = input("Enter the average (g): ")
file_path = input("enter the file path: ")  # input file path
output_folder = input("Enter the output folder path: ")
read_last_column(file_path, output_folder, Reference_mass)