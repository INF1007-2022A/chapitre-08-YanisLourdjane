#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
with open("text.txt", "w" ,encoding='utf-8') as f2:
    f2.write("""INVENTAIRE DU ZOO
Il y a 217 espèces animales au zoo, dont 68 espèces de lézards et 84 espèces de mammifères.
""")


# TODO: Définissez vos fonction ici
def exercice1(filepath1,filepath2):
    with open(filepath1, "r", encoding='utf-8') as f1, open(filepath2, "r", encoding='utf-8') as f2:
        for ligne1 in f1:
            ligne2=f2.readline()
            if ligne1!= ligne2:
                print("Il y a un probleme!!!!!!!!!")

def exercice2(filepath1,filepath2):
    with open(filepath1, "r", encoding='utf-8') as f1, open(filepath2, "w", encoding='utf-8') as f2:
        for ligne in f1:
            f2.write(ligne.replace(" ", "   "))


def exercice3(note_path, result_file_path):
    with open(note_path, "r", encoding='utf-8') as f1, open(result_file_path, "w", encoding='utf-8') as f2:
        #Cette methode permet de manipuler directement les lignes du fichier note_path
        for ligne in f1:
            #ligne.replace(" ", "")
            #ligne.strip()
            for key,value in PERCENTAGE_TO_LETTER.items():
                if value[0]<= int(ligne) < value[1]:
                    f2.write(f"{ligne} « {key} »")
                    print(f"{ligne} « {key} »")

        #Cette methode permet plutot de stocker chaque ligne du fichier noth_path dans une liste
        lignes=f1.readlines()
        for ligne in lignes:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0]<= int(ligne) < value[1]:
                    f2.write(f" {ligne} « {key} »")

def exercice4(recipes_path):
    pass

def exercice5(file_path):
    liste=[]
    with open(file_path, "r", encoding='utf-8') as f1:
        texte=f1.read().split()
        for mot in texte:
            if mot.isnumeric():
                liste.append(mot)

    return  sorted(liste)


def exercice6(file_path1, file_path2):
    with open(file_path1, "r", encoding='utf-8') as f1, open(file_path2, "w", encoding='utf-8') as f2:
        lignes=f1.readlines()
        for index, value in enumerate(lignes):
            if index%2==0:
                f2.write(lignes[index])

















if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice1("exemple.txt","text.txt")
    exercice2("exemple.txt", "exemple_copy.txt")
    exercice3("notes.txt", "notes_letter.txt")
    exercice4("recettes.p")
    print(exercice5("exemple.txt"))
    exercice6("notes.txt", "notes_skip.txt")
    pass
