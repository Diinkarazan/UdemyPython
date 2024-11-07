# region Imports

# endregion


# region Variables globales
# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces
POUCE_POUR_CM = 2.54
CM_POUR_POUCE = 0.394
# endregion


# region Fonctions
# Fonction d'affichge du menu du programme, retourne le choix de l'utilisateur
def afficher_menu():
    print("*****************************************")
    print("*        Programme de conversion        *")
    print("*****************************************")
    print("*     1 - Convertion pouces -> cm       *")
    print("*     2 - Convertion cm -> pouces       *")
    print("*     3 - Quitter                       *")
    print("*****************************************\n")
    return input("Choisissez une conversion : ")


# Fonction de demande de saisie de la valeur à convertir et de convertion
def demander_convertir_valeur(unite_un, unite_deux, valeur_de_conversion):
    valeur = input(f"Saisissez la valeur à convertir :")
    try:
        valeur_float = float(valeur)
    except:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        print("(Utilisez le point et non la virgule pour les décimales)")
    # Affichge de la valeur de conversion
    valeur_convertie = round(valeur_float * valeur_de_conversion, 2)
    print(f"Résultat de la conversion : {valeur_float} {unite_un} = {valeur_convertie} {unite_deux}\n")


# Fonction de saisie de réponse utilisateur pour continuer dans la séquence de conversion choisi ou de revenir au menu
def demander_pour_continuer():
    r = str(input("Voulez-vous continuer : o/n ?").lower())
    if r == "o":
        return True
    elif r == "n":
        return False
    else:
        print("Je n'ai pas compris votre saisie")
        return demander_pour_continuer()
# endregion


"""
Programme principale de l'application
Ce programme à pour but de convertir des valeur de pouce en cm ou inversement 
Le programme demandera un choix utilisateur sur le mode de converion et lancera un module de conversion à la chaine
L'utilisateur pourra interrrompre cette sépquence et revenir au menu principal
Le menu permmtra de mettre fin au programme sur un choix utilisateur
"""
# region Programme principale
def LancementProgramme():
    # boucle du menu
    while True:
        choix = afficher_menu()
        if choix == "3":
            break

        # boucle de conversion selon le mode choisi
        while True:
            if choix == "1":
                demander_convertir_valeur("pouces", "cm", POUCE_POUR_CM)
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "2":
                demander_convertir_valeur("cm", "pouces", CM_POUR_POUCE)
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            else:
                print("ERREUR : Veuillez saisir 1 ou 2 ou 3 pour sortir.")

    # sortie du programme
    print("Fin du programme")

# endregion