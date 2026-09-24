import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QTableWidget,
                             QTableWidgetItem, QComboBox, QStackedWidget,
                             QMessageBox, QHeaderView, QLineEdit, QListWidget,
                             QInputDialog, QTabWidget)
from PyQt6.QtCore import Qt


class GestionElevesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logiciel de Gestion des Élèves")
        self.resize(900, 600)

        # Variables de stockage des données
        self.eleves = []  # Liste de dict: [{'nom': '...', 'genre': 'Garçon'/'Fille'}]
        self.matieres = []
        self.semestre = ""
        self.annee = ""

        # Widget central empilé pour gérer les étapes
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Initialisation des étapes
        self.init_etape1()
        self.init_etape2()
        self.init_etape3()
        self.init_etape4()
        self.init_etape5()

    # ==========================================
    # ETAPE 1 : Saisie des élèves
    # ==========================================
    def init_etape1(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        titre = QLabel("Étape 1 : Saisie de la liste des élèves")
        titre.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(titre)

        self.table_eleves = QTableWidget(0, 2)
        self.table_eleves.setHorizontalHeaderLabels(["Nom de l'élève", "Genre et Action"])
        self.table_eleves.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table_eleves)

        btn_layout = QHBoxLayout()
        btn_supprimer = QPushButton("Supprimer la ligne")
        btn_supprimer.clicked.connect(lambda: self.table_eleves.removeRow(
            self.table_eleves.currentRow()) if self.table_eleves.currentRow() >= 0 else None)
        btn_layout.addWidget(btn_supprimer)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Bouton Suivant en bas à droite
        nav_layout = QHBoxLayout()
        nav_layout.addStretch()
        btn_suivant = QPushButton("Suivant")
        btn_suivant.clicked.connect(self.valider_etape1)
        nav_layout.addWidget(btn_suivant)

        layout.addLayout(nav_layout)
        self.stacked_widget.addWidget(page)

        # Ajouter une ligne par défaut
        self.ajouter_ligne_eleve()

    def ajouter_ligne_eleve(self):
        row = self.table_eleves.rowCount()
        self.table_eleves.insertRow(row)

        # --- Champ de saisie (Nom) ---
        line_nom = QLineEdit()
        line_nom.setPlaceholderText("Saisissez le nom (Entrée pour valider)")
        line_nom.returnPressed.connect(self.ajouter_ligne_eleve)
        self.table_eleves.setCellWidget(row, 0, line_nom)

        # --- Conteneur pour Genre et Bouton Ajouter ---
        container = QWidget()
        layout_genre = QHBoxLayout(container)
        layout_genre.setContentsMargins(5, 2, 5, 2)

        combo_genre = QComboBox()
        combo_genre.addItems(["Garçon", "Fille"])

        btn_ajouter = QPushButton("Ajouter un élève")
        btn_ajouter.clicked.connect(self.ajouter_ligne_eleve)

        layout_genre.addWidget(combo_genre)
        layout_genre.addWidget(btn_ajouter)

        self.table_eleves.setCellWidget(row, 1, container)

        # --- MISE EN FORME CONDITIONNELLE ---
        def appliquer_style_genre(genre):
            font = line_nom.font()
            font.setBold(genre == "Fille")
            line_nom.setFont(font)

        # Connecter le changement de texte du combo box à la fonction de style
        combo_genre.currentTextChanged.connect(appliquer_style_genre)
        # Initialiser le style au cas où (bien que par défaut ce soit "Garçon")
        appliquer_style_genre(combo_genre.currentText())

        # Donner le focus automatiquement pour accélérer la saisie
        line_nom.setFocus()

    def valider_etape1(self):
        self.eleves.clear()
        for row in range(self.table_eleves.rowCount()):
            # Extraction du nom depuis le QLineEdit
            widget_nom = self.table_eleves.cellWidget(row, 0)
            if widget_nom and isinstance(widget_nom, QLineEdit):
                nom = widget_nom.text().strip()
                if nom:
                    # Extraction du genre depuis le conteneur
                    container = self.table_eleves.cellWidget(row, 1)
                    if container:
                        combo = container.findChild(QComboBox)
                        genre = combo.currentText() if combo else "Garçon"
                        self.eleves.append({'nom': nom, 'genre': genre})

        if not self.eleves:
            QMessageBox.warning(self, "Erreur", "Veuillez saisir obligatoirement au moins un élève.")
            return
        self.stacked_widget.setCurrentIndex(1)

    # ==========================================
    # ETAPE 2 : Saisie des matières
    # ==========================================
    def init_etape2(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        titre = QLabel("Étape 2 : Saisie des matières")
        titre.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(titre)

        self.list_matieres = QListWidget()
        layout.addWidget(self.list_matieres)

        btn_layout = QHBoxLayout()
        btn_ajouter = QPushButton("Cliquez ici pour ajouter une matière")
        btn_ajouter.setStyleSheet("background-color: black; font-weight: bold; color: white; font-size: 20px;")
        btn_ajouter.clicked.connect(self.ajouter_matiere)
        btn_supprimer = QPushButton("Supprimer la matière")
        btn_supprimer.setStyleSheet("background-color: white; font-weight: bold; color: red; font-size: 20px;")
        btn_supprimer.clicked.connect(lambda: self.list_matieres.takeItem(self.list_matieres.currentRow()))
        btn_layout.addWidget(btn_ajouter)
        btn_layout.addWidget(btn_supprimer)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        nav_layout = QHBoxLayout()
        btn_prec = QPushButton("Précédant")
        btn_prec.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        btn_suivant = QPushButton("Suivant")
        btn_suivant.clicked.connect(self.valider_etape2)
        nav_layout.addWidget(btn_prec)
        nav_layout.addStretch()
        nav_layout.addWidget(btn_suivant)

        layout.addLayout(nav_layout)
        self.stacked_widget.addWidget(page)

    def ajouter_matiere(self):
        text, ok = QInputDialog.getText(self, "Matière", "Nom de la matière :")
        if ok and text:
            self.list_matieres.addItem(text)

    def valider_etape2(self):
        self.matieres = [self.list_matieres.item(i).text() for i in range(self.list_matieres.count())]
        if not self.matieres:
            QMessageBox.warning(self, "Erreur", "Veuillez saisir au moins une matière.")
            return
        self.stacked_widget.setCurrentIndex(2)

    # ==========================================
    # ETAPE 3 : Semestre et Année
    # ==========================================
    def init_etape3(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titre = QLabel("Étape 3 : Sélection du Semestre et de l'Année")
        titre.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(titre, alignment=Qt.AlignmentFlag.AlignCenter)

        self.combo_semestre = QComboBox()
        self.combo_semestre.addItems(["1er Semestre", "2ème Semestre", "3ème Semestre"])
        layout.addWidget(self.combo_semestre)

        self.combo_annee = QComboBox()
        self.combo_annee.addItems(["2026-2027", "2027-2028"])
        layout.addWidget(self.combo_annee)

        nav_layout = QHBoxLayout()
        btn_prec = QPushButton("Précédant")
        btn_prec.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        btn_suivant = QPushButton("Suivant")
        btn_suivant.clicked.connect(self.valider_etape3)
        nav_layout.addWidget(btn_prec)
        nav_layout.addStretch()
        nav_layout.addWidget(btn_suivant)

        layout.addLayout(nav_layout)
        self.stacked_widget.addWidget(page)

    def valider_etape3(self):
        self.semestre = self.combo_semestre.currentText()
        self.annee = self.combo_annee.currentText()
        self.preparer_etape4()
        self.stacked_widget.setCurrentIndex(3)

    # ==========================================
    # ETAPE 4 : Résumé et Confirmation
    # ==========================================
    def init_etape4(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_resume = QLabel("")
        self.label_resume.setStyleSheet("font-size: 30px; font-weight: bold; color: red;")
        self.label_resume.setWordWrap(True)
        self.label_resume.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_resume)

        nav_layout = QHBoxLayout()
        btn_prec = QPushButton("Précédant")
        btn_prec.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        btn_ok = QPushButton("Ok")
        btn_ok.clicked.connect(self.valider_etape4)
        nav_layout.addWidget(btn_prec)
        nav_layout.addStretch()
        nav_layout.addWidget(btn_ok)

        layout.addLayout(nav_layout)
        self.stacked_widget.addWidget(page)

    def preparer_etape4(self):
        N = len(self.eleves)
        nb_G = sum(1 for e in self.eleves if e['genre'] == "Garçon")
        nb_F = N - nb_G
        nb_Ma = len(self.matieres)

        texte = (f"Pour les résultats du  {self.semestre}  de l’année  {self.annee} ,\n"
                 f"Vous aviez  {N}  élèves au total dont  {nb_G}  garçons et  {nb_F}  filles.\n\n"
                 f"Ces élèves ont composés dans  {nb_Ma}  matières.")
        self.label_resume.setText(texte)

    def valider_etape4(self):
        self.generer_interface_principale()
        self.stacked_widget.setCurrentIndex(4)

    # ==========================================
    # ETAPE 5 : Interface Principale (Tableau Final)
    # ==========================================

    def init_etape5(self):
        self.page_principale = QWidget()
        self.layout_principal = QVBoxLayout(self.page_principale)

        # Le Ruban (Ribbon)
        self.ruban = QTabWidget()
        self.ruban.setFixedHeight(70)

        # Initiation des différents onglets
        self.onglet_fichier = QWidget()
        self.onglet_accueil = QWidget()
        self.onglet_modifier = QWidget()
        self.onglet_historique = QWidget()

        # Ajout des onglets au ruban
        self.ruban.addTab(self.onglet_fichier, "Fichier")
        self.ruban.addTab(self.onglet_accueil, "Accueil")
        self.ruban.addTab(self.onglet_modifier, "Modifier")
        self.ruban.addTab(self.onglet_historique, "Historiques")

        # Configuration de l'onglet accueil
        layout_accueil = QHBoxLayout()
        # Réduction de l'espace interne du ruban (gauche, haut, droite, bas)
        layout_accueil.setContentsMargins(5, 2, 5, 2)

        self.btn_enregistrer = QPushButton("Enregistrer")
        self.btn_importer = QPushButton("Importer")
        self.btn_exporter = QPushButton("Exporter")

        layout_accueil.addWidget(self.btn_enregistrer)
        layout_accueil.addWidget(self.btn_importer)
        layout_accueil.addWidget(self.btn_exporter)

        layout_accueil.addStretch()

        self.onglet_accueil.setLayout(layout_accueil)

        # Ajout du bouton "Classer" dans le coin supérieur droit
        btn_classer = QPushButton("Classer")
        btn_classer.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 4px 20px; font-weight: bold; margin-right: 5px;")

        # Placement spécifique du bouton dans l'espace vide à côté des onglets
        self.ruban.setCornerWidget(btn_classer, Qt.Corner.TopRightCorner)

        # Ajout du ruban au layout principal
        self.layout_principal.addWidget(self.ruban)

        # Ligne de séparation
        line = QWidget()
        line.setFixedHeight(2)
        line.setStyleSheet("background-color: #cccccc;")
        self.layout_principal.addWidget(line)

        # Le Tableau Final (Initialisé vide, rempli à l'étape 4)
        self.table_finale = QTableWidget()
        self.layout_principal.addWidget(self.table_finale)

        self.stacked_widget.addWidget(self.page_principale)
    def generer_interface_principale(self):
        nb_colonnes = 2 + len(self.matieres)
        nb_lignes = 2 + len(self.eleves)  # 2 lignes d'en-tête (ligne0, ligne1) + les élèves

        self.table_finale.clear()
        self.table_finale.setRowCount(nb_lignes)
        self.table_finale.setColumnCount(nb_colonnes)
        self.table_finale.verticalHeader().setVisible(False)
        self.table_finale.horizontalHeader().setVisible(False)

        # Ligne 0 : Liste des matières centrée
        item_titre = QTableWidgetItem("Liste des Matières")
        item_titre.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_finale.setItem(0, 2, item_titre)

        # Fusion des cellules (row, col, rowSpan, colSpan)
        if len(self.matieres) > 1:
            self.table_finale.setSpan(0, 2, 1, len(self.matieres))

        # Ligne 1 : En-têtes (Nom, Genre, puis les matières)
        self.table_finale.setItem(1, 0, QTableWidgetItem("Nom de l'élève"))
        self.table_finale.setItem(1, 1, QTableWidgetItem("Genre"))

        for col, matiere in enumerate(self.matieres, start=2):
            self.table_finale.setItem(1, col, QTableWidgetItem(matiere))

        # Styliser les lignes 0 et 1 pour les démarquer en tant qu'en-têtes
        for r in [0, 1]:
            for c in range(nb_colonnes):
                item = self.table_finale.item(r, c)
                if item:
                    item.setBackground(Qt.GlobalColor.lightGray)
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)

        # Remplissage des données des élèves (à partir de la ligne 2)
        for r, eleve in enumerate(self.eleves, start=2):
            item_nom = QTableWidgetItem(eleve['nom'])
            item_nom.setFlags(item_nom.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Lecture seule

            # Reprise de la mise en forme conditionnelle pour le tableau final
            if eleve['genre'] == "Fille":
                font = item_nom.font()
                font.setBold(True)
                item_nom.setFont(font)

            item_genre = QTableWidgetItem(eleve['genre'])
            item_genre.setFlags(item_genre.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Lecture seule

            self.table_finale.setItem(r, 0, item_nom)
            self.table_finale.setItem(r, 1, item_genre)

            # Les cellules de la plage à droite (notes) sont laissées vides et modifiables
            for c in range(2, nb_colonnes):
                self.table_finale.setItem(r, c, QTableWidgetItem(""))

        self.table_finale.resizeColumnsToContents()
        self.table_finale.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestionElevesApp()
    window.show()
    sys.exit(app.exec())