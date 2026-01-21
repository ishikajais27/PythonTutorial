import matplotlib.pyplot as plt

n = int(input("Enter number of students: "))
names = [input(f"Enter name of student {i+1}: ") for i in range(n)]
marks = [int(input(f"Enter marks of {names[i]}: ")) for i in range(n)]
plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Chart of Student Marks")
plt.show()
