def removeLetter(word1,word2):
    count = 0
    for i in range(0,len(word1)-1,1):
        for j in range(len(word2)-1):
            if(word1[i] == word2[j]):
                word2 = word2[:j] + word2[(j+1):]
                count += 2
    return (len(word1)+len(word2)+2) - count

if __name__ == '__main__':
    # On récupère le nom des personnes à² tester
    nom1 = input(str("Rentrer le nom de la première personne : "))
    nom2 = input(str("Rentrer le nom de la seconde personne  : "))

    # On transforme tout en minuscule
    nom1 = nom1.lower().replace(" ","")
    nom2 = nom2.lower().replace(" ","")

    # Solution 1
    #lettre_diff = [letter for letter in set(nom1) | set(nom2) if letter not in set(nom1) & set(nom2)]
    
    # Solution 2
    #lettre_diff = [lettre for lettre in nom1 if lettre not in nom2]
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    flames = flames[::-1]
    print(flames[removeLetter(nom1,nom2)%len(flames)])