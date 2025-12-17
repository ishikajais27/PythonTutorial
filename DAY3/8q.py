lst = list(map(int, input("Enter list elements: ").split()))
n = int(input("Enter rotation value: "))
left_rotate = lst[n:] + lst[:n]
right_rotate = lst[-n:] + lst[:-n]
print("Left rotated list:", left_rotate)
print("Right rotated list:", right_rotate)
