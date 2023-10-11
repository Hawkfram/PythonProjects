import random as rd

game = True;

def perdue():
    print("Vous avez perdue !")
    exit(0)

def perdue2():
    print("Le joueur 2 à perdue !")
    exit(0)

def valide(liste):
    for i in range(0,len(liste)-1,1):
        if liste[i]+1 != liste[i+1]:
            return False
    return True

def gameStart(adv):
    adv = adv.capitalize()
    xyz = []
    lastNumber = 0
    while True:
        print("Joueur 1 : Choissiser l'ordre de passage (1/2)")
        etr = int(input("> "))

        if etr == 1:
            while True:
                if lastNumber == 20:
                    perdue()
                
                print("Votre tour Joueur 1")
                print("Combien de nombre voulez vous rentrer (max 3):")
                rep = int(input("> "))

                # 3 max car on ne peut donner que 4 nombre par tour
                if rep <= 0 or rep > 3:
                    print("Choix trop grand")
                    perdue()

                print("Rentrer les valeurs :")

                for it in range(rep):
                    nb = int(input("> "))
                    xyz.append(nb)

                lastNumber = xyz[-1]

                if valide(xyz):
                    
                    print('Ordre des nombres apèrs le 1er joueur !')
                    print(xyz)
                    
                    if lastNumber >= 21:
                        perdue()
                    else:
                        
                        #Si le joueur 2 est un ordi
                        if lastNumber == 20:
                                perdue2()
                        
                        print("Votre tour Joueur 2")
                        
                        if adv == "Oui":
                            for it2 in range(1,int(rd.randint(2,4))):
                                xyz.append(lastNumber + it2)
                        else:
                            #Si c'est un joueur
                            print("Combien de nombre voulez vous rentrer (max 3):")
                            rep = int(input("> "))

                            if rep <= 0 or rep > 3:
                                print("Choix trop grand")
                                perdue2()

                            print("Rentrer les valeurs :")

                            for it in range(rep):
                                nb = int(input("> "))
                                xyz.append(nb)

                        print('Ordre des nombres apèrs le 2eme joueur !')
                        print(xyz)

                        if not(valide(xyz)):
                            print("Les nombres se suivent pas !")
                            perdue2()

                        lastNumber = xyz[-1]

                        if lastNumber >= 21:
                            perdue2()
                else:
                    print("Les nombres se suivent pas !")
                    perdue()

        elif etr == 2:
            while True:
                if lastNumber == 20:
                    perdue2()
        
                print("Votre tour Joueur 2")

                if adv == "Oui":
                    for it2 in range(1,int(rd.randint(2,4))):
                        xyz.append(lastNumber + it2)
                else:
                    print("Combien de nombre voulez vous rentrer (max 3):")
                    rep = int(input("> "))

                    # 3 max car on ne peut donner que 4 nombre par tour
                    if rep <= 0 or rep > 3:
                        print("Choix trop grand")
                        perdue()

                    print("Rentrer les valeurs :")

                    for it in range(rep):
                        nb = int(input("> "))
                        xyz.append(nb)

                lastNumber = xyz[-1]

                if valide(xyz):
                    
                    print('Ordre des nombres apèrs le 2eme joueur !')
                    print(xyz)
                    
                    if lastNumber >= 21:
                        perdue2()
                    else:
                        
                        if lastNumber == 20:
                                perdue()

                        print("Votre tour Joueur 1")
                        print("Combien de nombre voulez vous rentrer (max 3):")
                        rep = int(input("> "))

                        if rep <= 0 and rep > 3:
                            print("Choix trop grand")
                            perdue()

                        print("Rentrer les valeurs :")

                        for it in range(rep):
                            nb = int(input("> "))
                            xyz.append(nb)

                        print('Ordre des nombres apèrs le 1er joueur !')
                        print(xyz)

                        if not(valide(xyz)):
                            print("Les nombres se suivent pas !")
                            perdue()

                        lastNumber = xyz[-1]

                        if lastNumber >= 21:
                            perdue()
                else:
                    print("Les nombres se suivent pas !")
                    perdue()
        else:
            print("Choix non valide !")

while game:
    print("Voulez vous commencer la partie (Oui/Non) ? ")
    etr = input("> ")

    if etr == 'Oui':

        print("Voulez vous que le joueur 2 soit un ordinateur (Oui)")
        rep = input("> ")

        gameStart(rep)
    else:
        print("Voulez vous quitter (Oui/Non) ? ")
        etr = input("> ")
        if etr == "Oui":
            print("Vous quitte le jeu")
            exit(0)
        elif etr == "Non":
            print("Continue")
        else:
            print("Choix non valide !")