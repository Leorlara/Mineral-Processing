import os
import pandas as pd

# ====== EDIT THESE PATHS ======
excel_path = r"C:\Users\leorl\Downloads\Sample_List_Template_Rev_0.xlsx"
folder_path = r"C:\Users\leorl\Downloads\RAW DATA - Copy\RAW DATA - Copy - Copy"
# ===============================

# --- Read Excel (Column A, starting at row 2) ---
df = pd.read_excel(excel_path)

# Get values from column A starting at A2
sample_list = df.iloc[0:, 0].dropna().astype(str).tolist()

# Clean sample names (remove spaces)
sample_list = [s.strip() for s in sample_list]

# --- Read Folder Files ---
files = os.listdir(folder_path)

# Remove file extensions
file_names = [os.path.splitext(f)[0] for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Clean file names
file_names = [f.strip() for f in file_names]

# --- Compare ---
samples_set = set(sample_list)
files_set = set(file_names)

missing_files = samples_set - files_set
extra_files = files_set - samples_set
matches = samples_set & files_set

# --- Results ---
print("\n MATCHING FILES:")
for m in sorted(matches):
    print(m)

print("\n SAMPLES WITH NO FILE:")
for m in sorted(missing_files):
    print(m)

print("\n⚠ FILES NOT IN SAMPLE LIST:")
for e in sorted(extra_files):
    print(e)

print("\nDone.")