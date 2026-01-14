fname = input("Enter file name: ")

f = open(fname, "r")
text = f.read()
f.close()

lines = text.splitlines()
words = text.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))
