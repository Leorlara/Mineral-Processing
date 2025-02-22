import csv

def read_10th_column(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 10:  
                    print(row[9])  
                else:
                    print("Row does not have 10 columns")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
Reference_mass = input("Enter the average (g): ")
file_path = input("enter the file path")  # input file path
read_10th_column(file_path)