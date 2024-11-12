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
    
def cuisson(time_sec, interval):
    print("Début de la cuisson :")
    iteration = int(time_sec / interval)
    temps_ecoule = 0
    for i in range(iteration):
        for y in range(interval):
            print(".", end="", flush=True)
            temps_ecoule += 1
            time.sleep(1)

        temps_restant = time_sec - temps_ecoule
        minute = temps_restant // 60
        secondes = temps_restant - minute * 60
        print(f" Temps restant : {minute:02d}:{secondes:02d} minutes")

    print("Fin de la cuisson :")

def cuisson_horloge(time_sec):
    print("Début de la cuisson :")
    for d in range(time_sec, 0, -1):
        mins, secs = divmod(d, 60)
        print(f"\rTemps restant : {mins:02d}:{secs:02d} minutes", end='', flush=True)
        time.sleep(1)
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
                cuisson(180,10)
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "2":
                #cuisson(360,10)
                cuisson_horloge(360)
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            elif choix == "3":
                cuisson(540,10)
                # demande de sortie du mode de conversion
                if demander_pour_continuer() == False:
                    break
            else:
                print("ERREUR : Veuillez saisir 1,2,3 ou 4 pour sortir.")

    # sortie du programme
    print("Fin du programme")

# endregion
