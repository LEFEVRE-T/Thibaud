import unittest
import doctest
import python


class TestLancement(unittest.TestCase):
    def test_import(self):
        self.assertEqual(devine.registre, {})
        self.assertEqual(devine.renvoie1(), 1)

    def test_gagne_perdu_simple(self):
        solution = 3
        restants = 1
        user_input = devine.fake_input([solution])
        self.assertEqual(devine.devine(restants, solution, user_input), "gagne")

        user_input = devine.fake_input([solution + 1])
        self.assertEqual(devine.devine(restants, solution, user_input), "perdu")


if __name__ == "__main__":
    unittest.main(exit=False)
    doctest.testmod(python)