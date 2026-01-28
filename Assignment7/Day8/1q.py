import pandas as pd

file = input("Enter CSV file name (with extension): ")
df = pd.read_csv(file)
print("CSV Data:")
print(df)
