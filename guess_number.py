# Igrica "Ugani skrito število":
# Program na random izbere število in userja vpraša, naj ugane to število.
# User vpiše številko - če je prenizka, mu računalnik pove da je prenizka.
# Če je previsoka, mu pove da je previsoka. In če je prava, mu čestita in program se konča
# (drugače pa teče v neskončni zanki, dokler uporabnik ne odgovori pravilno).

import os
import random

if __name__ == '__main__':
    os.system('clear')

    print("\t**********************************************")
    print("\t*** Guess a number  ***")
    print("\t*** Enter a number ***")
    print("\t*** If you want to exit write 'exit' ***")
    print("\t**********************************************")

    random_value = random.randint(1, 1000)
    while True:
        number = input('Enter a number: ')
        if number == 'exit':
            exit()
        try:
            number = int(number)

            if number < random_value:
                print('number too low')
            if number > random_value:
                print('number too big')
            if number == random_value:
                print('Congrats the number is correct')
                exit()
        except ValueError:
            print('Input valid number')
