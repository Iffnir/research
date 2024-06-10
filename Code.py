Number1 = int(input("Enter Number 1:"))
Number2 = int(input("Enter Number 2:"))
count = 1
while count > 0:
    Choice = int(input("Enter Choice:\n"
   " 1: Addition\n"
   " 2: Subtraction\n"
   " 3: Multiplication\n"
   " 4: Division\n"))
    if Choice == 1:
        output = Number1 + Number2
        count = 0
    elif Choice == 2:
        output = Number1 - Number2
        count = 0
    elif Choice == 3:
        output = Number1 * Number2
        count = 0
    elif Choice == 4:
        output = Number1 / Number2
        count = 0
    else:
       output = "Invalid Choice."
print("Result : ", output)
