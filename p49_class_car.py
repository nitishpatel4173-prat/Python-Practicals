# Practical 49: Class Car with multiple objects


class Car:
    """A simple Car class."""

    wheels = 4                      # class attribute shared by all cars

    def __init__(self, brand, model, year, color):
        self.brand = brand          # instance attributes (different for every car)
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} | Colour: {self.color} "
              f"| Wheels: {Car.wheels}")

    def age(self, current_year):
        return current_year - self.year


car1 = Car("Toyota", "Fortuner", 2022, "White")
car2 = Car("Honda", "City", 2019, "Silver")
car3 = Car("Tata", "Nexon", 2024, "Blue")

for car in (car1, car2, car3):
    car.display_info()

print("\nAge of car2 in 2026:", car2.age(2026), "years")
print("Brand of car3      :", car3.brand)
