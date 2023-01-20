import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

# Create the main window
root = tk.Tk()

# Create a function to be called when the menu item is selected
def callback():
    # Set up the figure and the plot
    fig, ax = plt.subplots()
    # Generate the data for the sine wave
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    # Plot the sine wave
    ax.plot(x, y)
    # Fill the area under the sine wave
    ax.fill_between(x, y, 0)
    # Show the plot
    plt.show()
# Create the popup menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Sine", command=callback)
menu.add_command(label="Cosine", command=callback)
menu.add_command(label="Tangent", command=callback)

# Bind the popup menu to a right mouse button click event
root.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

# Run the main loop
root.mainloop()
