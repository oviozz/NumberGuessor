import random

limit_counter = 20


def intro():
    print('Welcome to Number Guessing Game!'+'\n')


def checking():
    random_number = random.randint(1, limit_counter)
    print(random_number)

    print('---------------------------------------------------------------------')
    print(f'I am thinking of a number between 1 and {limit_counter}!' + '\n')
    print('Guess a number')
    end = 0
    guess = 12


    while end != 1:

        if guess == 1:
            a = input('Do you want to play again: Y/N: '+ '\n').lower()
            if a == 'y' or a == 'yes':
                checking()
            else:
                ending()



        if guess == 0:
            end = 1

        try:
            number = int(input(f'Your Guess [{guess-2}]: '))
            guess -= 1

            if number == random_number:
                print('***********************************************************')
                print('Holy Cow! How lucky can you be!')
                print('***********************************************************')
                ending()

            elif (random_number - 5 < number < random_number + 5):
                print('You are too close. Try again!' + '\n')
                continue

            elif (random_number - 50 < number < random_number + 50):
                print("You are kind of near. Don't give up!" + '\n')
                continue

            elif number > random_number:
                print('- You guess too high!' + '\n')

            elif number < random_number:
                print('- You guess too low!' + '\n')



        except ValueError:
            print('Please enter a number only!' + '\n')
            continue

    exit(endnum=random_number)

def exit(endnum):
    print(f' The correct number was: {endnum}')
    print('Hope you had fun!')


def ending():
    print('Thanks for playing. Hope you had fun!')
    quit()



intro()
checking()
