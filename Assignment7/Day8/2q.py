import pandas as pd

file = input()
df = pd.read_csv(file)
print(df.head())
print(df.tail())
print(df.describe())
