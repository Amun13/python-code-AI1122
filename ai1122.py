def long_multiplication(num1, num2):
    # Convert numbers to strings to iterate through digits
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Initialize result with zeros
    result = [0] * (len(num1_str) + len(num2_str))
    
    # Multiply each digit and store the result in the appropriate position
    for i in range(len(num1_str) - 1, -1, -1):
        for j in range(len(num2_str) - 1, -1, -1):
            # Calculate the product of digits and add it to the result array
            mul = int(num1_str[i]) * int(num2_str[j])
            pos1 = i + j
            pos2 = i + j + 1
            total = mul + result[pos2]
            result[pos1] += total // 10
            result[pos2] = total % 10
    
    # Convert result list to a string
    result_str = ''.join(map(str, result)).lstrip('0')
    
    # Check if the result is an empty string (occurs when result is 0)
    if not result_str:
        return "0"
    
    return result_str

# Example usage:
num1 = 123456789
num2 = 987654321
result = long_multiplication(num1, num2)
print(f"The result of {num1} * {num2} is: {result}")
