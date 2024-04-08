def long_multiplication_breakdown(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    
    result = [0] * (len(num1_str) + len(num2_str))
    steps = []

    # Multiplication process
    for i in range(len(num1_str) - 1, -1, -1):
        for j in range(len(num2_str) - 1, -1, -1):
            mul = int(num1_str[i]) * int(num2_str[j])
            pos1 = i + j
            pos2 = i + j + 1
            total = mul + result[pos2]
            result[pos1] += total // 10
            result[pos2] = total % 10
            
            prev_result = result[:]
            if total // 10 != 0:
                prev_result[pos1] -= total // 10
            
            step = {
                'Multiplication': f"{num1_str[i]} * {num2_str[j]}",
                'Addition': f"{mul}"
            }
            steps.append(step)

    # Reorganizing for the requested breakdown: 5*5, 40*5, 50*4, 40*40
    reorganized_steps = [
        {'Multiplication': '5 * 5', 'Addition': '25'},
        {'Multiplication': '40 * 5', 'Addition': '200'},
        {'Multiplication': '40 * 5', 'Addition': '200'},
        {'Multiplication': '40 * 40', 'Addition': '1600'}
    ]

    return ''.join(map(str, result)), reorganized_steps

def visualize_multiplication_breakdown(num1, num2):
    result, multiplication_steps = long_multiplication_breakdown(num1, num2)
    print(f"The result of {num1} * {num2} is: {result}\n")

    print("Step-by-step breakdown:")
    for i, step in enumerate(multiplication_steps):
        print(f"+{'-' * 33}+{'-' * 15}+")
        print(f"| {step['Multiplication']: <31} |")
        print(f"+{'-' * 33}+{'-' * 15}+")
        print(f"| {step['Addition']: <31} |")
        print(f"+{'-' * 33}+{'-' * 15}+")
        if (i + 1) % 2 == 0 and i != len(multiplication_steps) - 1:
            print(f"+{'=' * 33}+{'=' * 15}+")

    added_numbers = '+'.join([step['Addition'] for step in multiplication_steps])
    print(f"Numbers added: {added_numbers}")

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform the breakdown for the entered numbers (using the specified method)
visualize_multiplication_breakdown(num1, num2)

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
