fname = input("Enter file name: ")

f = open(fname, "r")
lines = f.readlines()
f.close()

f = open(fname, "w")
for line in lines:
    if line.strip():
        f.write(line)
f.close()

print("Blank lines removed")
