def split_two_digit_number(AB):
    if 10 <= AB <= 99:  # Ensure AB is a two-digit number
        AB_str = str(AB)  # Convert the number to a string
        A = int(AB_str[0])  # Extract the first digit and convert it back to an integer
        B = int(AB_str[1])  # Extract the second digit and convert it back to an integer
        return [A, B]
    else:
        return "Invalid input: The number must be a two-digit number."

def long_multiplication_breakdown(AB, C):
    digits_AB = split_two_digit_number(AB)
    if isinstance(digits_AB, str):  # Check if the returned value is an error message
        return digits_AB, []

    result = [0, 0, 0]  # Initialize the result list for a maximum of three digits
    steps = []

    # Multiplication process
    for i, digit in enumerate(reversed(digits_AB)):
        mul = digit * C
        pos1 = i
        pos2 = i + 1

        total = mul + result[pos2]
        result[pos1] += total % 10
        result[pos2] = total // 10

        step = {
            'Multiplication': f"{digit} * {C}",
            'Addition': f"{mul}"
        }
        steps.append(step)

    # Remove leading zeros and reverse steps to match natural calculation order
    result = int(''.join(map(str, result[::-1])).lstrip('0'))
    steps.reverse()

    return result, steps

def visualize_multiplication_breakdown(AB, C):
    result, multiplication_steps = long_multiplication_breakdown(AB, C)
    if isinstance(result, str):  # Check if the result is an error message
        print(result)
        return

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
