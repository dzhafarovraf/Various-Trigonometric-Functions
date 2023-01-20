import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

root = tk.Tk()

def getSine():
  
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.fill_between(x, y, 0)
    plt.show()

def getCosine():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.cos(x)
    ax.plot(x, y)
    ax.fill_between(x, y, 0)
    plt.show()

def getTangent():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.tan(x)
    ax.plot(x, y)
    ax.fill_between(x, y, 0)
    plt.show()

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Sine", command=getSine)
menu.add_command(label="Cosine", command=getCosine)
menu.add_command(label="Tangent", command=getTangent)

root.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

root.mainloop()
