count = 1
while count > 0:

    Choice = int(input("Enter Weekday:\n"
                   " 1: Monday\n"
                   " 2: Tuesday\n"
                   " 3: Wedne1sday\n"
                   " 4: Thursday\n"
                   " 5: Friday\n"
                   " 6: Saturday\n"
                   " 7: Sunday\n"))
    if Choice == 1:
        output = "Monday"
        count = 0
    elif Choice == 2:
        output = "Tuesday"
        count = 0
    elif Choice == 3:
        output = "Wednesday"
        count = 0
    elif Choice == 4:
        output = "Thursday"
        count = 0
    elif Choice == 5:
        output = "Friday"
        count = 0
    elif Choice == 6:
        output = "Saturday"
        count = 0
    elif Choice == 7:
        output = "Sunday"
        count = 0
    else:
        output = "Invalid Choice"
        print("Invalid Choice")
print("It is : ", output)