import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function to plot
def f(x1, x2):
    return -12*x2 + 4*np.power(x1, 2) + 4*np.power(x2, 2) - 4*x1*x2

# Generate x and y values
x = np.linspace(0.5, 1, 50)
y = np.linspace(0.5, 1, 50)
X, Y = np.meshgrid(x, y)

# Compute the function values for each (x, y) pair
Z = f(X, Y)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

# Add labels and title
ax.set_xlabel('X1')
ax.set_ylabel('x2')
ax.set_zlabel('Z')
ax.set_title('Given function')

# Show the plot
plt.show()