import pandas as pd
import matplotlib.pyplot as plt

def indicateurs(x, y):
  minimum_x = min(x)
  minimum_y = min(y)
  print(minimum_x)


def data_frame(x, nom_x, y, nom_y, index, name):
  name = pd.DataFrame({nom_x : pd.Series(x, index = index), nom_y : y})
  return(name)

d = {'X' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),   'Y' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
plt.plot('X', 'Y', 'cs', data=df)
plt.show()
print(df)
indicateurs(df.X, df.Y)
print(data_frame([2,4,6,7], "mi", [3,5,7,9], "ki", "gg"))