import random as rd

name = str(input('What is your name challenger : '))
print(f'Good luck {name} !')

word = ['elephant','table', 'cable', 'gentilesse', 'soleil', 'jeu', 'arme', 'deception', 'fort']

wordTaken = rd.choice(word)
response = "_" * len(wordTaken)

turns = 10
count = 0

print('Guess the characters (max 10 turns)')

while response != wordTaken:

    count += 1

    if count > turns:
        print(f'You loose !!!\n The word was {wordTaken}')
        break

    inputUser = str(input('Guess a characters : ')).lower()

    while len(inputUser) != 1 or inputUser not in 'abcdefghijklmnopqrstuvwxyz' or inputUser in response:
        inputUser = str(input('Guess a characters : ')).lower()

    if inputUser in wordTaken:
        for number in range(0,len(wordTaken),1):
            if wordTaken[number] == inputUser:
                response = response[:number] + inputUser + response[(number+1):]
    
    print(response)

if count < turns:
    print(f'Congratulation you win in {count} turns !')
