import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Create the main window
root = tk.Tk()

# Define a function to be called when a menu item is selected
def callback(event):
    # Get the selected menu item label
    label = event.widget.entrycget(event.widget.index(event.widget.focus()), "label")

    # Create a figure and plot the selected function
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    if label == "Sine":
        y = np.sin(x)
    elif label == "Cosine":
        y = np.cos(x)
    elif label == "Tangent":
        y = np.tan(x)
    elif label == "Cotangent":
        y = 1 / np.tan(x)
    elif label == "Secant":
        y = 1 / np.cos(x)
    elif label == "Cosecant":
        y = 1 / np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel(label)
    ax.set_title(label + " function")
    plt.show()

# Create the popup menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Sine", command=callback)
menu.add_command(label="Cosine", command=callback)
menu.add_command(label="Tangent", command=callback)
menu.add_command(label="Cotangent", command=callback)
menu.add_command(label="Secant", command=callback)
menu.add_command(label="Cosecant", command=callback)

# Bind the popup menu to a right mouse button click event
root.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

# Run the main loop
root.mainloop()
