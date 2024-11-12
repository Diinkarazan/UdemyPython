# region Imports
import os
import random
import time
# endregion


# region Variables globales
# endregion


# region Fonctions
# Fonction d'éffacement du terminal console
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Fonction de génération d'un chiffre aléatoire avec x nombres
def ajout_nombre_aleatoire(seq, ite):
    for i in range(ite):
        seq += str(random.randint(0,9))
    return seq
# endregion

# region Programme principale
# Lancement du programme principal
def LancementProgramme():
    sequence = ""
    sequence = ajout_nombre_aleatoire(sequence, 3)
    score = 0

    # Boucle itérative des séquences de nombres
    while True:
        print("Retenez la séquence")
        time.sleep(1)
        sequence = ajout_nombre_aleatoire(sequence, 1)
        print(sequence)
        time.sleep(3)
        clear_screen()
        reponse = input("Votre réponse : ")
        if(reponse == sequence):
            score += 1
            print("Bonne réponse")
            print(f"Votre score est : {score}")
            time.sleep(1)
            clear_screen()
        else :
            print(f"Mauvaise réponse, la séquence était {sequence}")
            print(f"Votre score final : {score}")
            break
    # sortie du programme
    print("Fin du programme")
    exit()
# endregion
