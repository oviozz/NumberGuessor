import random

# Max limit range
limit_counter = 20

#intro
def intro():
    print('Welcome to Number Guessing Game!')


def checking():
    # random number from 1 - max_limit_counter
    random_number = random.randint(1, limit_counter)

    print('---------------------------------------------------------------------')
    print(f'I am thinking of a number between 1 and {limit_counter}!' + '\n')
    print('Guess a number')

    end = 0
    guess = 12

    #checks if end != 1 if it does the game ends
    while end != 1:

        # when the number of guesses remains to 1 prompt a input whether you want to play the game or not?
        if guess == 1:
            a = input('Do you want to play again: Y/N: '+ '\n').lower()
            if a == 'y' or a == 'yes':
                checking()
            else:
                ending()


        # if number of guess goes to 0 end the game cause end = 1
        if guess == 0:
            end = 1

        # the try method checks if the user is inputing correct value it not it will raise a ValueError
        try:
            number = int(input(f'Your Guess [{guess-2}]: '))
            guess -= 1

            if number == random_number:
                print('***********************************************************')
                print('Holy Cow! How lucky can you be!')
                print('***********************************************************')
                ending()

            # if the chosen number is near - 5 or + 5 print this option
            elif (random_number - 5 < number < random_number + 5):
                print('You are too close. Try again!' + '\n')
                continue

            # if the chosen number is near - 50 or + 50 print this option
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
    #print this after the loops runs / ending
    exit(endnum=random_number)

def exit(endnum):
    print(f' The correct number was: {endnum}')
    print('Hope you had fun!')
    quit()


def ending():
    print('Thanks for playing. Hope you had fun!')
    quit()



intro()
checking()

