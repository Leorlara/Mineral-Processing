import os

folder_path = r"C:\Users\leorl\Downloads\RAW DATA - Copy\RAW DATA - Copy - Copy"


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Skip if no file
    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)
        
        # Avoids if already ends with _M
        if not name.endswith("_M"):
            new_name = name + "_M" + ext
            new_file_path = os.path.join(folder_path, new_name)
            
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} → {new_name}")