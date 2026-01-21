from abc import ABC, abstractmethod


class Student(ABC):
    @abstractmethod
    def display(self):
        pass

class Result(Student):
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter name: ")
marks = int(input("Enter marks: "))
r = Result(name, marks)
r.display()
