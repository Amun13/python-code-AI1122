pip install sympy

import sympy as sp
import cmath

class MathChatbot:
    def __init__(self):
        pass

    def factorize_polynomial(self, expression):
        try:
            # Convert the string expression to a sympy expression
            expr = sp.sympify(expression)
            # Use Sympy to factorize the polynomial expression
            factored_expression = sp.factor(expr)
            return f"The factorized form of {expression} is: {factored_expression}"
        except sp.SympifyError:
            return "Sorry, please enter a factorizable polynomial! Updates coming soon."

    def quadratic_formula(self, a, b, c):
        try:
            # Calculate solutions using the quadratic formula
            discriminant = cmath.sqrt(b**2 - 4*a*c)
            root1 = (-b + discriminant) / (2*a)
            root2 = (-b - discriminant) / (2*a)
            return f"The solutions are: {root1} and {root2}"
        except ZeroDivisionError:
            return "Coefficient 'a' cannot be zero. Please enter valid coefficients."

    def run_chatbot(self):
        print("Welcome to the Math Chatbot!")
        while True:
            user_choice = input("Choose an option (1. Factorize Polynomial, 2. Quadratic Formula, 3. Exit): ")

            if user_choice == '1':
                user_expression = input("Enter a polynomial to factorize (e.g., x**2 - 4): ")
                response = self.factorize_polynomial(user_expression)
                print(response)

            elif user_choice == '2':
                a = float(input("Enter the coefficient 'a' in the quadratic equation: "))
                b = float(input("Enter the coefficient 'b' in the quadratic equation: "))
                c = float(input("Enter the coefficient 'c' in the quadratic equation: "))
                response = self.quadratic_formula(a, b, c)
                print(response)

            elif user_choice == '3':
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose from 1, 2, or 3.")

# Example usage
chatbot = MathChatbot()
chatbot.run_chatbot()
