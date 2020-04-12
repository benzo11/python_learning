# FizzBuzz: to je klasična naloga, user vpiše številko med 10 in 100.
# Računalnik nato vse te številke izpiše in pri vseh, ki so deljive s 3 napiše Fizz (namesto številke).
# Pri tistih, ki so deljive s 5 izpiše Buzz. Pri tistih, ki so pa hkrati deljive s 3 in 5 pa izpiše FizzBuzz.

from flask import Flask, render_template, request

app = Flask(__name__)
# Can do something with backend in memory? Put some variable in thread, and than read from thread? is that possible?
result_stack = []


@app.route("/")
def index():
    return render_template("fizzbuzz.html")


@app.route("/number", methods=["POST"])
def check_number():
    number = request.form.get("number")
    fizzbuzz = ''

    try:
        # In python if we want to compare something, it has to be in the correct type.
        # User can enter float or some special characters.
        number = int(number)
    except ValueError:
        return render_template("fizzbuzz.html",
                               errorMessage='Pleałse enter a number!',
                               result_stack=result_stack)

    if number < 10 or number > 100:
        return render_template("fizzbuzz.html",
                               errorMessage='Please enter a number between 10 and 100.',
                               result_stack=result_stack)

    if number % 3 == 0:
        fizzbuzz = 'Fizz'
    if number % 5 == 0:
        # Because we already declared fizzbuzz variable, we can append empty or previous value
        # Could add an extra check if both conditions are true but did not find it necessary.
        fizzbuzz = fizzbuzz + 'Buzz'
    if fizzbuzz == '':
        fizzbuzz = number

    result_stack.append(fizzbuzz)

    return render_template("fizzbuzz.html",
                           result_stack=result_stack)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
