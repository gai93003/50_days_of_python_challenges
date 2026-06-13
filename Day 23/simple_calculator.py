import operator

def calculator():
    try:
        num1 = int(input("Enter number: "))
        opt = input("Pick operator (+ - / *) : ")
        num2 = int(input("Enter another number: "))

        if opt not in ['+', '-', '*', '/'] or len(opt) > 1:
            print("Please enter a valid operator")
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("You cannot divide a number by zero, Try again")
    else:
        if opt == "+":
            return f"Ans is: {operator.add(num1, num2)}"
        elif opt == "-":
            return f"Ans is: {operator.sub(num1, num2)}"
        elif opt == "*":
            return f"Ans is: {operator.mul(num1, num2)}"
        elif opt == "/":
            return f"Ans is: {operator.truediv(num1, num2)}"
        
    return "Try again"

print(calculator())