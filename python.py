# PARTIE CODE

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import random as rd

d = {'X' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'Y' : [1, 2, 3, 4],
    'Z' : ['A', 'B', 'C', 'D']}
df = pd.DataFrame(d)


def choix_donnees():

  import_ = input("Entrez le chemin du fichier à importer : ")
  print("Import non réussi donc la suite sera faite avec un data frame déjà créé.")
 
  return (import_)


def while_liste(txt, liste, type = ''):

  variable = type(input(txt))
  while variable not in liste:
    variable = type(input(txt))

  return(variable)


def indicateurs(nom, type):
  if type == quanti:
    mini = min(nom)
   maxi = max(nom)
   mean = st.mean(nom)
   median = st.median(nom)
   sd = st.stdev(nom)
   var = st.variance(nom)
  
  else:
    print("l")

  return(pd.DataFrame([mini, maxi, mean, median, sd, var], index = ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var']))


def choix():
  print(" 1 : Afficher données \n 2 : Calculer indicateurs \n 3 : Autres \n Entrez le numéro du choix")
  action = -1
  while action != 3:
    action = while_liste('Que voulez-vous faire : ', range(1, 4), int)
    if action == 1:
      print(df)
    elif action == 2:
      colonne = while_liste('Nom de colonne sur lequel faire : ', ['X', 'Y'], str)
      type = while_liste('Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'], str)
      print(indicateurs(df[colonne], type))
    else:
      print("r")


# PARTIE UTILISATEUR


donnees = choix_donnees()
choix()
