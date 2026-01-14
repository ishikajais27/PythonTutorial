# Q2: Search word in file and display line numbers

filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, "r") as file:
    lines = file.readlines()

found = False
for i in range(len(lines)):
    if word in lines[i]:
        print("Word found at line number:", i + 1)
        found = True

if not found:
    print("Word not found in file.")
