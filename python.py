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


def indicateurs(colonne): # Fonction qui calcule des indicateurs

  if colonne.dtypes == "int64":
    mini = min(colonne)
    maxi = max(colonne)
    mean = st.mean(colonne)
    median = st.median(colonne)
    sd = st.stdev(colonne)
    var = st.variance(colonne)  
    print(pd.DataFrame([mini, maxi, mean, median, sd, var], index = ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var']))
  else:
    compter(colonne)
    

def scatter(x, y):
  plt.plot(x, y)
  plt.savefig("nuage_de_points")


def realisation(data, choix): # Fonction qui agit en fonction du choix de l'utilisateur

  if choix == 1:
    print(data)
  elif choix == 2:
    colonne = while_liste('Nom de colonne sur lequel faire : ', data.columns)
    indicateurs(data[colonne])
  elif choix == 3:
    axe_x = while_liste("Nom de colonne pour l'axe x : ", data.columns)
    axe_x = while_liste("Nom de colonne pour l'axe x : ", data.columns)
    scatter(axe_x, axe_y)
  else:
    print("r")


# PARTIE UTILISATEUR

if __name__ == "__main__":
  fichier = pd.read_csv(input("Entrez le nom du fichier à importer : "), sep = ';')
  while True:
    print('\n 1 : Afficher données \n 2 : Calculer indicateurs \n 3 : Nuage de points \n Entrez le numéro du choix \n "exit" pour sortir')
    action = while_liste('Que voulez-vous faire : ', ["1", "2", "3", "exit"])
    if action == "exit":
      break
    action = int(action)
    realisation(fichier, action)
