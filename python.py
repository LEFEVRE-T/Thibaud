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
    

def scatter(data, x, y):
  plt.scatter(data[x], data[y])
  plt.title(x + str(" en fonction de ") + y)
  plt.xlabel(x)
  plt.ylabel(y)
  plt.savefig(str("Nuage_de_points de ") + x + str(" en fonction de ") + y)


def barplot(data, x):
  data[x].value_counts(normalize = True).plot(kind = 'bar')
  plt.title(str("Répartition de la variable ") + x)
  plt.xlabel(x)
  plt.ylabel("Fréquence")
  plt.savefig(str("Diagramme en barres de la variable ") + x)


def piechart(data, x):
  data[x].value_counts(normalize = True).plot(kind = 'pie')
  plt.axis('equal') 
  plt.title(str("Répartition de la variable ") + x)
  plt.savefig(str("Diagramme circulaire de la variable ") + x)


def realisation(data, choix): # Fonction qui agit en fonction du choix de l'utilisateur

  if choix == "1":
    print(data)
  elif choix == "2":
    colonne = while_liste('Nom de colonne sur lequel faire : ', data.columns)
    indicateurs(data[colonne])
  elif choix == "3":
    axe_x = while_liste("Nom de colonne pour l'axe x : ", data.columns)
    axe_y = while_liste("Nom de colonne pour l'axe y : ", data.columns)
    scatter(data, axe_x, axe_y)
  elif choix == "4":
    axe_x = while_liste("Nom de colonne pour l'axe x : ", data.columns)
    barplot(data, axe_x)
  elif choix == "5":
    variable = while_liste("Nom de colonne pour la variable : ", data.columns)
    piechart(data, variable)
  else:
    print("r")


#""
if __name__ == "__main__":
  fichier = pd.read_csv(input("Entrez le nom du fichier à importer : "), sep = ';')
  while True:
    print('\n 1 : Afficher données \n 2 : Calculer indicateurs \n 3 : Nuage de points \n 4 : Diagramme en barres \n 5 : Diagramme circulaire \n Entrez le numéro du choix \n "exit" pour sortir')
    action = while_liste('Que voulez-vous faire : ', ["1", "2", "3", "4", "5", "exit"])
    if action == "exit":
      break
    realisation(fichier, action)
import matplotlib.pyplot as plt
 PARTIE UTILISATEUR
"
# Histogramme
data["montant"].hist(density=True)
plt.show()
# Histogramme plus beau
data[data.montant.abs() < 100]["montant"].hist(density=True,bins=20)
plt.show()
