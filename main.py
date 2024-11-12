# region Imports
import EpreuveCodeUn
import EpreuveCodeDeux
import EpreuveCodeUn_Modifie

from EpreuveCodeUn_Modifie import *
# endregion


# region Variables globales

# endregion


# region Fonctions
def afficher_menu():
    print("**********************************************")
    print("*        Programme de cuisson                *")
    print("**********************************************")
    print("*     1 - Epreuve de code un                 *")
    print("*     2 - Epreuve de code deux               *")
    print("*     3 - Epreuve de code trois              *")
    print("*     4 - Quitter                            *")
    print("********************************************\n")
    return input("Choisissez votre exercice : ")

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
# boucle du menu
while True:
    choix = afficher_menu()
    if choix == "4":
        break

    # boucle de conversion selon le mode choisi
    while True:
        if choix == "1":
            EpreuveCodeUn.LancementProgramme()
            # demande de sortie du mode de conversion
            if demander_pour_continuer() == False:
                break
        elif choix == "2":
            EpreuveCodeDeux.LancementProgramme()
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

# endregion