class Student:
    def display(self):
        print("Display method in Student class")

class Result(Student):
    def display(self):
        print("Display method in Result class")

r = Result()
r.display()
