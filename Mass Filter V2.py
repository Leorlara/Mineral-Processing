import csv
import os

def sanitize_path(path): #fuction that removes quotes and normalizes the path
    return os.path.normpath(path.strip().strip('"'))  # Remove quotes and normalize path when you copy from file exploer it will come with quotes

def filter_csv_files_in_folder(folder_path, output_folder, reference_masses): # fuction that performes the filtering 
    try:
        folder_path = sanitize_path(folder_path)
        output_folder = sanitize_path(output_folder)
        
        print(f"Processing files in folder: {folder_path}")
        print(f"Saving filtered files to: {output_folder}")
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)  # Create output folder if it doesn't exist (in case of typo)
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if not os.path.isfile(file_path):  # Skip directories
                continue
            
            print(f"Processing file: {file_name}")
            
            if file_name not in reference_masses: # here just in case a reference mass was not provided
                print(f"Skipping {file_name}: No reference mass provided.")
                continue
            
            reference_mass = reference_masses[file_name] # Filter range (change it you want to use a different range)
            lower_bound = reference_mass * 0.7  # -30%
            upper_bound = reference_mass * 1.3  # +30%
            filtered_rows = []
            
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=';')  # Use semicolon as delimiter (chnage if a different one is been used)
                header = next(reader, None)  # Read the header if present
                
                if header:
                    filtered_rows.append(header)
                
                for row in reader:
                    if len(row) >= 10:  # Ensure the row has at least 10 columns
                        try:
                            value = float(row[9].replace(',', '.'))  # Convert 10th column to float, handling comma decimal separator (added for files that use , as decimal separator)
                            if lower_bound <= value <= upper_bound:
                                filtered_rows.append(row)
                        except ValueError:
                            print(f"Skipping row with invalid numeric value in 10th column: {row}")
                    else:
                        print("Skipping row with insufficient columns")
            
            output_file_path = os.path.join(output_folder, file_name)  # Keep the original file name (essential for the files to be processed correctly)
            
            with open(output_file_path, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(filtered_rows)
            
            print(f"Filtered CSV saved as: {output_file_path}") # if everything goes well, you will see each print for each file
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = input("Enter the folder path containing files: ") #Copy path from your file explorer
output_folder = input("Enter the output folder path: ") # Copy the path from your file explorer
folder_path = sanitize_path(folder_path)
output_folder = sanitize_path(output_folder)

reference_masses = {}

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
if not files:
    print("No files found in the specified folder.")
else:
    for file_name in files:
        reference_mass = float(input(f"Enter the reference mass for {file_name}: ").replace(',', '.'))
        reference_masses[file_name] = reference_mass
    
    filter_csv_files_in_folder(folder_path, output_folder, reference_masses)