lst = list(map(int, input("Enter list elements: ").split()))

mx = lst[0]
mn = lst[0]

for i in lst:
    if i > mx:
        mx = i
    if i < mn:
        mn = i

print("Maximum element:", mx)
print("Minimum element:", mn)
