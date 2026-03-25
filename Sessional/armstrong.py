
def is_armstrong(num):
    order = len(str(num))  
    sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    return num == sum



start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)