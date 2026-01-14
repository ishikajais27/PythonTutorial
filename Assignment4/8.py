def greet(name, msg="Hello"):
    return msg + " " + name

name = input()
msg = input()
print(greet(name, msg=msg))
