import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def remove_fit_outliers(file_path, output_path):
    try:
        # 1. Load the private Excel file
        # Required: pip install pandas openpyxl scipy matplotlib
        df = pd.read_excel(file_path)
        
        # Clean column names (removes hidden spaces)
        df.columns = df.columns.str.strip()

        # 2. Define our variables (Update these strings if your column names differ)
        x_col = 'GPI'
        y_col = 'Mill specific energy (kWh/t)'

        if x_col not in df.columns or y_col not in df.columns:
            print(f"Error: Could not find columns '{x_col}' or '{y_col}'")
            print(f"Available columns: {df.columns.tolist()}")
            return

        # Remove rows with NaN in these specific columns so the math doesn't break
        df_temp = df.dropna(subset=[x_col, y_col]).copy()

        # 3. Calculate the Linear Fit and Residuals
        slope, intercept, r_value, p_value, std_err = stats.linregress(df_temp[x_col], df_temp[y_col])
        
        # Predicted Y values based on the fit
        df_temp['Expected_Y'] = intercept + slope * df_temp[x_col]
        
        # Calculate the distance (Residual) from the line
        df_temp['Residual'] = df_temp[y_col] - df_temp['Expected_Y']

        # 4. Filter by Z-Score of the Residuals
        # We remove points that are more than 2 Standard Deviations away from the line
        z_scores = np.abs(stats.zscore(df_temp['Residual']))
        df_clean = df_temp[z_scores < 2].copy()

        print(f"Original rows: {len(df)}")
        print(f"Rows after removing fit outliers: {len(df_clean)}")

        # 5. Save the new file
        df_clean.drop(columns=['Expected_Y', 'Residual'], inplace=True)
        df_clean.to_excel(output_path, index=False)
        print(f"--- SUCCESS: Cleaned file saved to {output_path} ---")

        # 6. Visualize the removal
        plt.figure(figsize=(10, 6))
        plt.scatter(df_temp[x_col], df_temp[y_col], color='red', label='Outliers', alpha=0.5)
        plt.scatter(df_clean[x_col], df_clean[y_col], color='blue', label='Kept Data')
        plt.plot(df_temp[x_col], df_temp['Expected_Y'], color='black', label='Trend Line')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Outlier Removal: {x_col} vs {y_col}")
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# --- SET YOUR PATHS HERE ---

# Path to your private data (outside GitHub)
input_file = r"C:\Users\leorl\Downloads\Database code\Revised database - Model - Revised.xlsx"

# Path where the new "Cleaned" file will be created
output_file = r"C:\Users\leorl\Downloads\Database code\Cleaned_Mineral_Data.xlsx"

if __name__ == "__main__":
    remove_fit_outliers(input_file, output_file)