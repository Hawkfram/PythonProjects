import random
import re

def choix():
    print("\n==============Rock Paper Scissor===============\n")
    print("\t * 1: Deux bots ");
    print("\t * 2: Un joueurs et un bot ");
    print("\t * 3: Deux joueurs ");
    print("\n===============================================\n")

    return input(str("Quelle mode de jeu choissisez vous : \n>"))
   

def regle():
    print("\n=================Règles du jeu=================\n")
    print("\t * Le ciseau gagne sur la feuille")
    print("\t * La pierre gagne sur le ciseau")
    print("\t * La feuille gagne sur la pierre")
    print("\n===============================================\n")


if __name__ == '__main__':
    choixMode = choix()
    regle()
    while True:

        reponse = input(str("Que choissisez vous (pierre/cisseau/feuille) :\n>"))