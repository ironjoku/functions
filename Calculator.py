def calculator(num1, num2, operation):
    def add():
        return num1 + num2

    def subtract():
        return num1 - num2

    def multiply():
        return num1 * num2

    def divide():
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"

    if operation == "add":
        return add()
    elif operation == "subtract":
        return subtract()
    elif operation == "multiply":
        return multiply()
    elif operation == "divide":
        return divide()
    else:
        return "Invalid operation"

# Using the function
num_1 = 160
num_2 = 5
op = "divide"

result = calculator(num_1, num_2, op)
print(f"Result of {num_1} {op} {num_2} is: {result}")
