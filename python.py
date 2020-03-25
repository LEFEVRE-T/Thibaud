# PARTIE IMPORTS

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import random
import collections


# PARTIE CODE

def while_liste(txt, liste, type = str): #Fonction qui permet de ne pas avoir à écrire le while à chaque fois

  variable = type(input(txt))
  while variable not in liste:
    variable = type(input(txt))

  return(variable)


def compter(donnees): # Fonction qui compte les éléments
  
  compteur = collections.Counter(donnees)
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
    print(data)
  elif choix == 2:
    colonne = while_liste('Nom de colonne sur lequel faire : ', fichier.columns)
    type_donnees = while_liste('Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'])
    indicateurs(data[colonne], type_donnees)
  else:
    print("r")


# PARTIE UTILISATEUR

if __name__ == "__main__":
  fichier = pd.read_csv(input("Entrez le nom du fichier à importer : "), sep = ';')
  while True:
    print('\n 1 : Afficher données \n 2 : Calculer indicateurs \n 3 : Autres \n Entrez le numéro du choix \n "exit" pour sortir')
    action = while_liste('Que voulez-vous faire : ', ["1", "2", "3", "exit"])
    if action == "exit":
      break
    action = int(action)
    realisation(fichier, action)