from Magasin import Magasin
import unittest
from unittest.mock import Mock

class TestMagasin(unittest.TestCase):
    def setUp(self):
        self. magasin1 = Magasin("Magasin1", "0123456789", "Evry")
        self.jeu1 = Mock(cosole_jeu="PS2", genre="RPG", prix=23, description="jeu de RPG", code_rayon="ABC.12.35.20")

    def test_ajouter_jeu(self):
        self.magasin1.ajouter_jeu(self.jeu1)
        self.assertTrue(self.jeu1 in self.magasin1.jeux)

    def test_supprimer_jeu(self):
        self.magasin1.ajouter_jeu(self.jeu1)
        self.magasin1.remove_jeu(self.jeu1)
        self.assertFalse(self.jeu1 in self.magasin1.jeux)

    
    def test_nb_jeux(self):
        self.magasin1.ajouter_jeu(self.jeu1)
        self.assertTrue(self.magasin1.nb_jeux() == 1)