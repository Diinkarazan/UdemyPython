# region Imports
import os
# endregion

# region Variables globales
QUESTIONS = (
    {
        "numero" : 1,
        "question" : "Quelle est la capitale de la France ?",
        "choix" : ("(a) Marseille", "(b) Lyon", "(c) Bordeaux", "(d) Paris"),
        "reponse" : ("d", "Paris"),
        "pays" : "France"
    },
    {
        "numero" : 2,
        "question" : "Quelle est la capitale de l'Angleterre ?",
        "choix" : ("(a) Londres", "(b) Manchester", "(c) Liverpool", "(d) Bristol"),
        "reponse" : ("a", "Londres"),
        "pays" :"Angleterre"
    },
    {
        "numero" : 3,
        "question" : "Quelle est la capitale des USA ?",
        "choix" : ("(a) New york", "(b) Los Angeles", "(c) Whashington", "(d) Détroit"),
        "reponse" : ("c", "Whashington"),
        "pays" :"USA"
    },
    {
        "numero" : 4,
        "question" : "Quelle est la capitale du Japon ?",
        "choix" : ("(a) Osaka", "(b) Kyoto", "(c) Tokyo", "(d) Hiroshima"),
        "reponse" : ("c", "Tokyo"),
        "pays" :"Japon"
    }
)
# endregion

# region Fonctions
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def poser_question():
    for q in QUESTIONS:
        print(f" Question n°{q['numero']} : {q['question']}")
        for c in q['choix']:
            print(f"    {c}")
        print("")
        reponse = input("Votre réponse : ")
        verif = q['reponse']
        if reponse == verif[0]:
            print("Bravo vous avez trouvé !")
        else:
            print("Mauvaise réponse : ")
            print(f"Pays : {q['pays']}")
            print(f"La bonne réponse était : ({verif[0]}) {verif[1]}")
        print("")

# endregion

# region Programme principale
# Lancement du programme principal
clear_screen()
print("Début du programme - Questionnaire")
print("")
poser_question()
print("")
print("Fin du programme")
# endregion
