def stats(lst):
    return sum(lst), sum(lst) / len(lst), max(lst), min(lst)

nums = list(map(int, input().split()))
print(stats(nums))
