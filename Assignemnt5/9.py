f = open(input(), "r")
data = f.read().split()
f.close()

d = {}
for i in data:
    d[i] = d.get(i, 0) + 1

f = open(input(), "w")
for k, v in d.items():
    f.write(k + " " + str(v) + "\n")
f.close()
