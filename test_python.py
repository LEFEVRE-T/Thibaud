import unittest
import doctest
import python
import pandas as pd


class TestLancement(unittest.TestCase):
    def test_compter(self):
        donnees = ['A', 'A', 'A', 'B', 'C']
        self.assertEqual(python.compter(donnees), {'A': 3, 'B': 1, 'C': 1})


    def test_while_liste(self):
        choix = "A"
        txt = "Entrer quelque chose : "
        liste = ['A', 'B', 'C', 'D']
        get_user_input = python.fake_input([choix])
        self.assertEqual(python.while_liste(txt, liste, get_user_input), "A")

        # Teste que la fonction ne renvoie rien si l'input n'est pas dans la liste et renvoie un "StopIteration" ce qui confirme    que la fonction fonctionne mais comme cela créer une erreur je ne sais pas s'il faut mettre le test
        """
        choix = "E"
        get_user_input = python.fake_input([choix])
        self.assertEqual(python.while_liste(txt, liste, get_user_input), "")       
        """

    # Test apparement non fonctionnel car la vraie valeur d'un DataFrame est ambigüe ; du coup je n'ai pas mis le test pour les     autres fonctions
    """
    def test_indicateurs(self):
        df = pd.DataFrame({'A': [2,4,6,8,10], 'B': ['A', 'B', 'C', 'B', 'A']})
        reponse = pd.DataFrame([2,10,6,6,3.162278,10], index = ['Min', 'Max', 'Mean', 'Med', 'Sd', 'Var'])
        self.assertEqual(python.indicateurs(df['A']), reponse)
    """

if __name__ == "__main__":
    unittest.main(exit=False)
    doctest.testmod(python)