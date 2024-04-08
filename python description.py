def long_multiplication(num1, num2):
    # Convert numbers to strings to iterate through digits
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Initialize result with zeros
    result = [0] * (len(num1_str) + len(num2_str))
    
    # Multiply each digit and store the result in the appropriate position
    steps = []  # List to store step-by-step calculation details
    
    # Iterate through each digit of num1 and num2
    for i in range(len(num1_str) - 1, -1, -1):
        for j in range(len(num2_str) - 1, -1, -1):
            # Calculate the product of individual digits
            mul = int(num1_str[i]) * int(num2_str[j])
            
            # Determine positions for storing the multiplication result
            pos1 = i + j
            pos2 = i + j + 1
            
            # Perform addition and update result array considering carry-over
            total = mul + result[pos2]
            result[pos1] += total // 10  # Update the carry-over
            result[pos2] = total % 10     # Update the current digit
            
            # Save step-by-step calculation details
            step = f"{num1_str[i]} * {num2_str[j]} = {mul} -> "
            step += f"Add {total // 10} to {result[pos1]} and put {total % 10} in position {pos2}"
            steps.append(step)
    
    # Convert result list to a string, removing leading zeros if present
    result_str = ''.join(map(str, result)).lstrip('0')
    
    # Check if the result is zero
    if not result_str:
        return "0", steps  # Return "0" as the result along with the steps
    
    return result_str, steps  # Return the calculated result string without leading zeros and the steps

def long_multiplication(num1, num2):
    # ... (The previous implementation of long_multiplication function remains the same)
    # (I'm re-using the same function for illustration purposes)

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the long_multiplication function with user-provided numbers
result, steps = long_multiplication(num1, num2)

# Output the multiplication result and steps
print(f"The result of {num1} * {num2} is: {result}")
print("Step-by-step calculation:")
for step in steps:
    print(step)

