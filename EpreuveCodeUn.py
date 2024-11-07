# region Imports

# endregion


# region Variables globales

# endregion


# region Fonctions

# endregion

# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces

# region Programme principale
def LancementProgramme():
    print("Début du programme")
    print()
    print("Menu")
    print("1 - Conversion pouces vers cm")
    print("2 - Conversion cm vers pouces")
    print("X - Sortir")
    print()

    sortir = False
    while sortir != True:
        choix_str = input("Choisissez votre conversion (saisissez 1 ou 2) : ")
        if choix_str.lower() == "x":
            sortir = True
            break
        elif int(choix_str) == 1:
            print("Conversion de pouces vers cm")
            valeur_str = input("Saisissez la valeur à convertir : ")
            resultat = float(valeur_str)*2.54
            print(f"{valeur_str} pouces sont égales à : {round(resultat,2)} cm")
        elif int(choix_str) == 2:
            print("Conversion de cm vers pouces")
            valeur_str = input("Saisissez la valeur à convertir : ")
            resultat = float(valeur_str) *0.394
            print(f"{valeur_str} cm sont égales à : {int(resultat)} pouces")
        else:
            print("ERREUR : Veuillez saisir 1 ou 2 ou X pour sortir.")

    print("Fin du programme")

# endregion