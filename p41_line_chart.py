# Practical 41: Line chart using sample data

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2025 = [120, 135, 150, 145, 170, 190]
sales_2026 = [140, 150, 165, 180, 200, 230]

plt.figure(figsize=(8, 5))
plt.plot(months, sales_2025, marker="o", label="2025")
plt.plot(months, sales_2026, marker="s", label="2026")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.grid(True)
plt.legend()

plt.savefig("p41_line_chart.png")
print("Plot saved as p41_line_chart.png")
plt.show()
