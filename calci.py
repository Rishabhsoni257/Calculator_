def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

print("Simple Calculator")
print("Type 'exit' to quit")

while True:
    expression = input("\nEnter calculation (e.g. 10 + 5): ")

    if expression.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        num1, operator, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)

        result = calculate(num1, operator, num2)
        print("Result:", result)

    except:
        print("Invalid format. Use: number operator number")
