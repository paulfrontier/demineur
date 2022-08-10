import sys

from PySide6 import QtWidgets, QtGui
from game import Demineur


class Interface(QtWidgets.QWidget):  # classe de l'interface
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.game = Demineur(mines=20, hauteur=20, largueur=20)  # Création du jeu
        self.largueur = self.game.largueur * 25
        self.hauteur = self.game.hauteur * 25 + 50
        self.setMinimumSize(self.largueur, self.hauteur)
        self.setMaximumSize(self.largueur, self.hauteur)
        self.setWindowTitle("Demineur")
        self.setup_ui()

    def setup_ui(self):  # Création du layout
        self.create_layout()
        self.create_widgets()
        self.update_interface()

    def create_layout(self):
        self.main_layout = QtWidgets.QGridLayout(self)  # Création du layout principal
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

    def create_widgets(self):
        label_drapeau = QtWidgets.QLabel("Drapeau")
        drapeau_icone = QtGui.QPixmap("minrr.png")  # Création de l'icône
        drapeau_icone = drapeau_icone.scaled(25, 25) # redimensionnement de l'image
        label_drapeau.setPixmap(drapeau_icone)  # affichage de l'image
        label_score = QtWidgets.QLabel(str(self.game.nombre_mines))         # Création du label score
        label_drapeau.setStyleSheet("background-color : #4A752C")
        label_score.setStyleSheet("background-color : #4A752C")
        self.main_layout.addWidget(label_drapeau, 0, 0, 1, 2)
        self.main_layout.addWidget(label_score, 0, 2, 1, -1)

    def update_interface(self):
        for ligne in range(len(self.game.grille_player)): # Création des cases lignes
            for colonne in range(len(self.game.grille_player[ligne])): # Création des cases colonnes
                self.creer_case((ligne, colonne), self.game.grille_player[ligne][colonne])

    def recup_teinte_damier(self, coordonate):
        if coordonate[0] % 2 == 0 and coordonate[1] % 2 == 0:
            return "claire"
        if coordonate[0] % 2 == 1 and coordonate[1] % 2 == 1:
            return "claire"
        return "fonce"

    def creer_case(self, coordonate: tuple, valeur: int):
        global couleur
        couleur_police = "black"
        teinte = self.recup_teinte_damier(coordonate)
        case = QtWidgets.QPushButton("")

        if valeur == 9:
            couleur = "#a2s149" if teinte == "fonce" else "#d3f590"
        elif 0 <= valeur <= 8:
            couleur = "#d7b899" if teinte == "fonce" else "#e5c29f"
            if valeur != 0:
                case.setText(str(valeur))
            if valeur == 1:
                couleur_police = "bleu"
            elif valeur == 2:
                couleur_police = "vert"
            elif valeur == 3:
                couleur_police = "rouge"
            elif valeur == 4:
                couleur_police = "orange"
            elif valeur == 5:
                couleur_police = "violet"
        if self.game.perdu and valeur == 9:
            case.setText("B")
            couleur = "#a2s149"

        case.setStyleSheet(f"""
            background-color : {couleur};
            color : {couleur_police};
            border : none;
            max-width : 25px;
            max-height : 25px;
            min-width : 25px;
            min-height : 25px;
            margin : 0; 
            """)
        case.clicked.connect(lambda: self.jouer(coordonate)) # Création de la connection
        self.main_layout.addWidget(case, coordonate[0] + 1, coordonate[1], 1, 1)

    def jouer(self, coordonate: tuple):
        self.game.jouer(coordonate)
        self.update_interface()
        if self.game.perdu:
            perdu = QtWidgets.QMessageBox(text="Perdu")
            perdu.exec()
