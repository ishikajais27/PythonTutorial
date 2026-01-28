import pandas as pd

file = input("Enter CSV file name (with extension): ")
df = pd.read_csv(file)
print("First 5 rows:")
print(df.head())
print("Last 5 rows:")
print(df.tail())
print("Statistical Summary:")
print(df.describe())
