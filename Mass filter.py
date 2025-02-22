import csv

def read_last_column(file_path):
    try:
        file_path = file_path.strip('"')  # Remove quotes from file path (a qol improvement when you use the copy as a path on windows)
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=';')  # Use semicolon as delimiter
            for row in reader:
                if row:  # Ensure row is not empty
                    print(row[-1])  # Print the last column
                else:
                    print("Empty row encountered")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
Reference_mass = input("Enter the average (g): ")
file_path = input("enter the file path")  # input file path
read_last_column(file_path)