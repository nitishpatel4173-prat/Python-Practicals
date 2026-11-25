# Practical 5: Convert days into years, weeks and remaining days (1 year = 365 days)

total_days = int(input("Enter number of days: "))

years = total_days // 365          # complete years
remaining = total_days % 365       # days left after removing the years
weeks = remaining // 7             # complete weeks in the remaining days
days = remaining % 7               # days left after removing the weeks

print(f"{total_days} days = {years} year(s), {weeks} week(s) and {days} day(s)")
