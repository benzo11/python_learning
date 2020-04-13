# FizzBuzz: to je klasična naloga, user vpiše številko med 10 in 100.
# Računalnik nato vse te številke izpiše in pri vseh, ki so deljive s 3 napiše Fizz (namesto številke).
# Pri tistih, ki so deljive s 5 izpiše Buzz. Pri tistih, ki so pa hkrati deljive s 3 in 5 pa izpiše FizzBuzz.

import os


def check_number(number):
    fizz_buzz = ''

    if number % 3 == 0:
        fizz_buzz = 'Fizz'
    if number % 5 == 0:
        fizz_buzz = fizz_buzz + 'Buzz'
    if fizz_buzz == '':
        fizz_buzz = number

    return fizz_buzz


if __name__ == '__main__':
    os.system('clear')

    print("\t**********************************************")
    print("\t*** Fizzbuzz  ***")
    print("\t*** Enter a number ***")
    print("\t*** Write 'exit' to exit the program ***")
    print("\t**********************************************")

    while True:
        number_input = input('Enter a number: ')

        try:
            if number_input == 'exit':
                break

            number_input = int(number_input)
            if number_input < 10 or number_input > 100:
                raise ValueError
            print("\t*** Result  ***")

            for i in range(1, number_input + 1):
                print('\t', check_number(i))
            print("**********************************************")
        except ValueError:
            print('Re-enter a number between 10 and 100')
