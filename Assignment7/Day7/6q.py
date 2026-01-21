class Student:
    def __init__(self, name):
        self.name = name

class Marks(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

class Result(Marks):
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter name: ")
marks = int(input("Enter marks: "))
r = Result(name, marks)
r.display()
