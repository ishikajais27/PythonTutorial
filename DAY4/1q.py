n = int(input("Enter number of students: "))
students = {}
for _ in range(n):
    name = input("Enter student name: ")
    roll = input("Enter student roll number: ")
    students[name] = roll

print("Keys:", list(students.keys()))
print("Values:", list(students.values()))
