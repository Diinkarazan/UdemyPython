# region Imports



# endregion


# region Variables globales

# endregion


# region Fonctions
# Fonction d'affichge du menu du programme, retourne le choix de l'utilisateur
def afficher_menu():
    print("**********************************************")
    print("*        Programme de ...                *")
    print("**********************************************")
    print("*     1 - xxx                                *")
    print("*     2 - xxx                                *")
    print("*     3 - xxx                                *")
    print("*     4 - Quitter                            *")
    print("********************************************\n")
    return input("Choisissez votre .... : ")


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

# region Programme principale
def LancementProgramme():
    # boucle du menu
    while True:
        choix = afficher_menu()
        if choix == "4":
            break

        # boucle de conversion selon le mode choisi
        while True:
            if choix == "1":

                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "2":

                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "3":

                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            else:
                print("ERREUR : Veuillez saisir 1,2,3 ou 4 pour sortir.")

    # sortie du programme
    print("Fin du programme")
    exit()

# endregion
