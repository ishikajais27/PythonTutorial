departments = {}
n = int(input("Enter number of departments: "))
for _ in range(n):
    dept = input("Enter department name: ")
    students = {}
    m = int(input(f"Enter number of students in {dept}: "))
    for _ in range(m):
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
    departments[dept] = students

print(departments)
