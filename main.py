#importation des bibliothèques
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import sys

#Création d'une variable app
app = QApplication(sys.argv)

#création de la fenêtre, déclaration de la variable window
window = QMainWindow()

#Taille de la fenêtre
window.setGeometry(100, 100, 800, 600)
#Titre de la fenêtre
window.setWindowTitle("Mon Prémier logiciel")
#couleur de la fenêtre
window.setStyleSheet("background-color: rgb(25, 25, 35)")

y = 200

# Label d'instruction
labelInput = QLabel("Entrez un message!", window)
labelInput.setStyleSheet("color: white")
labelInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
labelInput.setGeometry(
    int((window.width() - 400) / 2),
    int(y),
    400,
    30
)
y += 40

# Champ de saisie (QLineEdit)
input = QLineEdit(window)
input.setObjectName("input")
input.setStyleSheet("background-color: white")
input.setGeometry(
    int((window.width() - 300) / 2),
    int(y),
    300,
    30
)

# Actualiser la variable y
y += 50

# Ajout d'un bouton
button = QPushButton("Lancer le script", window)
button.setStyleSheet("background-color: white; border-radius: 5px")
button.setGeometry(
    int((window.width() - 200) / 2),
    int(y),
    200,
    35
)

# Mettre le texte pour les résultats, on actualise y d'abord
y += 55
resultat = QLabel("", window)
resultat.setStyleSheet("color: white; font-size: 25px")
resultat.setAlignment(Qt.AlignmentFlag.AlignCenter)
resultat.setGeometry(
    int((window.width() - 400) / 2),
    int(y),
    400,
    40
)

# Codage du script exécuté
def script(message):
    resultat.setText(message)

# Créer un événement sur le bouton, lorsqu'on clique dessus on lance la fonction script
button.clicked.connect(lambda: script(input.text()))

# Affichage de la fenêtre
window.show()

# Pour tout stop
sys.exit(app.exec())
