# region Imports

# endregion

# region Variables globales
# endregion

# region Fonctions

# Fonction de détermination de la majorité d'un individu par son age
def est_majeur(age):
    if age <= 0:
        return False    
    if age >= 18:
        return True
    return False

# Fonction de récupération des informations d'un ou des individus
def recuperer_infos_personne(numero_personne):
    nom_personne = input(f"Nom de la personne {numero_personne}: ")
    age_personne = input(f"Age de la personne {numero_personne}: ")
    return nom_personne, int(age_personne) 

def recuperer_et_afficher_infos_personnes(numero_personne):
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)

# Fonction d'affichage des résutlats du questionnaire 
def afficher_infos_personne(numero_personne, nom, age):
    print(f"La personne {numero_personne} est {nom} son age est {age} ans")
    print(f"Le nom contient {len(nom)} lettres")
    if est_majeur(age):
        print(f"{nom} est majeur")
    else:
        print(f"{nom} est mineur")
# endregion

# region Programme principale
# Lancement du programme principal
print("Début du programme")

for i in range(1,4):
    recuperer_et_afficher_infos_personnes(i)


print("Fin du programme")
# endregion
