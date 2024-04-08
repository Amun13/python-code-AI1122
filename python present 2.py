def long_multiplication_breakdown(AB, C):
    AB_str = str(AB)
    C_str = str(C)
    
    # Assuming AB is a two-digit number and C is a single-digit number
    if len(AB_str) != 2 or len(C_str) != 1:
        return "Invalid input: AB should be a two-digit number and C should be a single-digit number.", []
    
    result = [0] * (len(AB_str) + len(C_str))
    steps = []

    # Multiplication process
    for i in range(len(AB_str) - 1, -1, -1):
        mul = int(AB_str[i]) * int(C_str)
        pos1 = i
        pos2 = i + 1
        total = mul + result[pos2]
        result[pos1] += total // 10
        result[pos2] = total % 10

        step = {
            'Multiplication': f"{AB_str[i]} * {C_str}",
            'Addition': f"{mul}"
        }
        steps.append(step)

    # Reorganize steps for clarity
    steps.reverse()  # Reverse the steps to match the natural calculation order

    return ''.join(map(str, result)).lstrip('0'), steps

def visualize_multiplication_breakdown(AB, C):
    result, multiplication_steps = long_multiplication_breakdown(AB, C)
    print(f"The result of {AB} * {C} is: {result}\n")

    print("Step-by-step breakdown:")
    for i, step in enumerate(multiplication_steps):
        print(f"+{'-' * 33}+")
        print(f"| {step['Multiplication']: <31} |")
        print(f"+{'-' * 33}+")
        print(f"| {step['Addition']: <31} |")
        print(f"+{'-' * 33}+")
        if (i + 1) < len(multiplication_steps):
            print(f"+{'=' * 33}+")

    added_numbers = '+'.join([step['Addition'] for step in multiplication_steps])
    print(f"Numbers added: {added_numbers}")

# Example usage with AB as a two-digit number and C as a single-digit number
AB = 45  # Example two-digit number
C = 6    # Example single-digit number
visualize_multiplication_breakdown(AB, C)
