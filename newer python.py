import re

def evaluate_expression_with_explanation(expression):
    try:
        result = eval(expression)
        explanation = f"Step-by-step calculation: {expression} = {result}"
        return result, explanation
    except Exception as e:
        return None, "Sorry, I couldn't compute the result. Please enter a valid mathematical expression."

def greet_user():
    print("Welcome to the Personalized GCSE Math Chatbot! Let's do some math.")
    print("You can also chat with me. Type 'quit' to exit at any time.")

def respond_to_greeting(message):
    if "hello" in message.lower():
        return "Hello there! How are you today?"
    elif "fine" in message.lower() or "good" in message.lower():
        return "That's great to hear! Ready to solve some math problems?"
    else:
        return "Nice to chat with you! Let's solve some math problems."

def gcse_math_chatbot():
    greet_user()
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'quit':
            print("Goodbye! Have a great day!")
            break

        response = respond_to_greeting(user_input)
        if response:
            print(f"Bot: {response}")
        else:
            # Regular expression to match basic arithmetic expressions
            pattern = r'^\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*([-+*/])\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*$'
            match = re.match(pattern, user_input)
            
            if match:
                num1, operator, num2 = match.groups()
                result, explanation = evaluate_expression_with_explanation(f"{num1}{operator}{num2}")
                print(f"Bot: {result}")
                print(f"Bot Explanation: {explanation}")
            else:
                print("Bot: Please enter a valid mathematical expression (e.g., '2 + 3', '10 * 5', '8 / 2').")

if __name__ == "__main__":
    gcse_math_chatbot()
