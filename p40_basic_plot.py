# Practical 40: A basic plot using matplotlib
# Install once (macOS Terminal):  pip3 install matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [value ** 2 for value in x]      # squares of x

plt.plot(x, y)
plt.title("Squares of Numbers")
plt.xlabel("Number (x)")
plt.ylabel("Square (y)")

plt.savefig("p40_basic_plot.png")    # saves the picture in the current folder
print("Plot saved as p40_basic_plot.png")
plt.show()                           # opens the plot window
