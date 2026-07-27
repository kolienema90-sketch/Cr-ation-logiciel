import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple PyQt6")
        self.resize(400, 200)

        # Appel de la méthode qui initialise les composants
        self.init_ui()

    def init_ui(self):
        # 1. Création des widgets
        self.label = QLabel("Bonjour, bienvenue dans PyQt6 !", self)
        self.bouton = QPushButton("Cliquez-ici", self)

        # 2. Organisation de la mise en page (Layout vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.bouton)

        # Application du layout à la fenêtre
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec())