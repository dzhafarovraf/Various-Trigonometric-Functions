import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

OPTION_DISPLAY_PROMPT1 = 1
OPTION_DISPLAY_PROMPT2  = 2
OPTION_DISPLAY_PROMPT3 = 3
OPTION_DISPLAY_PROMPT4 = 4
OPTION_QUIT = 5

def display_menu():
  print("\nWelcome!")
  print("Select a trigonometric identity")
  print("1. Sine")
  print("2. Cosine")
  print("3. Tangent") 
  print("4. Cosecant")
  print("5. Secant")
  print("6. Cotangent")
  print("7. Arcsine")
  print("8. Arccosine")
  print("9. Arctangent")

def get_menu_choice():
    choice = int(input("\nEnter your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("\nInvalid choice. Please enter a valid option: "))
    return choice

def display_submenu():
    print("\nSelect Option: ")
    print("1. Display Graph")
    print("2. Display Area under Curve")
    print("3. Return to Previous Menu")
    print("4.Quit")

def get_submenu_choice():
    choice = int(input("\nEnter your choice: "))
    while choice < 1 or choice > 3:
        choice = int(input("\nInvalid choice. Please enter a valid option: "))
    return choice

def display_singraph():
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
    
def display_cosgraph():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.cos(x)
    ax.plot(x, y)
    ax.fill_between(x, y, 0)
    plt.show()

display_menu()
choice = get_menu_choice()
while choice != OPTION_QUIT:
  if choice == OPTION_DISPLAY_PROMPT1:
    display_submenu()
    submenuchoice = get_submenu_choice()
    if submenuchoice == 1:
        display_graph()
    elif submenuchoice == 2:
        display_menu()
  #elif choice == OPTION_DISPLAY_PROMPT2:
    #display_area()
  #elif choice == OPTION_DISPLAY_PROMPT3:
    #add_car()
  #elif choice == OPTION_DISPLAY_PROMPT4:
    #add_customer()
  display_menu()
  choice = get_menu_choice()

print("\nGoodbye!")