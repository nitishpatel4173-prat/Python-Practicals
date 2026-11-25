# Practical 50: Method overloading using default arguments and *args


class Calculator:
    # Technique 1: default arguments - one method, different numbers of arguments
    def area(self, a, b=None):
        if b is None:
            return 3.14159 * a * a      # one argument  -> circle (radius a)
        return a * b                    # two arguments -> rectangle

    # Technique 2: *args - any number of arguments
    def add(self, *args):
        total = 0
        for number in args:
            total += number
        return total


calc = Calculator()

print("Area of circle (radius 5)       :", calc.area(5))
print("Area of rectangle (4 x 6)       :", calc.area(4, 6))
print()
print("add(10, 20)                     :", calc.add(10, 20))
print("add(1, 2, 3, 4, 5)              :", calc.add(1, 2, 3, 4, 5))
print("add()                           :", calc.add())


# Why it is needed: defining two methods with the same name does not overload.
class Demo:
    def show(self):
        print("show() with no arguments")

    def show(self, name):               # noqa: F811 - replaces the one above
        print("show() with name =", name)


demo = Demo()
demo.show("Python")
try:
    demo.show()
except TypeError as error:
    print("Error:", error)
