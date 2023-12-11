import random as rd

numberToGuess = rd.randint(1000,10000)

game = True
count = 0

while game:


    print('Guess the 4 digits :')
    rep = str(input('> '))

    while len(rep) != 4:
        print('Guess the 5 digits :')
        rep = str(input('> '))
    count += 1

    if rep == str(numberToGuess):
        print("Bien jouer vous êtes devenue un MasterMind!")
        print(f"Cela vous fait {count} essais!")
        game = False
    else:
        message = "Nombre corespondant :"
        for i in range(0,len(str(numberToGuess)),1):
            if rep[i] == str(numberToGuess)[i]:
                message += " "+rep[i]
            else:
                message += " X"
        print(message)