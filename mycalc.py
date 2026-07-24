num1=float(input("Enter first number for math operation: "))
num2=float(input("Enter second number for math operation: "))
operation=input("Enter operation you would like to perform (+, -, *, /): ")
match operation:
    case "+":   print(num1 + num2)
    case "-":   print(num1 - num2)
    case "*":   print(num1 * num2)
    case "/":   print(num1 / num2)              
    case _:   print("Invalid operation")