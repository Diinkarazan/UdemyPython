# region Imports
import EpreuveCodeUn
import EpreuveCodeDeux
import EpreuveCodeTrois
import EpreuveCodeQuatre
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
    print("*     4 - Epreuve de code quatre             *")
    print("*     5 - Quitter                            *")
    print("********************************************\n")
    return input("Choisissez votre exercice : ")

# endregion

# region Programme principale
# boucle du menu
while True:
    choix = afficher_menu()
    if choix == "5":
        break

    # boucle de conversion selon le mode choisi
    while True:
        if choix == "1":
            EpreuveCodeUn.LancementProgramme()
            # demande de sortie du mode de conversion
        elif choix == "2":
            EpreuveCodeDeux.LancementProgramme()
            # demande de sortie du mode de conversion
        elif choix == "3":
            EpreuveCodeTrois.LancementProgramme()
            # demande de sortie du mode de conversion
        elif choix == "4":
            EpreuveCodeQuatre.LancementProgramme()
            # demande de sortie du mode de conversion
        else:
            print("ERREUR : Veuillez saisir 1,2,3... ou 5 pour sortir.")

# sortie du programme
print("Fin du programme")

# endregion