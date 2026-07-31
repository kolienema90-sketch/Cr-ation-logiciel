import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
QApplication,
QWidget,
QLabel,
QLineEdit,
QPushButton,
QVBoxLayout
)
from PyQt6.QtCore import Qt

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Mon premier logiciel")
        self.resize(800, 600)
        #Layout principale
        layout = QVBoxLayout()

        # 1 Label d'instruction
        self.label_instruction = QLabel("Veuillez remplir ce champ ci-dessous!", self)
        self.label_instruction.setStyleSheet("color:red")
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_instruction)

        # 2 Champ de saisie
        self.champ_saisie = QLineEdit(self)
        self.champ_saisie.setPlaceholderText("Ecrivez votre nom ici...")
        layout.addWidget(self.champ_saisie)

        # 3 Bouton de validation
        self.button_valider = QPushButton("Je valide", self)
        layout.addWidget(self.button_valider)

        # 4 Label pour afficher le resultat
        self.label_resultat = QLabel("", self)
        layout.addWidget(self.label_resultat)

        # Connexion du bouton au clic
        self.button_valider.clicked.connect(self.recuperer_valeur)


        self.setLayout(layout)

    def recuperer_valeur(self):
        # récupération de la valeur saisie dans QLineEdit
        valeur_saisie = self.champ_saisie.text()

        #Affichage du resultat dans label_resultat
        if valeur_saisie.strip() == "":
            self.label_resultat.setText("Vous n'aviez rien saisie")

        else:
            self.label_resultat.setText(f"Votre nom est: {valeur_saisie}")

            #Affichage dans le consle python
            print(f"Votre nom est: {valeur_saisie}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaFenetre()
    window.show()

    sys.exit(app.exec())