import pandas as pd

file = input("Enter CSV file name (with extension): ")
df = pd.read_csv(file)
corr = df.corr(numeric_only=True)
print("Correlation Matrix:")
print(corr)
