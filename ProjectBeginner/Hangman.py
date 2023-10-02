import random as rd

someWords = 'apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'

someWords = someWords.split(' ')

choice = rd.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    response = ['_' for letter in range(len(choice))]
    print("".join(response) +'\n')

    countLeft = len(choice) + 2
    count = 0

    while countLeft > 0 and "".join(response) != choice:

        try:
            guess = str(input('Enter a letter to guess : '))
        except:
            print("Enter only a LETTER")
        
        if not guess.isalpha():
            print("That was not a LETTER !")
            continue
        elif len(guess) > 1:
            print("Just ONE letter")
            continue
        elif guess in response:
            print("Already guessed this letter")
            continue

        count += 1

        if guess in choice:
            for index,letter in enumerate(choice):
                if letter == guess:
                    response[index] = letter
        else:
            countLeft-=1

        print(" ".join(response))

if countLeft == 0:
    print(f'You loose the word was {choice} ! ')
else:
    print(f'You win in {count} try!')
