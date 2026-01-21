class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

name = input("Enter name: ")
roll_no = input("Enter roll number: ")
marks = int(input("Enter marks: "))
s = Student(name, roll_no, marks)
s.display()
