# region Imports
import os
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


# endregion

# region Programme principale
# Lancement du programme principal
def LancementProgramme():
    3**2
    # sortie du programme
    print("Fin du programme")
    exit()
    
# endregion
