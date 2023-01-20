import matplotlib.pyplot as plt
import numpy as np

def plot_trig_identity(identity):
    # Set up the figure and the plot
    fig, ax = plt.subplots()

    # Generate the data for the identity
    x = np.linspace(-2*np.pi, 2*np.pi, 100)

    if identity == 'sin(x)':
        y = np.sin(x)
    elif identity == 'cos(x)':
        y = np.cos(x)
    elif identity == 'tan(x)':
        y = np.tan(x)
    elif identity == 'csc(x)':
        y = 1 / np.sin(x)
    elif identity == 'sec(x)':
        y = 1 / np.cos(x)
    elif identity == 'cot(x)':
        y = 1 / np.tan(x)
    else:
        print('Invalid identity')
        return

    # Plot the identity
    ax.plot(x, y)

    # Show the plot
    plt.show()

# Test the function with different identities
plot_trig_identity('sin(x)')
plot_trig_identity('cos(x)')
plot_trig_identity('tan(x)')
plot_trig_identity('csc(x)')
plot_trig_identity('sec(x)')
plot_trig_identity('cot(x)')
