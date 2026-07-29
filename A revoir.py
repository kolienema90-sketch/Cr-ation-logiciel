import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Application Professionnelle - PyQt6")
    self.setMinimumSize(850, 550)

    # Widget central et disposition principale
    self.central_widget = QWidget()
    self.setCentralWidget(self.central_widget)
    main_layout = QHBoxLayout(self.central_widget)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    # 1. Barre latérale (Sidebar)
    sidebar = QWidget()
    sidebar.setObjectName("Sidebar")
    sidebar.setFixedWidth(220)
    sidebar_layout = QVBoxLayout(sidebar)
    sidebar_layout.setContentsMargins(15, 20, 15, 20)
    sidebar_layout.setSpacing(10)

    title_label = QLabel("MonLogiciel")
    title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
    sidebar_layout.addWidget(title_label)

    sidebar_layout.addSpacing(20)

    # Boutons de navigation
    self.btn_dashboard = QPushButton("Tableau de bord")
    self.btn_analytics = QPushButton("Analyses")
    self.btn_settings = QPushButton("Paramètres")

    for btn in [self.btn_dashboard, self.btn_analytics, self.btn_settings]:
      btn.setFixedHeight(40)
      btn.setCursor(Qt.CursorShape.PointingHandCursor)
      sidebar_layout.addWidget(btn)

    sidebar_layout.addStretch()
    main_layout.addWidget(sidebar)

    # 2. Zone de contenu principal
    self.content_area = QWidget()
    self.content_area.setObjectName("ContentArea")
    content_layout = QVBoxLayout(self.content_area)
    content_layout.setContentsMargins(30, 30, 30, 30)

    self.header_label = QLabel("Tableau de bord")
    self.header_label.setStyleSheet(
        "font-size: 22px; font-weight: bold; color: #2C3E50;"
    )
    content_layout.addWidget(self.header_label)

    content_layout.addSpacing(15)

    self.desc_label = QLabel(
        "Bienvenue dans l'interface principale. Sélectionnez une option dans"
        " le menu de gauche."
    )
    self.desc_label.setStyleSheet("font-size: 14px; color: #7F8C8D;")
    content_layout.addWidget(self.desc_label)

    content_layout.addStretch()
    main_layout.addWidget(self.content_area)

    # Application des styles QSS (Feuille de style)
    self.apply_stylesheet()

    # Connexions des signaux
    self.btn_dashboard.clicked.connect(lambda: self.switch_content("Tableau de bord"))
    self.btn_analytics.clicked.connect(lambda: self.switch_content("Analyses de données"))
    self.btn_settings.clicked.connect(lambda: self.switch_content("Paramètres du système"))

  def switch_content(self, title):
    self.header_label.setText(title)
    self.desc_label.setText(f"Affichage des données pour : {title}")

  def apply_stylesheet(self):
    stylesheet = """
            QWidget#Sidebar {
                background-color: #1E1E2F;
            }
            QWidget#Sidebar QPushButton {
                background-color: transparent;
                color: #A0A0AB;
                border: none;
                text-align: left;
                padding-left: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QWidget#Sidebar QPushButton:hover {
                background-color: #2D2D44;
                color: white;
            }
            QWidget#ContentArea {
                background-color: #F8F9FA;
            }
        """
    self.setStyleSheet(stylesheet)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())
