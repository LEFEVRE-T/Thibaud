# PARTIE IMPORTS

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import random
import collections


# PARTIE CODE

d = {'X' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'Y' : [1, 2, 3, 4],
    'Z' : ['A', 'B', 'C', 'D']}
df = pd.DataFrame(d)

def choix_donnees(): # Fonction pour l'import des données

  import_ = input("Entrez le chemin du fichier à importer : ")
  print("Import non réussi donc la suite sera faite avec un data frame déjà créé.")
 
  return (import_)


def while_liste(txt, liste, type = str): #Fonction qui permet de ne pas avoir à écrire le while à chaque fois

  variable = type(input(txt))
  while variable not in liste:
    variable = type(input(txt))

  return(variable)


def compter(data): # Fonction qui compte les éléments
  
  compteur = collections.Counter(data)
  print(compteur)


def indicateurs(colonne, type_donnees): # Fonction qui calcule des indicateurs

  if type_donnees == "quanti":
    mini = min(colonne)
    maxi = max(colonne)
    mean = st.mean(colonne)
    median = st.median(colonne)
    sd = st.stdev(colonne)
    var = st.variance(colonne)  
    print(pd.DataFrame([mini, maxi, mean, median, sd, var], index = ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var']))
  else:
    compter(colonne)
    

def realisation(data, choix): # Fonction qui agit en fonction du choix de l'utilisateur

  if choix == 1:
    print(df)
  elif choix == 2:
    colonne = while_liste('Nom de colonne sur lequel faire : ', ['X', 'Y', 'Z'])
    type_donnees = while_liste('Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'])
    indicateurs(df[colonne], type_donnees)
  else:
    print("r")


def choix(): # Fonction qui fait choisir à l'utilisateur l'action à réaliser

  while True:
    print('\n 1 : Afficher données \n 2 : Calculer indicateurs \n 3 : Autres \n Entrez le numéro du choix \n "exit" pour sortir')
    action = while_liste('Que voulez-vous faire : ', ["1", "2", "3", "exit"])
    if action == "exit":
      break
    action = int(action)
    realisation(df, action)


# PARTIE UTILISATEUR

if __name__ == "__main__":
  donnees = choix_donnees()
  choix()

"""
mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
print(contenu)
"""