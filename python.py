# PARTIE CODE

import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import random as rd

"""
def indicateurs_quali(x):

"""
def while_liste(variable, txt, liste):
  variable = input(txt)
  while variable not in liste:
    variable = input(txt)





def demande(nbr):
  if nbr == 0:
    print("Le programme ne vous est pas déstiné.")
  elif nbr == 1:
    while_liste("type", 'Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'])
  else:
    while_liste("type", 'Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'])

def indicateurs_num(x):
  mini = min(x)
  maxi = max(x)
  mean = st.mean(x)
  median = st.median(x)
  sd = st.stdev(x)
  var = st.variance(x)
  return(mini, maxi, mean, median, sd, var)

def data_frame_1(x, nom_x, index):
  name = pd.DataFrame({nom_x : pd.Series(x, index = index)})
  return(name)

def data_frame_2(x, nom_x, y, nom_y, index):
  name = pd.DataFrame({nom_x : pd.Series(x, index = index), nom_y : y})
  return(name)

d = {'X' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),   'Y' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
plt.plot('X', 'Y', 'cs', data=df)
plt.show()
print(df)
print(indicateurs_num(df.X)[1])


# PARTIE UTILISATEUR

while_liste("type", 'Type de données entre "quali" & "quanti" : ', ['quali', 'quanti'])

demande(nbr)
indi1 = indicateurs_num(df.X)
indi2 = indicateurs_num(df.Y)
print(data_frame_2(indi1, "e", indi2, "f", ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var']))
