class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

m1 = int(input("Enter marks of student 1: "))
m2 = int(input("Enter marks of student 2: "))
s1 = Student(m1)
s2 = Student(m2)
print("Total Marks:", s1 + s2)
