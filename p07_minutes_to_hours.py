# Practical 7: Convert total minutes into hours and minutes

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60        # complete hours
minutes = total_minutes % 60       # remaining minutes

print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")
