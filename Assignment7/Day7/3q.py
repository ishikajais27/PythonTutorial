class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

class Result(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_result(self):
        print("Marks:", self.marks)

name = input("Enter name: ")
marks = int(input("Enter marks: "))
r = Result(name, marks)
r.display()
r.show_result()
