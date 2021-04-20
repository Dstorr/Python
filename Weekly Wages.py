#Weekly Wages
print("============")
print("Weekly Wages")
print("============")

#Name Input
name = input("What is your name?")

#Hourly rate
hourly_rate = float(input("What is your hourly rate?"))
#Regular Hours
regular_hours_worked = int(input("How many regular hours did you work?"))
#Overtime Hours
overtime_hours_worked = int(input("How many overtime hours did you work?"))

#Math for Regular hours, Overtime and Total
regular_hours = regular_hours_worked * hourly_rate
overtime_hours = 1.5 * hourly_rate
Total = regular_hours + overtime_hours

print("\n")

print("Weekly Pay for:", name)

print("\n")

#Output
print("Regular Pay: $", regular_hours)
print("Overtime Pay: $", overtime_hours)
print("Total: $", Total)

print("\n")

#Happy Messages
print("============")
print("Happy Meter")
print("============")

#Happy Question
happy = int(input("How happy are you from a scale of 1-10? "))
print("\n")

#Not happy(3 or less)
if happy <= 3:
    print("You are not happy, cheer up bud.")
#Medium Happy(4 - 7)
elif happy >= 4 and happy <= 7:
    print("You are medium happy, you're doing pretty good bud.")
#Very Happy(8 or higher)
else:
    print("You are very happy, keep it up buddy.")

// hello