import random

random_number = random.randint(1, 10)

guess = ''

while guess is not random_number:
    guess = int(input('Qual seu palpite? '))
print('O numero sorteado era: ', guess)