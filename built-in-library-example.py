# Using Python built-in libraries

# Import the datetime library to use it in the program
import datetime

# Assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month

month_word = time.strftime("%B")

today = datetime.datetime.today()

weekday = today.weekday()
'''
# Get day of week from user as integer
weekday = int(input("Enter an integer 0-6 as the day of the week: "))
'''
# Display date/time
print(f"The Current Date And Time Is {time}")
print(f"The Current Month Is {month}")
print(f"The Current Month Is {month_word}")
print(f"Today is {today}")
print(f"The day of the week is {weekday}\n")

# Gets the dataetype of the variables
print(type(weekday))
print()

# if-else statements to determine the day of the week
if weekday == 0:
    weekday_word = "Monday"
elif weekday == 1:
    weekday_word = "Tuesday"
elif weekday == 2:
    weekday_word = "Wednesday"
elif weekday == 3:
    weekday_word = "Thursday"
elif weekday == 4:
    weekday_word = "Friday"
elif weekday == 5:
    weekday_word = "Saturday"
elif weekday == 6:
    weekday_word = "Sunday"

else:
    print("Invalid day of the week!!!")
    weekday_word = "INVALID"

print()
print(f"The day of the week is {weekday_word}")


