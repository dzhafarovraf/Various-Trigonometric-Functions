import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

# Set up the figure and the plot
fig, ax = plt.subplots()

# Generate the data for the sine wave
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Plot the sine wave
line, = ax.plot(x, y)

# Define the function to integrate
def f(x):
    return np.sin(x)

# Set the limits of the integration
a = 0
b = 2*np.pi

# Calculate the area under the curve
area, _ = simpson(f, a, b)

# Add a label to the line showing the area under the curve
line.set_label(f'Area: {area:.2f}')

# Add a legend
ax.legend()

# Show the plot
plt.show()
