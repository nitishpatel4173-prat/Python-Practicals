# Practical 43: Line width, colour and pattern (linestyle) in matplotlib

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 2, 3, 4, 5]
y2 = [0, 2, 4, 6, 8, 10]
y3 = [0, 3, 6, 9, 12, 15]
y4 = [0, 4, 8, 12, 16, 20]

plt.figure(figsize=(8, 5))
plt.plot(x, y1, color="red", linewidth=1, linestyle="-", label="solid, width 1")
plt.plot(x, y2, color="green", linewidth=2, linestyle="--", label="dashed, width 2")
plt.plot(x, y3, color="blue", linewidth=3, linestyle="-.", marker="o",
         markersize=8, label="dash-dot, width 3, circles")
plt.plot(x, y4, color="#ff8800", linewidth=4, linestyle=":", alpha=0.7,
         label="dotted, width 4, 70% opaque")

plt.title("Line Attributes in Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig("p43_line_attributes.png")
print("Plot saved as p43_line_attributes.png")
plt.show()
