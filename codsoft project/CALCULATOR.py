def Calc(x,y,operation):
    if operation == '+':
        return x+y
    elif operation == '-':
        return x-y
    elif operation == '*':
        return x*y
    elif operation == '/':
        if y!= 0:
            return x/y
        else:
            return "Error:Division by zero"
    else:
        return "Invalid operation"
x= float(input("Enter the value for x:"))
y= float(input("Enter the value for y:"))
print("Choose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter your Operator: ")
result = Calc(x,y,operation)
print(f"The result is: {result}")
