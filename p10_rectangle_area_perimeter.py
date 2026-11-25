# Practical 10: Area and perimeter of a rectangle

length = float(input("Enter length of the rectangle : "))
breadth = float(input("Enter breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area      = {area:.2f}")
print(f"Perimeter = {perimeter:.2f}")
