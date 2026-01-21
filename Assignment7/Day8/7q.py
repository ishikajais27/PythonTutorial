import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
x = [int(input(f"Enter x value {i+1}: ")) for i in range(n)]
y = [int(input(f"Enter y value {i+1}: ")) for i in range(n)]
plt.plot(x, y, marker='o')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Graph")
plt.show()
