import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

def menu():
   
    options = {
        1: option_Sine_1,
        2: option_Cosine_2,
        3: option_Tangent_3,
        4: exit
    }

    print("Select a trigonometric function:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    print("4. Exit")

    choice = input("Enter your choice: ")

    while choice not in options:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")

  
    options[choice]()

def option_Sine_1():

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
    menu() 

def option_Cosine_2():

    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.cos(x)
    ax.plot(x, y)
    ax.fill_between(x, y, 0)
    plt.show()
    menu() 

def option_Tangent_3():

    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.tan(x)
    ax.plot(x, y)
    ax.fill_between(x, y, 0)
    plt.show()
    menu()  

def exit():
    print("later sk8er...")

menu()
