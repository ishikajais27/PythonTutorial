lst = list(map(int, input("Enter list elements: ").split()))

n = len(lst)
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Ascending order:", lst)

desc = []
for i in range(n - 1, -1, -1):
    desc.append(lst[i])

print("Descending order:", desc)
