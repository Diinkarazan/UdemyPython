# region Imports
import os
# endregion

# region Variables globales
# endregion

# region Fonctions
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def afficher_table_multiplication(numero_table, min=1, max=10):
    for i in range(min,max+1):
        if i > 9:
            print(f" {numero_table} X {i} = {i*numero_table}")
        else:
            print(f" {numero_table} X  {i} = {i*numero_table}")


def choisir_table():
    table = int(input("Choisissez votre table de multiplication : "))
    if table <1 or table > 10:
        print("ERREUR : La valeur saisie doit être comprise en 1 et 10.") 
        return

    val_min_max_oui = input("Voulez-vous définnir des valeurs MIN et MAX : O/N ")

    if val_min_max_oui == "O" or val_min_max_oui == "o":
        min = int(input("MIN : "))
        max = int(input("MAX : "))
        
        if min > max:
            print("ERREUR : la valeur MIN ne peut être supérieur à la valeur MAX.")
            return           

    else:
        min = 1
        max = 10

    return table, min, max



# endregion

# region Programme principale
# Lancement du programme principal
clear_screen()
print("Début du programme")
print("")
table, min, max = choisir_table()
afficher_table_multiplication(table, min, max)
print("")
print("Fin du programme")
# endregion
