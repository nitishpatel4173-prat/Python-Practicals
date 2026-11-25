# Practical 11: Speed, Distance and Time calculator

print("Speed, Distance and Time Calculator")
print("1. Calculate Speed")
print("2. Calculate Distance")
print("3. Calculate Time")
choice = input("Enter your choice (1/2/3): ").strip()

if choice == "1":
    distance = float(input("Enter distance (km): "))
    hours = float(input("Enter time (hours): "))
    if hours == 0:
        print("Error: Time cannot be zero.")
    else:
        print(f"Speed = Distance / Time = {distance / hours:.2f} km/h")
elif choice == "2":
    speed = float(input("Enter speed (km/h): "))
    hours = float(input("Enter time (hours): "))
    print(f"Distance = Speed x Time = {speed * hours:.2f} km")
elif choice == "3":
    distance = float(input("Enter distance (km): "))
    speed = float(input("Enter speed (km/h): "))
    if speed == 0:
        print("Error: Speed cannot be zero.")
    else:
        print(f"Time = Distance / Speed = {distance / speed:.2f} hours")
else:
    print("Invalid choice! Please enter 1, 2 or 3.")
