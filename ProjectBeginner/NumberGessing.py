import random as rd
import math;

lowerBound = int(input('Enter lower bound : '))
upperBound = int(input('Enter upper bound : '))

#if the user make an error
if(lowerBound >= upperBound):
    tmp = lowerBound
    lowerBound = upperBound
    upperBound = tmp

tryActu = 0

randomNumber = rd.randint(lowerBound,upperBound)

print('\tYou have only '+str(math.ceil(math.log(upperBound-lowerBound+1,2)))+' chances to guess the number ! ')

while tryActu < math.log(upperBound-lowerBound+1,2):

    guessedNumber = int(input(f"Guess a number between {lowerBound} and {upperBound} : "))
    while guessedNumber > upperBound or guessedNumber < lowerBound:
        guessedNumber = int(input(f"Retry: Guess a number between {lowerBound} and {upperBound} : "))
    
    tryActu += 1

    if guessedNumber == randomNumber:
        print(f'Congratulation you did it in {tryActu} try')
        break;
    if guessedNumber > randomNumber:
        print("You Guessed too high !")
    else:
        print("You Guessed too small !")

if tryActu > math.log(upperBound-lowerBound+1,2):
    print(f'\nThe number is {randomNumber}')