import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton


class MainWindoW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Modulaire PyQt6")
        self.resize(500, 300)
        # compteur interne
        self.counter = 0

        #Widget central et disposition
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout=QVBoxLayout()
        self.central_widget.setLayout(layout)

        #Création des widgets
        self.label=QLabel(f"Nombre de clics: {self.counter}")
        layout.addWidget(self.label)

        self.button=QPushButton("Incrimenter le compteur")
        layout.addWidget(self.button)

        #Connexion du signal au slot
        self.button.clicked.connect(self.increment_counter)

    def increment_counter(self):
        self.counter+=1
        self.label.setText(f"Nombre de clics: {self.counter}")

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindoW()
    window.show()
    sys.exit(app.exec())

