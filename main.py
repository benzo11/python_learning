# Igrica "Ugani skrito število":
# Program na random izbere število in userja vpraša, naj ugane to število.
# User vpiše številko - če je prenizka, mu računalnik pove da je prenizka.
# Če je previsoka, mu pove da je previsoka. In če je prava, mu čestita in program se konča
# (drugače pa teče v neskončni zanki, dokler uporabnik ne odgovori pravilno).

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/number", methods=["POST"])
def check_number():
    number = request.form.get("number")
    random_number = generateRandomNUmber()
    message = ''
    game_status = False

    try:
        # In python if we want to compare something, it has to be in the correct type.
        # User can enter float or some special characters.
        number = int(number)
    except ValueError:
        return render_template("index.html",
                               errorMessage='Please enter a number!')

    if number < random_number:
        message = 'Entered value is too small'
    elif number > random_number:
        message = 'Entered value is too big'
    elif number == random_number:
        message = ''
        game_status = True

    return render_template("index.html",
                           errorMessage=message,
                           game_status=game_status)


def generateRandomNUmber():
    return random.randint(1, 100)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
