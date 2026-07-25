import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class FenetreSaisie(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Configuration de la fenêtre principale
    self.setWindowTitle("Exemple de saisie PyQt6")
    self.resize(350, 200)

    # Layout principal vertical
    layout = QVBoxLayout()

    # 1. Création d'un label d'instruction
    self.label_instruction = QLabel(
        "Veuillez entrer une valeur ci-dessous :", self
    )
    layout.addWidget(self.label_instruction)

    # 2. Champ de saisie (QLineEdit)
    self.champ_saisie = QLineEdit(self)
    self.champ_saisie.setPlaceholderText("Tapez quelque chose ici...")
    layout.addWidget(self.champ_saisie)

    # 3. Bouton de validation (QPushButton)
    self.bouton_valider = QPushButton("Valider", self)
    layout.addWidget(self.bouton_valider)

    # 4. Label pour afficher le résultat
    self.label_resultat = QLabel("", self)
    layout.addWidget(self.label_resultat)

    # Connexion du clic du bouton à la méthode de récupération
    self.bouton_valider.clicked.connect(self.recuperer_valeur)

    # Application du layout à la fenêtre
    self.setLayout(layout)

  def recuperer_valeur(self):
    # Récupération de la valeur saisie dans le QLineEdit
    valeur_saisie = self.champ_saisie.text()

    # Affichage de la valeur récupérée dans le label
    if valeur_saisie.strip() == "":
      self.label_resultat.setText("⚠️ Vous n'avez rien saisi !")
    else:
      self.label_resultat.setText(f"✅ Valeur récupérée : {valeur_saisie}")

      # (Optionnel) Affichage également dans la console Python
      print(f"Valeur récupérée : {valeur_saisie}")


if __name__ == "__main__":
  # Initialisation de l'application PyQt
  app = QApplication(sys.argv)

  # Création et affichage de la fenêtre
  fenetre = FenetreSaisie()
  fenetre.show()

  # Exécution de la boucle principale de l'application
  sys.exit(app.exec())