import random

def computer_guess(number):
    low = 1
    high = number
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #cloud be high bc low = high
        feedback = input(f'Is {guess} too hight (H), too low (L), or correctly (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number {guess} correctly!')

computer_guess(10)