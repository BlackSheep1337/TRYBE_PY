import random

def guess_number():
    number_at = int(input("Guess a number between: "))
    number_from = int(input("And: "))
    guess = int(input("Digit your guess: "))
    random_number = random.randint(number_at, number_from)
    if (guess == random_number):
        print("You win!!")
    else:
        print("You lose!")
    print(f"The number is {random_number}")

if __name__ == "guess_number":
    guess_number()