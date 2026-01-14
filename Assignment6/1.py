

filename = input("Enter file name: ")

with open(filename, "w") as file:
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    file.write("Name: " + name + "\n")
    file.write("Roll No: " + roll + "\n")
    file.write("Marks: " + marks + "\n")

print("Student details written to file successfully.")
