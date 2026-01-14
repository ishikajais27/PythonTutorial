import csv

f = open(input(), "w", newline="")
w = csv.writer(f)
n = int(input())
for i in range(n):
    w.writerow(input().split())
f.close()
