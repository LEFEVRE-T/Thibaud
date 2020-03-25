# PARTIE IMPORTS

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import random
import collections


# PARTIE CODE

def choix_donnees(): # Fonction pour l'import des données

  fichier = pd.read_csv(input("Entrez le nom du fichier à importer : "), sep = ';')
 
  return (fichier)


def while_liste(txt, liste, type = str): #Fonction qui permet de ne pas avoir à écrire le while à chaque fois

  variable = type(input(txt))
  while variable not in liste:
    variable = type(input(txt))

  return(variable)


def compter(donnees): # Fonction qui compte les éléments
  
  compteur = collections.Counter(donnees)
  print(compteur)


def indicateurs(data): # Fonction qui calcule des indicateurs

  colonne = while_liste('Nom de colonne sur lequel faire : ', data.columns)
  type_donnees = while_liste('Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'])
  if type_donnees == "quanti":
    mini = min(data[colonne])
    maxi = max(data[colonne])
    mean = st.mean(data[colonne])
    median = st.median(data[colonne])
    sd = st.stdev(data[colonne])
    var = st.variance(data[colonne])  
    print(pd.DataFrame([mini, maxi, mean, median, sd, var], index = ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var']))
  else:
    compter(data[colonne])
    

def realisation(data, choix): # Fonction qui agit en fonction du choix de l'utilisateur

  if choix == 1:
    print(donnees)
  elif choix == 2:
    indicateurs(data)
  else:
    print("r")


def choix(donnees): # Fonction qui fait choisir à l'utilisateur l'action à réaliser

  while True:
    print('\n 1 : Afficher données \n 2 : Calculer indicateurs \n 3 : Autres \n Entrez le numéro du choix \n "exit" pour sortir')
    action = while_liste('Que voulez-vous faire : ', ["1", "2", "3", "exit"])
    if action == "exit":
      break
    action = int(action)
    realisation(donnees, action)


# PARTIE UTILISATEUR

if __name__ == "__main__":
  donnees = choix_donnees()
  choix(donnees)