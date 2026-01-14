import string

f = open(input(), "r")
data = f.read()
f.close()
for i in string.punctuation:
    data = data.replace(i, "")
print(data)
