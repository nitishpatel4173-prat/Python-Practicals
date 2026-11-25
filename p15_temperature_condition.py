# Practical 15: Temperature condition (in degrees Celsius)

temperature = float(input("Enter temperature in Celsius: "))

if temperature < 15:
    print("It is COLD. Wear warm clothes.")
elif temperature <= 30:
    print("It is COMFORTABLE. Enjoy the weather.")
else:
    print("It is HOT. Stay hydrated and avoid direct sun.")
