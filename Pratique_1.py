import sys
from PyQt6.QtWidgets import QApplication, QWidget

#création de la classe principale qui herite de QWidget
class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        #Configuration de la fenêtre
        self.setWindowTitle("Mon application PyQt6")
        self.resize(400, 300)

# Point d'entrée de l'application
if __name__=="__main__":

   #Initialisation de l'application
   app = QApplication(sys.argv)

   #Instancination de la classe
   fenetre=MaFenetre()
   fenetre.show()

   #Lancement de la boucle
   sys.exit(app.exec())