
from sympy.interactive import printing
printing.init_printing(use_latex = True)

import numpy as np
import sympy as sp
import cmath

class MathChatbot:
    def __init__(self):
        pass

    def factorize_polynomial(self, expression):
        try:
            # Use Sympy library to factorize the polynomial expression
            factored_expression = sympy.factor(expression)
            return f"The factorized form of {expression} is: {factored_expression}"
        except sympy.SympifyError:
            return "Sorry can you please enter a factorisable polynomial! Updates coming soon."

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
                user_question = input("Ask a question on factorizing polynomials (e.g., x^2 - 4): ")
                response = self.factorize_polynomial(user_question)
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
                print("Really Sorry! We can't do this at the moment :). Please choose from 1, 2, or 3.")

# Example usage
chatbot = MathChatbot()
chatbot.run_chatbot()
