import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x+3)**2

def df(x):
    return 2*(x+3)

def gradientdescent(initial_value, learning_rate, num_iterations):
    x = initial_value
    x_history = [x]
    for i in range(num_iterations):
        gradient = df(x)
        x = x - learning_rate * gradient
        x_history.append(x)
    return x, x_history

initial_value = 2
learning_rate = 0.1
num_iterations = 30
x, x_history = gradientdescent(initial_value, learning_rate, num_iterations)
print("Local minimum is:", x)

x_vals = np.linspace(-5, 5, 100)
plt.plot(x_vals, f(x_vals))
plt.plot(2, f(2), 'rx')
plt.show()

x_vals = np.linspace(-5, 5, 100)
plt.plot(x_vals, f(x_vals)) #(x,y)
plt.plot(x_history, f(np.array(x_history)), 'rx')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent")
plt.show()
