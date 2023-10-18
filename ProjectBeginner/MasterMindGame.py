import random as rd

numberToGuess = rd.randint(1000,10000)

game = True
count = 0

print('Guess the 5 digits :')
rep = str(input('> '))

while game:

    if rep == str(numberToGuess):
        print("Great you've become a Mastermind!")
        print(f"It took you only {count} tries!")
        game = False
    
    