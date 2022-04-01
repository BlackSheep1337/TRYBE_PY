import random

def guess(number):
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {number}: '))
        if guess < random_number:
            print('Oops guess again, too low')
        elif guess > random_number:
            print('Oops guess again, too high')
    print(f'Yay you win the number is {random_number}')

if __name__ == "__main__":
    number = int(input('Guess a number between 1 and: '))
    guess(number)