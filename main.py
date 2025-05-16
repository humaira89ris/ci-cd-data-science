import pandas as pd

# Load the original dataset
df = pd.read_csv("data/dataset.csv")
print("📥 Original Data Loaded")
print(df.head())

# Step 1: Remove duplicates
df_clean = df.drop_duplicates()
print("✅ Duplicate rows removed")

# Step 2: Save the cleaned dataset
df_clean.to_csv("data/processed_dataset.csv", index=False)
print("📁 Processed dataset saved as data/processed_dataset.csv")
