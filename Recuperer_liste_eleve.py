import sys
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class GestionEleves(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Configuration de la fenêtre
    self.setWindowTitle("Saisie de liste d'élèves - PyQt6")
    self.resize(350, 400)

    # Layout principal
    layout_principal = QVBoxLayout()

    # 1. Section de saisie d'un élève
    layout_saisie = QHBoxLayout()
    self.input_eleve = QLineEdit()
    self.input_eleve.setPlaceholderText("Nom de l'élève...")
    # Permet d'ajouter en appuyant sur Entrée
    self.input_eleve.returnPressed.connect(self.ajouter_eleve)

    btn_ajouter = QPushButton("Ajouter")
    btn_ajouter.clicked.connect(self.ajouter_eleve)

    layout_saisie.addWidget(self.input_eleve)
    layout_saisie.addWidget(btn_ajouter)
    layout_principal.addLayout(layout_saisie)

    # 2. Liste visuelle des élèves (QListWidget)
    self.liste_widget = QListWidget()
    layout_principal.addWidget(QLabel("Liste des élèves saisis :"))
    layout_principal.addWidget(self.liste_widget)

    # Bouton pour supprimer un élève sélectionné
    btn_supprimer = QPushButton("Supprimer la sélection")
    btn_supprimer.clicked.connect(self.supprimer_eleve)
    layout_principal.addWidget(btn_supprimer)

    # 3. Bouton pour récupérer et valider la liste finale
    btn_valider = QPushButton("Récupérer la liste (Action)")
    btn_valider.setStyleSheet("background-color: #4CAF50; color: white;")
    btn_valider.clicked.connect(self.recuperer_liste_eleves)
    layout_principal.addWidget(btn_valider)

    self.setLayout(layout_principal)

  def ajouter_eleve(self):
    nom = self.input_eleve.text().strip()
    if nom:
      self.liste_widget.addItem(nom)
      self.input_eleve.clear()  # Vider le champ de saisie
      self.input_eleve.setFocus()  # Remettre le focus

  def supprimer_eleve(self):
    ligne_selectionnee = self.liste_widget.currentRow()
    if ligne_selectionnee >= 0:
      self.liste_widget.takeItem(ligne_selectionnee)

  def recuperer_liste_eleves(self):
    # Récupération de tous les éléments du QListWidget dans une liste Python
    liste_eleves = []
    for index in range(self.liste_widget.count()):
      liste_eleves.append(self.liste_widget.item(index).text())

    # Exemple d'utilisation de la liste récupérée
    print("Liste finale des élèves :", liste_eleves)

    # Affichage d'un récapitulatif pour l'utilisateur
    from PyQt6.QtWidgets import QMessageBox

    if liste_eleves:
      noms = ", ".join(liste_eleves)
      QMessageBox.information(
          self,
          "Succès",
          f"Nombre d'élèves : {len(liste_eleves)}\nÉlèves : {noms}",
      )
    else:
      QMessageBox.warning(
          self, "Attention", "La liste des élèves est vide !"
      )


if __name__ == "__main__":
  app = QApplication(sys.argv)
  fenetre = GestionEleves()
  fenetre.show()
  sys.exit(app.exec())