# Practical 21: Accessing and modifying list elements using indexing

colors = ["red", "green", "blue", "yellow", "black"]
print("Original list  :", colors)

# ---------- Accessing ----------
print("First element  :", colors[0])
print("Third element  :", colors[2])
print("Last element   :", colors[-1])
print("Second last    :", colors[-2])

# ---------- Modifying ----------
colors[1] = "orange"          # change using a positive index
colors[-1] = "white"          # change using a negative index
print("After modifying:", colors)

# ---------- Adding and removing using positions ----------
colors.append("pink")         # add at the end
colors.insert(2, "purple")    # add at index 2
removed = colors.pop(0)       # remove the element at index 0
print("After append, insert, pop:", colors)
print("Removed element:", removed)

# ---------- Index with a loop ----------
for index, color in enumerate(colors):
    print(f"colors[{index}] = {color}")

# ---------- Invalid index ----------
try:
    print(colors[10])
except IndexError as error:
    print("Error:", error)
