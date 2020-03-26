# PARTIE IMPORTS

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
import collections


# PARTIE CODE

def while_liste(txt, liste, type = str, get_user_input = input): #Fonction qui permet de ne pas avoir à écrire le while à chaque fois
    variable = type(get_user_input(txt))
    while variable not in liste:
          variable = type(get_user_input(txt))
    return(variable)


def compter(donnees): # Fonction qui compte les éléments
    compteur = collections.Counter(donnees)
    return(compteur)


def indicateurs(colonne): # Fonction qui calcule des indicateurs
    mini = min(colonne)
    maxi = max(colonne)
    mean = st.mean(colonne)
    median = st.median(colonne)
    sd = st.stdev(colonne)
    var = st.variance(colonne)  
    return(pd.DataFrame([mini, maxi, mean, median, sd, var], index = ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var']))



def etude(colonne): # Fonction qui choisi l'étude en fonction du type de variable
    if colonne.dtypes == "int64":
      print(indicateurs(colonne))
    else:
      print(compter(colonne))
    

def scatter(data, x, y):
    plt.scatter(data[x], data[y])
    plt.title(x + str(" en fonction de ") + y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(str("Nuage_de_points de ") + x + str(" en fonction de ") + y)
    print('\n Graphique enregistré sous le nom : ' + str("Nuage_de_points de ") + x + str(" en fonction de ") + y)


def barplot(data, x):
    data[x].value_counts(normalize = True).plot(kind = 'bar')
    plt.title(str("Répartition de la variable ") + x)
    plt.xlabel(x)
    plt.ylabel("Fréquence")
    plt.savefig(str("Diagramme en barres de la variable ") + x)
    print('\n Graphique enregistré sous le nom : ' + str("Diagramme en barres de la variable ") + x)


def piechart(data, x):
    data[x].value_counts(normalize = True).plot(kind = 'pie')
    plt.axis('equal') 
    plt.title(str("Répartition de la variable ") + x)
    plt.savefig(str("Diagramme circulaire de la variable ") + x)
    print('\n Graphique enregistré sous le nom : ' + str("Diagramme circulaire de la variable ") + x)


def hist(data, x):
    data[data[x].abs() < 100][x].hist(density = True, bins=20)
    plt.title(str("Répartition de la variable ") + x)
    plt.xlabel(x)
    plt.ylabel("Fréquence")
    plt.savefig(str("Histogramme de la variable ") + x)
    print('\n Graphique enregistré sous le nom : ' + str("Histogramme de la variable ") + x)


def add_col(data, colonne1, colonne2, new_col, choix):
    if choix == 1 and colonne1.dtypes == "int64" and colonne2.dtypes == "int64":
      data[new_col] = colonne1 + colonne2
    elif choix == 2 and colonne1.dtypes == "int64" and colonne2.dtypes == "int64":
      data[new_col] = colonne1 - colonne2
    elif choix == 3 and colonne1.dtypes == "int64" and colonne2.dtypes == "int64":
      data[new_col] = colonne1 * colonne2
    elif choix == 4 and colonne1.dtypes == "int64" and colonne2.dtypes == "int64":
      data[new_col] = colonne1 / colonne2
    elif choix == 5:
      data[new_col] = colonne1.map(str) + colonne2.map(str)
    else:
      print("\n Choix uniquement possible avec deux variables quantitatives.")
    return data


def realisation(data, choix): # Fonction qui agit en fonction du choix de l'utilisateur
    if choix == "1":
      print(data)
    elif choix == "2":
      colonne = while_liste('\n Nom de colonne sur lequel faire : ', data.columns)
      etude(data[colonne])
    elif choix == "3":
      axe_x = while_liste("\n Nom de colonne pour l'axe x : ", data.columns)
      axe_y = while_liste("Nom de colonne pour l'axe y : ", data.columns)
      scatter(data, axe_x, axe_y)
    elif choix == "4":
      axe_x = while_liste("\n Nom de colonne pour l'axe x : ", data.columns)
      barplot(data, axe_x)
    elif choix == "5":
      variable = while_liste("\n Nom de colonne pour la variable : ", data.columns)
      piechart(data, variable)
    elif choix == "6":
      variable = while_liste("\n Nom de colonne pour la variable : ", data.columns)
      hist(data, variable)
    elif choix == "7":
      print('\n 1 : Somme de colonnes \n 2 : Soustraction de colonnes \n 3 : Multiplication de colonnes \n 4 : Division de colonnes \n 5 : Concaténation de colonnes \n Entrez le numéro du choix')
      action = while_liste('\n Que voulez-vous faire : ', range(1, 6), int)
      new_col = input("Nom de la nouvelle colonne : ")
      colonne1 = while_liste("\n Nom de la première colonne : ", data.columns)
      colonne2 = while_liste("\n Nom de la deuxième colonne : ", data.columns)
      print(add_col(data, data[colonne1], data[colonne2], new_col, action))
    elif choix == "8":
      nom_fichier = input("Nom du fichier : ")
      separateur_fichier = input("Séparateur : ")
      data.to_csv(nom_fichier, sep = separateur_fichier)
      print("Export fait.")


class fake_input:
    def __init__(self, saisies):
        self._iter = iter(saisies)

    def __call__(self, *args):
        print(args)
        return next(self._iter)


# PARTIE UTILISATEUR

if __name__ == "__main__":
  donnees = input("Entrez le nom du fichier à importer : ")
  separateur = input("Séparateur : ")
  fichier = pd.read_csv(donnees, sep = separateur)
  while True:
    print('\n 1 : Afficher données \n 2 : Étude descriptive \n 3 : Nuage de points \n 4 : Diagramme en barres \n 5 : Diagramme circulaire \n 6 : Histogramme \n 7 : Ajouter colonne \n 8 : Exporter données \n Entrez le numéro du choix ou "exit" pour sortir')
    action = while_liste('\n Que voulez-vous faire : ', ["1", "2", "3", "4", "5", "6", "7", "8", "exit"])
    if action == "exit":
      break
    realisation(fichier, action)
