def long_multiplication(num1, num2):
    # Convert numbers to strings to iterate through digits
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Initialize result with zeros
    result = [0] * (len(num1_str) + len(num2_str))
    
    # Multiply each digit and store the result in the appropriate position
    steps = []
    for i in range(len(num1_str) - 1, -1, -1):
        for j in range(len(num2_str) - 1, -1, -1):
            # Calculate the product of digits and add it to the result array
            mul = int(num1_str[i]) * int(num2_str[j])
            pos1 = i + j
            pos2 = i + j + 1
            total = mul + result[pos2]
            result[pos1] += total // 10
            result[pos2] = total % 10
            
            # Save step-by-step calculation
            step = f"{num1_str[i]} * {num2_str[j]} = {mul} -> "
            step += f"Add {total // 10} to {result[pos1]} and put {total % 10} in position {pos2}"
            steps.append(step)
    
    # Convert result list to a string
    result_str = ''.join(map(str, result)).lstrip('0')
    
    # Check if the result is an empty string (occurs when result is 0)
    if not result_str:
        return "0", steps
    
    return result_str, steps

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform long multiplication
result, multiplication_steps = long_multiplication(num1, num2)

# Display the step-by-step method
print(f"The result of {num1} * {num2} is: {result}\n")
print("Step-by-step method:")
for step in multiplication_steps:
    print(step)
def long_multiplication(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    result = [0] * (len(num1_str) + len(num2_str))
    steps = []

    for i in range(len(num1_str) - 1, -1, -1):
        for j in range(len(num2_str) - 1, -1, -1):
            mul = int(num1_str[i]) * int(num2_str[j])
            pos1 = i + j
            pos2 = i + j + 1
            total = mul + result[pos2]
            result[pos1] += total // 10
            result[pos2] = total % 10

            step = f"{num1_str[i]} * {num2_str[j]} = {mul} -> "
            step += f"Add {total // 10} to {result[pos1]} and put {total % 10} in position {pos2}"
            steps.append(step)

    result_str = ''.join(map(str, result)).lstrip('0')

    if not result_str:
        return "0", steps

    return result_str, steps

def visualize_multiplication(num1, num2):
    result, multiplication_steps = long_multiplication(num1, num2)
    print(f"The result of {num1} * {num2} is: {result}\n")

    print("Step-by-step method:")
    print(f"{'-' * 40}")
    print(f"| {'Multiplication':^15} | {'Addition':^23} |")
    print(f"{'-' * 40}")

    for step in multiplication_steps:
        mul, add = step.split(" -> ")
        mul = mul.split("=")[1].strip()
        add = add.split(" and put ")
        add_first = add[0].split("Add ")[1]
        add_second = add[1].split(" in position ")

        print(f"| {mul:^15} | {add_first + ' ':^15} | {add_second[1]:^15} |")
        print(f"{'-' * 40}")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

visualize_multiplication(num1, num2)

def perform_arithmetic_operation(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"


def calculate_percentage(original_value, percentage):
    return (percentage / 100) * original_value


def solve_linear_equation(a, b):
    if a != 0:
        return -b / a
    else:
        return "The equation is not linear (a cannot be zero)"


# Example usage:
print("GCSE Math Problem Solver")
print("========================\n")
print("1. Arithmetic Operations:")
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

result = perform_arithmetic_operation(operation, num1, num2)
print(f"Result of {num1} {operation} {num2} is: {result}\n")

print("2. Percentage Calculation:")
original_value = float(input("Enter the original value: "))
percentage = float(input("Enter the percentage (without % symbol): "))

percentage_result = calculate_percentage(original_value, percentage)
print(f"{percentage}% of {original_value} is: {percentage_result}\n")

print("3. Linear Equation Solver (ax + b = 0):")
a_value = float(input("Enter the 'a' value: "))
b_value = float(input("Enter the 'b' value: "))

solution = solve_linear_equation(a_value, b_value)
print(f"The solution to the equation {a_value}x + {b_value} = 0 is: {solution}")


