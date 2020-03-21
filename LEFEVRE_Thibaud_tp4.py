# -*- coding: utf-8 -*-
import statistics

def p1(liste):
    return liste
def p2(liste):
    return [x**2 for x in liste]
def p3(liste):
    return [x**3 for x in liste]
def p4(liste):
    return [x**4 for x in liste]
def pown(n):
    def puissance(liste):        
        return [x**n for x in liste]
    return puissance

registre_valeurs = {}
registre_fonction = {'sum' : sum, 'max' : max, 'min' : min, 'moy' : statistics.mean,
                     'sd' : statistics.stdev, 'puiss1' : p1, 'puiss2' : p2,
                     'puiss3' : p3, 'puiss4' : p4, 'puiss' : pown}
#Ajouter la fonction sum au registre

def loop():
    dataset_name = input("Entrez le nom du dataset")
    if dataset_name not in registre_valeurs:
        valeurs = input("Entrez les valeurs séparées par une virgule ")
        registre_valeurs[dataset_name] = valeurs =  [float(x) for x in valeurs.split(',')]
    fonction = input("Donnez le nom de la fonction a utiliser")
    if fonction not in registre_fonction:
        exposant = fonction.split('(')[1].split(')')[0]
        print(registre_fonction[fonction](exposant)(valeurs))
        fonction = registre_fonction[fonction]
        fonction(valeurs)
    print((registre_valeurs[dataset_name]))


if __name__ == "__main__":
  while True:
      message = input("entrée pour continuer, quittez en tapant exit puis entrée ")
      if message == "exit":
          break
      loop()