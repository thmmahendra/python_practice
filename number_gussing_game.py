# Generate Random Number
import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess the number from 1 to 100: '))

        if guess < number_to_guess:
            print('Too Low')

        elif guess > number_to_guess:
            print('Too high')

        else:
            print('Contratulation! You guess the correct number')
            break
    except ValueError:
        print('Please enter a valid number')
