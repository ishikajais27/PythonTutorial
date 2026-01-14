s = input("Enter a string: ")
v = c = d = sp = 0
for ch in s:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    else:
        sp += 1
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special characters:", sp)
