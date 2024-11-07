# region Imports
import time
# endregion


# region Variables globales

# endregion


# region Fonctions
# Fonction d'affichge du menu du programme, retourne le choix de l'utilisateur
def afficher_menu():
    print("**********************************************")
    print("*        Programme de cuisson                *")
    print("**********************************************")
    print("*     1 - Oeufs à la coque : 3 minutes       *")
    print("*     2 - Oeufs mollets : 6 minutes          *")
    print("*     3 - Oeufs durs : 9 minutes             *")
    print("*     4 - Quitter                            *")
    print("********************************************\n")
    return input("Choisissez votre cuisson : ")

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
    
def cuir_oeuf_coque():
    print("Début de la cuisson :")
    duree_totale = 3 * 60
    intervalle_particulier = 10
    for i in range(duree_totale):
        if i % intervalle_particulier == 0:
            temps_ecoule = duree_totale - i
            minute = temps_ecoule // 60
            secondes = temps_ecoule-minute*60
            print(f"Temps restant : {minute}:{secondes:02d}")
        else:
            print(".", end="", flush=True)
        time.sleep(1)

    print("Fin de la cuisson :")

def cuir_oeuf_mollet():
    print("Début de la cuisson :")
    for i in range(180):
        for y in range(10):
            time.sleep(1)
            i -= 1
            print(".", end="", flush=True)
        d = i
        min = d//60
        sec = d-min*60
        print(f"Temps restant : {min}:{sec}")
    print("Fin de la cuisson :")
    
def cuir_oeuf_dur():
    print("Début de la cuisson :")
    for i in range(180):
        for y in range(10):
            time.sleep(1)
            i -= 1
            print(".", end="", flush=True)
        d = i
        min = d//60
        sec = d-min*60
        print(f"Temps restant : {min}:{sec}")
    print("Fin de la cuisson :")


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
                cuir_oeuf_coque()
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "2":
                cuir_oeuf_mollet()
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "3":
                cuir_oeuf_dur()
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            else:
                print("ERREUR : Veuillez saisir 1,2,3 ou 4 pour sortir.")

    # sortie du programme
    print("Fin du programme")

# endregion