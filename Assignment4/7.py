from functools import reduce

nums = list(map(int, input().split()))
product = reduce(lambda x, y: x * y, nums)
print(product)
