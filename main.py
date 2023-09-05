#define the caculator function
def calculator():

    #taking the input from the user
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    operation=input("Choose the operation[+,-,*,/]:")

    # perform the selected operation
    if operation=="+":
        result=num1+num2
    elif operation=="-":
        result=num1-num2
    elif operation=="*":
        result=num1*num2
    elif operation=="/":
        result=num1/num2
    else:
        print("Invalid Operation Selected")
        return

    # print the result
    print("The result is:",result)

#calling the calculator function
calculator()
