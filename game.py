from random import randint
from pprint import pprint


class Demineur:
    def __init__(self, mines=10, hauteur=10, largueur=10):
        self.nombre_mines = mines
        self.hauteur = 10
        self.largueur = 10
        self.grille_player = [[9 for _ in range(self.largueur)] for _ in range(self.hauteur)]
        self.grille_game = [[0 for _ in range(self.largueur)] for _ in range(self.hauteur)]
        self.placer_mines()
        self.perdu = False

    def placer_mines(self):  # placer les mines aléatoirement
        coordonate_mines = []  # liste des coordonnées des mines
        for _ in range(self.nombre_mines):  # on crée une liste de coordonnées de mines
            coordonate = (
            randint(0, self.hauteur - 1), randint(0, self.largueur - 1))  # on choisit une coordonnée aléatoire
            while coordonate in coordonate_mines:  # tant que cordonnnées mine
                coordonate = (randint(0, self.hauteur - 1), randint(0, self.largueur - 1))  # on en tire une nouvelle
            coordonate_mines.append(coordonate)  # on l'ajoute à la liste des mines
            self.grille_game[coordonate[0]][coordonate[1]] = 9  # ligne colone 9=mine
            cases_proches = self.recup_near(coordonate)  # recup coordonnées cases proches
            for coordonate_case in cases_proches.values():  # pour chaque case proche
                if self.grille_game[coordonate_case[0]][coordonate_case[1]] != 9:  # si case pas mine
                    self.grille_game[coordonate_case[0]][coordonate_case[1]] += 1  # ajoute 1 à la case

        pprint(self.grille_game)

    def recup_near(self, coordonate: tuple) -> dict:  # renvoie les coordonnées des cases proches
        ligne = coordonate[0]
        colonne = coordonate[1]
        coordonate_near = {}  # dictionnaire des coordonnées des cases proches
        if self.in_grille((coordonate[0], coordonate[1] - 1)):
            coordonate_near.update({"gauche": (coordonate[0], coordonate[1] - 1)})
        if self.in_grille((coordonate[0], coordonate[1] + 1)):
            coordonate_near.update({"droite": (coordonate[0], coordonate[1] + 1)})
        if self.in_grille((coordonate[0] + 1, coordonate[1])):
            coordonate_near.update({"bas": (coordonate[0] + 1, coordonate[1])})
        if self.in_grille((coordonate[0] - 1, coordonate[1])):
            coordonate_near.update({"haut": (coordonate[0] - 1, coordonate[1])})
        if self.in_grille((coordonate[0] - 1, coordonate[1] - 1)):
            coordonate_near.update({"haut_gauche": (coordonate[0] - 1, coordonate[1] - 1)})
        if self.in_grille((coordonate[0] - 1, coordonate[1] + 1)):
            coordonate_near.update({"haut_droite": (coordonate[0] - 1, coordonate[1] + 1)})
        if self.in_grille((coordonate[0] + 1, coordonate[1] + 1)):
            coordonate_near.update({"bas_gauche": (coordonate[0] + 1, coordonate[1] + 1)})
        if self.in_grille((coordonate[0] + 1, coordonate[1] - 1)):
            coordonate_near.update({"bas_droite": (coordonate[0] + 1, coordonate[1] - 1)})
        return coordonate_near

    def in_grille(self, coordonate: tuple) -> bool:  # renvoie True si coordonnées dans grille
        return 0 <= coordonate[0] < self.hauteur - 1 and 0 <= coordonate[
            1] <= self.largueur - 1  # si coordonnées dans grille

    def jouer(self, coordonate: tuple, cases=None):  # joue une case
        if self.perdu:
            return
        valeur_game = self.grille_game[coordonate[0]][coordonate[1]]  # recup valeur game
        if valeur_game == 9:  # si mine
            print("LOST")
            self.perdu = True
            return
        elif valeur_game != 0:  # si case non vide
            self.grille_player[coordonate[0]][coordonate[1]] = valeur_game
            return
        if cases is None: # si pas de cases à afficher
            cases = []
        if coordonate not in cases:
            cases.append(coordonate)# si coordonnées pas déjà dans cases
            self.grille_player[coordonate[0]][coordonate[1]] = valeur_game  # affiche valeur game
            for case in self.recup_near(coordonate).values(): # pour chaque case proche
                self.jouer(case, cases=cases)


if __name__ == "__main__":  # si on lance le script
    game = Demineur()  # on crée un nouveau jeu
