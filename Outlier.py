import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def process_and_plot_outliers(file_path):
    # 1. Load the data
    # Ensure 'openpyxl' is installed if loading .xlsx (pip install openpyxl)
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    # 2. Prepare Columns (Adjust names if they differ in your file)
    x_col = 'GPI'
    y_col = 'Mill specific energy (kWh/t)'

    # Convert to numeric and drop rows with missing values in these columns
    df[x_col] = pd.to_numeric(df[x_col], errors='coerce')
    df[y_col] = pd.to_numeric(df[y_col], errors='coerce')
    data = df.dropna(subset=[x_col, y_col]).copy()

    x = data[x_col].values
    y = data[y_col].values

    # 3. Fit Linear Model to calculate residuals
    # This is the 'fitting' step to see how far points are from the trend
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    predicted = slope * x + intercept
    residuals = y - predicted

    # 4. Systematic Outlier Removal (IQR Method on Residuals)
    # This matches the logic from your provided snippet
    q1 = np.percentile(residuals, 25)
    q3 = np.percentile(residuals, 75)
    iqr = q3 - q1
    factor = 1.5  # Standard IQR factor; increase to 3.0 for 'extreme' only
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr

    # Identify which rows are outliers
    is_outlier = (residuals < lower_bound) | (residuals > upper_bound)
    
    clean_data = data[~is_outlier]
    outliers = data[is_outlier]

    # 5. Plotting (This will show up in VS Code)
    plt.figure(figsize=(10, 6))
    
    # Plot the good points
    plt.scatter(clean_data[x_col], clean_data[y_col], color='blue', alpha=0.6, label='Normal Data')
    
    # Plot the removed points in red
    plt.scatter(outliers[x_col], outliers[y_col], color='red', marker='x', s=80, label='Outliers Removed')
    
    # Plot the trend line
    plt.plot(x, predicted, color='black', linestyle='--', alpha=0.5, label='Trend Line')

    plt.title(f'Systematic Outlier Removal (Factor: {factor})')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Final command to render the graph in VS Code
    plt.show()

    # Save the cleaned result
    clean_data.to_csv("Cleaned_Database.csv", index=False)
    print(f"Done! Removed {len(outliers)} outliers.")

# Run the function
# Make sure the file name matches exactly what is in your folder
process_and_plot_outliers('Revised database - Model - Revised.xlsx - Original.csv')