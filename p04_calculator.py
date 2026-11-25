# Practical 4: Simple arithmetic calculator

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

print("Operators: +  -  *  /  //  %  **")
operator = input("Choose an operator: ").strip()

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator in ("/", "//", "%"):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    elif operator == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    elif operator == "//":
        print(f"{num1} // {num2} = {num1 // num2}")
    else:
        print(f"{num1} % {num2} = {num1 % num2}")
elif operator == "**":
    print(f"{num1} ** {num2} = {num1 ** num2}")
else:
    print("Invalid operator! Please use + - * / // % **")
