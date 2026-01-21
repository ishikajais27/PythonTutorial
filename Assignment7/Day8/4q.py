import pandas as pd

file = input("Enter CSV file name (with extension): ")
df = pd.read_csv(file)
filtered = df[df["marks"] > 60]
print("Students with marks greater than 60:")
print(filtered)
