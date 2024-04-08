print("Welcome to the Maths Chatbot!")

def greet_and_proceed():
    greeting_response = input("Hello there! How are you today?\n")

    if "fine" in greeting_response.lower() or "good" in greeting_response.lower():
        print("That's great to hear! Let's solve some math problems.")
    else:
        print("Nice to chat with you! Let's solve some math problems.")
    
    # After the greeting interaction, proceed to the main menu
    main_menu()

def main_menu():
    while True:
        
        option = input("Please press 0 to start: ")
        
        if option == '1':
            multiply_and_explain()
        elif option == '2':
            factorize_difference_of_squares()
        elif option == '3':
            solve_quadratic()
        elif option == '0':
            print("Starting the program. Welcome!")
            break
        else:
            print("Invalid option, please type 1, 2, 3, or 4.")

# The previously defined functions (multiply_and_explain, factorize_difference_of_squares, and solve_quadratic) should be included here as well.

if __name__ == "__main__":
    greet_and_proceed()

import webbrowser  # Import webbrowser module to open URLs in a web browser

def multiply_and_explain():
    # User input for numbers to multiply
    print("\n---- Multiplying a two-digit number by a single-digit number ----\n")
    print("\nYou have chosen option 1!")
    print("\nThis will be in the form of AB*C where A, B and C can be any whole numbers") 
    AB = int(input("\nEnter a two-digit number (AB): "))
    C = int(input("Enter a single-digit number (C): "))

    # Ensure AB is a two-digit number and C is a single-digit number
    if not (10 <= AB <= 99 and 0 <= C <= 9):
        print("AB must be a two-digit number and C must be a single-digit number.")
        return

    # Split the two-digit number AB into its digits A and B
    A = AB // 10  # Get the tens place digit
    B = AB % 10   # Get the ones place digit

    # Multiply each digit by C
    A_times_C = A * C
    B_times_C = B * C

    # Combine the results to get the final answer
    result = A_times_C * 10 + B_times_C

    # Detailed explanation with the user's numbers
    explanation = f"\nStep 1: To multiply {AB} by {C}, we break down {AB} into its digits: {A} (tens) and {B} (ones).\n\n"
    explanation += f"Step 2: We then multiply each digit by {C}: {A} * {C} = {A_times_C} (tens) and {B} * {C} = {B_times_C} (ones).\n\n"
    explanation += f"Step 3: We then combine these results: {A_times_C}0 (since it's in the tens place so we multiply the answer by 10) + {B_times_C} = {result}.\n\n"
    explanation += "Step 4: This is how we multiply a two-digit number by a single-digit number in a step-by-step manner.\n"

    print(explanation)

    # Provide an option to learn more about multiplication
    print("\n\nIt is always a good idea to practise checking your answers! \n\n\n\nPlease follow the link below for a quick youtube video for guidance if you need it!")
    print("\nFor more detailed explanations on multiplication and other math topics, you can visit Khan Academy or other educational websites.")
    learn_more = input("\nWould you like to watch a video on this topic? If yes type '0' otherwise type '1'): ").lower()
    if learn_more == '0':
        webbrowser.open("https://www.youtube.com/watch?v=SfxULALs_u8&ab_channel=KhanAcademy")
        print("Opening youtube video now...")
    elif learn_more == '1':
        print("\nContinuing with the program...")
    else:
        print("Invalid input. Please enter '0' for yes or '1' for no.")



    
import cmath  # Import complex math module
import webbrowser  # Import webbrowser module to open URLs in a web browser

def solve_quadratic():
    while True:
        print("\n---- Solving a Quadratic Equation ----\n")
        print("\nYou have chosen option 2!")
        print("\nThe standard form of a quadratic is ax^2 + bx + c where a, b, and c are whole numbers (which can be positive or negative).")
        print("\n The formula for the discriminant (D) is {b}^2 - 4*{a}*{c}.")
        print("\nThe discriminant is what determines how many roots there are (0, 1, or 2)")
        print("\nThere are 3 cases:")
        print("\nWhen D = 0, this means that there is 1 repeated root.")
        print("\nWhen D > 0, this means that there are 2 different roots.")
        print("\nWhen D < 0, this means that there are no roots (no solutions)")

        a = int(input("\nEnter the coefficient 'a' in the quadratic equation: "))
        b = int(input("\nEnter the coefficient 'b' in the quadratic equation: "))
        c = int(input("\nEnter the coefficient 'c' in the quadratic equation: "))

        discriminant = (b**2) - (4*a*c)

        if a == 0:
            print("Coefficient 'a' cannot be 0 in a quadratic equation.")
            
            continue

        explanation = f"\n\n\n\nGiven the equation {a}x^2 + {b}x + {c} = 0:\n\n"
        explanation += f"Step 1. Coefficients are a = {a}, b = {b}, c = {c}.\n\n"
        explanation += "Step 2. The quadratic formula is x = (-b ± sqrt(b^2 - 4ac)) / (2a).\n\n"
        explanation += f"Step 3. Discriminant (D) is {b}^2 - 4*{a}*{c} = {discriminant}.\n"

        if discriminant >= 0 and (discriminant**0.5).is_integer():
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)

            explanation += "        Since D is non-negative and a perfect square, the equation has real roots that are factorizable.\n\n"
            explanation += "Step 4. Calculate the roots using the quadratic formula:\n"
            explanation += f"        x1 = (-{b} + sqrt({discriminant})) / (2*{a}) = {root1},\n"
            explanation += f"        x2 = (-{b} - sqrt({discriminant})) / (2*{a}) = {root2}.\n"
            explanation += f"        The real solutions are x1 = {root1} and x2 = {root2}.\n\n"

            # Modify the explanation for the factors to correctly handle negative roots
            factor1 = f"(x - {root1})" if root1 >= 0 else f"(x + {-root1})"
            factor2 = f"(x - {root2})" if root2 >= 0 else f"(x + {-root2})"
            explanation += f"Step 5. The solutions lead to the factors {factor1} and {factor2},\n"
            explanation += "        indicating the points where the quadratic equation intersects the x-axis.\n"
            print(explanation)
            
            # Ask the user if they want to access the video
            print("\n\n\nIt is always a good idea to practise checking your answers! \n\n\n\n\nLuckily with factorising quadratics, we can do this by 'Expanding the Brackets'.\n\nPlease follow the link below for a quick youtube video for guidance if you need it!")
            access_video = input("\nWould you like to watch a video on this topic? If yes type '0' otherwise type '1'): ").strip().lower()
            if access_video == '0':
                url = 'https://www.youtube.com/watch?v=Dvo1Q-yBBhk&ab_channel=Cognito'
                webbrowser.open(url)
            
            break  # Exit the loop since we've found factorizable solutions

        else:  # Handling non-factorizable solutions
            print("\nThe provided coefficients do not lead to any roots because the discriminant is negative. Please try again with different values.")
            # No break here to allow the user to try again

