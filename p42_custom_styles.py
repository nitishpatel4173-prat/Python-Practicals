# Practical 42: Styles and custom themes in matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 5, 3, 8, 6, 9]

# A custom theme is a dictionary of rcParams settings
custom_theme = {
    "axes.facecolor": "#fff8e7",
    "axes.grid": True,
    "grid.linestyle": "--",
    "lines.linewidth": 3,
    "lines.color": "teal",
    "axes.titleweight": "bold",
    "font.size": 11,
}

fig = plt.figure(figsize=(14, 4))

# Built-in style 1
with plt.style.context("ggplot"):
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.plot(x, y)
    ax1.set_title("Style: ggplot")

# Built-in style 2
with plt.style.context("dark_background"):
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.plot(x, y)
    ax2.set_title("Style: dark_background")

# Custom theme
with plt.rc_context(custom_theme):
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.plot(x, y)
    ax3.set_title("Custom theme")

fig.tight_layout()
fig.savefig("p42_custom_styles.png")
print("Plot saved as p42_custom_styles.png")
plt.show()
