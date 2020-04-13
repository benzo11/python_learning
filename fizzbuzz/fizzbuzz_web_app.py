# Računalnik nato vse te številke izpiše in pri vseh, ki so deljive s 3 napiše Fizz (namesto številke).
# Pri tistih, ki so deljive s 5 izpiše Buzz. Pri tistih, ki so pa hkrati deljive s 3 in 5 pa izpiše FizzBuzz.

from flask import Flask, render_template, request
from fizzbuzz import check_number

app = Flask(__name__)
# Can do something with backend in memory? Put some variable in thread, and than read from thread? is that possible?
result_stack = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/number", methods=["POST"])
def process_number():
    number_input = request.form.get("number")
    try:
        number_input = int(number_input)
        if number_input < 10 or number_input > 100:
            raise ValueError
        strings = []
        for i in range(1, number_input + 1):
            strings.append(check_number(i))

        return render_template("index.html",
                               result_stack=strings)

    except ValueError:
        return render_template("index.html",
                               errorMessage='Number have to be between 10 and 100')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
