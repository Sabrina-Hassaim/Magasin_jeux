from Jeux import Jeux 
from typing import List


class Magasin():
    def __init__(self, nom, numero, adresse) :
        self.nom = nom
        self.numero = numero
        self.adresse = adresse
        self.jeux = []
    
    def ajouter_jeu(self, jeu: Jeux):
        self.jeux.append(jeu)

    def remove_jeu(self, jeu: Jeux):
        self.jeux.remove(jeu)

    
    def afficher_jeux(self):
        for jeu in self.jeux:
            print(jeu.description)

    def nb_jeux(self):
        return len(self.jeux)

    