#Jaicee Ball
#11/8/24
#P4LAB2
#Ask User for integer using loops

#Ask integer input from the user
while True:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    
#Check if the number is non-negative
    if number >= 0:
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
            
#Display message if the number is negative
    else:
        print("This program does not handle negative numbers.")
    
#Ask user if they want to run the program again
    repeat = input("Would you like to run the program again?: ").strip().lower()
    if repeat != "yes":
        print("Exiting program...")
        break



