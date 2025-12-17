lst = list(map(int, input("Enter list elements: ").split()))
n = int(input("Enter rotation value: "))

left_rotate = []
for i in range(n, len(lst)):
    left_rotate += [lst[i]]
for i in range(n):
    left_rotate += [lst[i]]

right_rotate = []
for i in range(len(lst) - n, len(lst)):
    right_rotate += [lst[i]]
for i in range(len(lst) - n):
    right_rotate += [lst[i]]

print("Left rotated list:", left_rotate)
print("Right rotated list:", right_rotate)
