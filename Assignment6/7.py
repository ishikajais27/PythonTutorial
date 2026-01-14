# Q7: Search word and show line numbers

filename = input("Enter file name: ")
search_word = input("Enter word to search: ")

with open(filename, "r") as file:
    line_no = 1
    found = False
    for line in file:
        if search_word in line:
            print("Word found at line:", line_no)
            found = True
        line_no += 1

if not found:
    print("Word not found.")
