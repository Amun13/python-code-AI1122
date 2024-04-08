
from flask import Flask, render_template, request

app = Flask(__name__)

def long_multiplication(num1, num2):
    # The implementation of your long_multiplication function remains the same
    pass

def visualize_multiplication(num1, num2):
    result, multiplication_steps = long_multiplication(num1, num2)
    output = f"The result of {num1} * {num2} is: {result}\n\n"
    output += "Step-by-step method:\n"
    output += f"{'-' * 40}\n"
    output += f"| {'Multiplication':^15} | {'Addition':^23} |\n"
    output += f"{'-' * 40}\n"

    for step in multiplication_steps:
        mul, add = step.split(" -> ")
        mul = mul.split("=")[1].strip()
        add = add.split(" and put ")
        add_first = add[0].split("Add ")[1]
        add_second = add[1].split(" in position ")

        output += f"| {mul:^15} | {add_first + ' ':^15} | {add_second[1]:^15} |\n"
        output += f"{'-' * 40}\n"

    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result_output = visualize_multiplication(num1, num2)
    return render_template('result.html', result=result_output)

if __name__ == '__main__':
    app.run(debug=True)

python3 --version