import webbrowser  # Import webbrowser module to open URLs in a web browser

        
def is_perfect_square(number):
    # Check if the number is a perfect square
    return number == int(number**0.5) ** 2

def factorize_difference_of_squares():
    print("\n---- The Difference of Squares Quadratic Factorisation Method ----\n")
    print("\nYou have chosen option 3: Factorise a difference of squares")
    print("\nFirst, we will provide a brief explanation of the 'The Difference of Squares Quadratic Factorisation Method'.")
    print("\nThe general standard form of a quadratic which we will be solving in this chatbot is ax^2+bx+c where a, b and c are whole numbers (which can be positive or negative).")
    print("\nThis is the specific case where in the standard form of the quadratic (ax^2+bx+c) the b=0 and the a=1 and the c must be subtracted from the x^2!")
    print("\nMake sure this is the case to use this option, otherwise please use option 2.")
    print("\nThis means that the quadratic has the standard form of x^2 - c.")
    print("\nThis is because in algebra 1 times a letter is just the letter and anything times 0 is nothing so that whole part disappears.")
    print("\nAnother condition on c is that it must be a square number.")
    print("\nA square number is the result when a number has been multiplied by itself.")
    print("\nWe are now going to be solving for x^2 - c.")

    while True:
        c_square = int(input("\nEnter the value for c (e.g.16. 16 is a square number because it's the answer to (4)^2): "))

        if c_square < 0:
            print("\n\n\nThe entered number is negative.\n\nPlease enter a positive square number:")
        elif is_perfect_square(c_square):
            c = c_square**0.5
            break  # Exit the loop if c_square is a positive perfect square
        else:
            print("\n\n\nThe entered number is not a square number.\n\nA square number is the result when a number has been multiplied by itself, \n\ne.g. 16 is a square number because it's the result of 4 times 4. \n\nPlease try again with a square number:")

    # Apply the difference of squares formula: x^2 - c^2 = (x - c)(x + c)
    factor1 = 1 - c  # Since x is always 1 in this case
    factor2 = 1 + c

    # Print the factors
    explanation = f"\n\n\nStarting factorization process for a difference of squares...\n"
    explanation += f"\nStep 1: Here, 'c' is identified as {c_square}, giving us '√c' = {c}.\n\n"
    explanation += "Step 2: Apply the difference of squares formula x^2 - c = (x - √c)(x + √c).\n\n"
    explanation += f"Step 3: The factors of x^2 - {c_square} are: (x - {c}) and (x + {c})."

    print(explanation)
    # Provide an option to learn more about multiplication
    print("\n\n\nIt is always a good idea to practise checking your answers! \n\n\n\nFor more detailed explanations on difference of squares and other math topics, you can visit an educational websites.")
    learn_more = input("\nWould you like to open the link on this topic? If yes type '0' otherwise type '1'): ").lower()
    if learn_more == '0':
        webbrowser.open("https://thirdspacelearning.com/gcse-maths/algebra/difference-of-two-squares/ ")
        print("\nOpening link now...")
    elif learn_more == '1':
        print("\nContinuing with the program...")
    else:
        print("Invalid input. Please enter '0' for yes or '1' for no.")


def main_menu():
    while True:
        print("\nChoose an option from the topics below:")
        print("1. Multiply a two-digit number by a single-digit number")
        print("2. Solve a quadratic equation")
        print("3. Factorize a difference of squares")
        print("4. Exit")
        
        option = input("Enter your choice (1/2/3/4): ")
        
        if option == '1':
            multiply_and_explain()
        elif option == '2':
            solve_quadratic()
        elif option == '3':
            factorize_difference_of_squares()
        elif option == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please type 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()





