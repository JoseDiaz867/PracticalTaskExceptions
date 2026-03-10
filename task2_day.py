"""
Write a program that analyzes the entered number and, depending on the number, gives the day of the week 
that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take into account cases of entering 
numbers from 8 and more, as well as cases of entering non-numerical data.
"""

def day_of_week():

    try:
        day_number = int(input("Enter a number (1-7) to find out the corresponding day of the week: "))
        days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

        if (day_number not in days):
            raise ValueError
        
        print(f"The number {day_number} corresponds to {days[day_number]}")
        
    except ValueError:
        print("Invalid input. Please enter a integer between 1 and 7.")

# Test.
day_of_week()