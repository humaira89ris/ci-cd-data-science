import pandas as pd

df = pd.read_csv("data/dataset.csv")
print("✅ Dataset Loaded Successfully!\n")
print(df.head())
print("\n📊 Class Distribution:")
print(df['target'].value_counts())
