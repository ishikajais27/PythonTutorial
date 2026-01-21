import pandas as pd

file = input("Enter CSV file name (with extension): ")
df = pd.read_csv(file)
df.fillna(df.mean(numeric_only=True), inplace=True)
print("Data after replacing missing values with mean:")
print(df)
