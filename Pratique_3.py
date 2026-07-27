import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactivité PyQt6")
        self.resize(400, 200)

        self.init_ui()
    def init_ui(self):
            self.label=QLabel("Prêt....", self)
            self.bouton=QPushButton("Cliquez-moi", self)
        #Connexion du signal 'clicked' à notre methode (slot)
            self.bouton.clicked.connect(self.dire_bonjour)

            layout=QVBoxLayout()
            layout.addWidget(self.label)
            layout.addWidget(self.bouton)

            self.setLayout(layout)
        #Définition du slot(la méthode appelée lors du clic)
    def dire_bonjour(self):
            self.label.setText("Le bouton a été cliqué avec succès!")












if __name__=="__main__":
    app=QApplication(sys.argv)
    fenetre=MaFenetre()
    fenetre.show()
    sys.exit(app.exec())