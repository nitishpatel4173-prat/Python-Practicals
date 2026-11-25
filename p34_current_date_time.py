# Practical 34: Current date and time using the datetime module

from datetime import datetime

now = datetime.now()

print("Current date and time :", now)
print("Date only             :", now.date())
print("Time only             :", now.time())
print("Formatted date        :", now.strftime("%d-%m-%Y"))
print("Formatted time (12 h) :", now.strftime("%I:%M:%S %p"))
print("Day of the week       :", now.strftime("%A"))
print("Month name            :", now.strftime("%B"))
print("Year                  :", now.year)
