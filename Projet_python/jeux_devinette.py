import random 
bot = random.randint(0,10)
nb_vie = 3
joueur = int(input("choisi un nombre entre 0 et 10 : "))
while nb_vie != 0 :
    print("nombre de vie : ",nb_vie)
    if joueur > bot : 
        print("tu es trop grand ")
        nb_vie -= 1
        joueur = int(input("choisi un nombre entre 0 et 10 : "))
    elif joueur < bot : 
        print("tu es trop petit")
        nb_vie -= 1
        joueur = int(input("choisi un nombre entre 0 et 10 : "))
    elif joueur == bot : 
        print("Félication tu as réussie")
        break
if nb_vie == 0 : 
    print("tu as perdue !!")