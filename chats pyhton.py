import re

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Sorry, I couldn't compute the result. Please enter a valid mathematical expression."

def gcse_math_chatbot():
    print("Welcome to the GCSE Math Chatbot! Enter 'quit' to exit.")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'quit':
            print("Goodbye!")
            break

        # Regular expression to match basic arithmetic expressions
        pattern = r'^\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*([-+*/])\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*$'
        match = re.match(pattern, user_input)
        
        if match:
            num1, operator, num2 = match.groups()
            result = evaluate_expression(f"{num1}{operator}{num2}")
            print(f"Bot: {result}")
        else:
            print("Bot: Please enter a valid mathematical expression (e.g., '2 + 3', '10 * 5', '8 / 2').")

if __name__ == "__main__":
    gcse_math_chatbot()
