import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) =  y=(x+3)²
def function(x):
    return (x+3)**2

# Define the derivative of the function f'(x) = 2(x+3)
def derivative(x):
    return 2 * (x + 3)

# Gradient Descent Algorithm
def gradient_descent(learning_rate, epochs):
    x = 10  # Initial value of x
    history = []  # To store the history of x values

    for _ in range(epochs):
        gradient = derivative(x)
        x = x - learning_rate * gradient  # Update x
        history.append(x)

    return x, history

# Parameters
learning_rate = 0.1
epochs = 50

# Run Gradient Descent
minima, history = gradient_descent(learning_rate, epochs)

# Output and Plot
print(f"The local minima occurs at: {minima}")

plt.plot([function(x) for x in history])
plt.title("Value of function at each iteration")
plt.xlabel("Iteration")
plt.ylabel("f(x)")
plt.show()