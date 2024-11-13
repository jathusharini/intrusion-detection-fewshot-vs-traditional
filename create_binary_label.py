import pandas as pd

# Load the Excel dataset
file_path = 'CIC-IDS-2017_Subset.xlsx'
df = pd.read_excel(file_path)

# Remove any extra spaces from column names
df.columns = df.columns.str.strip()

# Rename the "Label" column to "Attack Type" if it exists
if 'Label' in df.columns:
    df.rename(columns={'Label': 'Attack Type'}, inplace=True)
    print("Renamed 'Label' column to 'Attack Type'.")
else:
    raise KeyError("The dataset does not contain a 'Label' column.")

# Create a new "Label" column with binary classification: 0 for BENIGN, 1 for attacks
df['Label'] = df['Attack Type'].apply(lambda x: 0 if x.strip().upper() == 'BENIGN' else 1)

# Save changes back to the same Excel file
df.to_excel(file_path, index=False)
print(f"Modifications saved directly to '{file_path}'.")

# Create new CSV
df.to_csv("Modified_dataset.csv", index=False)
print("Modifications saved to 'Modified_dataset.csv'.")




