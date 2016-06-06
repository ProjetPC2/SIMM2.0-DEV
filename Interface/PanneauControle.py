# Fenetre panneau de controle du logiciel SIMM 2.0

#importation pour une fenetre simple
from AjouterEquipementFenetre import *
from ConsultationModificationEquipementFenetre import *
from RechercheBdT import RechercheBdT
from RechercherEquipementFenetre import *
from StatistiqueFenetre import *
from SupportFenetre import *


class Main(QDialog):

    def __init__(self):
        super().__init__()
        #creation des variables pour les differentes fenetres
        # self.ajouterEquipement = None
        # self.ajouterBdT = None
        # self.consulterModifierEquipement = None
        # self.rechercherEquipement = None
        # self.rechercheBdT = None
        # self.statistique = None
        self.listeBouton = list()
        self.initUI()



    def initUI(self):
        # self.ajoutEquipement = AjoutEquipement()

        #les boutons
        AddEq_Btn= QPushButton('Ajouter un \néquipement', self)
        AddEq_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        AddEq_Btn.move(75,150)
        AddEq_Btn.resize(150,100)
        AddEq_Btn.setIcon(QIcon('Images/PdC-Bouton_Ajouter.png'))
        AddEq_Btn.setIconSize(QtCore.QSize(40, 40))
        AddEq_Btn.clicked.connect(self.AddEqForm)
        AddEq_Btn.setObjectName("AddEq_Btn")


        AddBTD_Btn = QPushButton('Ajouter un \nbon de travail', self)
        AddBTD_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        AddBTD_Btn.move(250,150)
        AddBTD_Btn.resize(150, 100)
        AddBTD_Btn.setIcon(QIcon('Images/PdC_Bouton_BdT2.png'))
        AddBTD_Btn.setIconSize(QtCore.QSize(40, 40))
        AddBTD_Btn.clicked.connect(self.ouvrirFenetreAjoutBdT)
        AddBTD_Btn.setObjectName("AddBTD_Btn")


        ConsulterEq_Btn = QPushButton('Consulter ou \nmodifier \nun équipement', self)
        ConsulterEq_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        ConsulterEq_Btn.move(75, 300)
        ConsulterEq_Btn.resize(150,100)
        ConsulterEq_Btn.setIcon(QIcon('Images/PdC-crayon.png'))
        ConsulterEq_Btn.setIconSize(QtCore.QSize(40, 40))
        ConsulterEq_Btn.clicked.connect(self.ouvrirFenetreConsultationEquipement)
        ConsulterEq_Btn.setObjectName("ConsulterEq_Btn")


        SeachEq_Btn = QPushButton('Rechercher un \néquipement', self)
        SeachEq_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        SeachEq_Btn.move(250, 300)
        SeachEq_Btn.resize(150,100)
        SeachEq_Btn.setIcon(QIcon('Images/PdC_Bouton_Rechercher2.png'))
        SeachEq_Btn.setIconSize(QtCore.QSize(40,40))
        SeachEq_Btn.clicked.connect(self.ouvrirFenetreRechercheEquipement)
        SeachEq_Btn.setObjectName("SeachEq_Btn")

        SeachBDT_Btn = QPushButton('Rechercher un\nbon de travail', self)
        SeachBDT_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        SeachBDT_Btn.move(75, 450)
        SeachBDT_Btn.setMaximumSize(300, 300)
        SeachBDT_Btn.setIcon(QIcon('Images/PdC-Bouton_Recherche_BdT.png'))
        SeachBDT_Btn.setIconSize(QtCore.QSize(40,40))
        SeachBDT_Btn.setObjectName("SeachBDT_Btn")
        SeachBDT_Btn.clicked.connect(self.ouvrirRechercheBdT)

        Stats_Btn = QPushButton('Voir les \nstatistiques', self)
        Stats_Btn.setFont(QFont('SansSerif', 8, QFont.Bold))
        Stats_Btn.move(250, 450)
        Stats_Btn.setMaximumSize(300, 300)
        Stats_Btn.setIcon(QIcon('Images/PdC-Bouton-stats.png'))
        Stats_Btn.setIconSize(QtCore.QSize(40,40))
        Stats_Btn.clicked.connect(self.ouvrirStatistique)
        Stats_Btn.setObjectName("Stats_Btn")

        SupportPC2_Btn = QPushButton('Support \n technique', self)
        SupportPC2_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        SupportPC2_Btn.move(480,390)
        SupportPC2_Btn.setMaximumSize(300, 300)
        SupportPC2_Btn.setIcon(QIcon('Images/PC2.png'))
        SupportPC2_Btn.setIconSize(QtCore.QSize(150,150))
        # SupportPC2_Btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        SupportPC2_Btn.clicked.connect(self.ouvrirFenetreSupport)
        SupportPC2_Btn.setObjectName("SupportPC2_Btn")

        PrintInventaire_Btn = QPushButton('Imprimer l"inventaire', self)
        PrintInventaire_Btn.setFont(QFont( 'SansSerif', 8, QFont.Bold ))
        PrintInventaire_Btn.move(450, 150)
        PrintInventaire_Btn.resize(210, 70)
        PrintInventaire_Btn.setObjectName("PrintInventaire_Btn")

        #initialisation  fenetre du panneau de controle
        #Les déclaration des écritures dans la fenetre
        self.textTitre = QLabel("S.I.M.M. 2.0 <br> <u>Hôpital Saint-Michel</u>  ")
        self.textTitre.setStyleSheet("color: white")
        self.textTitre.setFont(QFont('Cambria', 24))
        self.textTitre.setAlignment(Qt.AlignHCenter)
        self.textTitre.wordWrap()

        self.textRemarque = QLabel("S.I.M.M : Système d'Inventorisation du Matériel Médical")
        self.textRemarque.setStyleSheet("color: white")
        self.textRemarque.setFont(QFont('Cambria', 12 ))
        self.textRemarque.setAlignment(Qt.AlignBottom)
        self.textRemarque.setAlignment(Qt.AlignCenter)

        #Size of the window
        self.setGeometry(400, 175, 720, 700)
        self.setWindowTitle('SIMM 2.0 : Panneau de controle')
        self.setWindowIcon(QIcon('Images/PC2.png'))


        layoutFond = QVBoxLayout()
        layoutConteneur = QHBoxLayout()
        layoutHorizontalGauche = QVBoxLayout()
        layoutHorizontalCentre = QVBoxLayout()
        layoutHorizontalDroit = QVBoxLayout()

        layoutHorizontalGauche.addWidget(AddEq_Btn)
        layoutHorizontalGauche.addWidget(ConsulterEq_Btn)
        layoutHorizontalGauche.addWidget(SeachBDT_Btn)

        layoutHorizontalCentre.addWidget(AddBTD_Btn)
        layoutHorizontalCentre.addWidget(SeachEq_Btn)
        layoutHorizontalCentre.addWidget(Stats_Btn)

        layoutHorizontalDroit.addWidget(PrintInventaire_Btn)
        layoutHorizontalDroit.addWidget(SupportPC2_Btn)

        layoutConteneur.addLayout(layoutHorizontalGauche)
        layoutConteneur.addLayout(layoutHorizontalCentre)
        layoutConteneur.addLayout(layoutHorizontalDroit)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem1 = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layoutFond.addWidget(self.textTitre)
        layoutFond.addItem(spacerItem1)

        layoutFond.addLayout(layoutConteneur)
        layoutFond.addItem(spacerItem)

        layoutFond.addWidget(self.textRemarque)

        layoutFond.addItem(spacerItem)


        #Définir la couleur de l'arriere plan de la fenêtre principale
        self.setObjectName("PanneauControle")
        self.setLayout(layoutFond)
        self.setStyleSheet((open("style.qss", "r").read()))
        backG = self.palette()
        backG.setColor(self.backgroundRole(), Qt.darkBlue)
        self.setPalette(backG)
        self.setMaximumSize(1500,1000)
        self.show()

    #declaration du  texte principal (titre) de la fenetre
    def paintEvent(self, event):

        mainTitle = QPainter()
        mainTitle.begin(self)
        self.drawText(event, mainTitle)
        mainTitle.end()

        remarque = QPainter()
        remarque.begin(self)
        self.DessinText(event, remarque)
        remarque.end()

        ligne = QPainter()
        ligne.begin(self)
        self.drawLines(event, ligne)
        ligne.end()

    #Mise en forme du texte principal (titre) de la fenetre
    def drawText (self, event, mainTitle):
         mainTitle.setPen(QColor(Qt.white))
         mainTitle.setFont(QFont('Cambria', 24))
         # mainTitle.drawText(event.rect(), Qt.AlignHCenter, self.textTitre)


    # Mise en forme du texte principal (titre) de la fenetre
    def DessinText(self, event, remarque):
        remarque.setPen(QColor(Qt.white))
        remarque.setFont(QFont('Cambria', 12 ))
        # remarque.drawText(event.rect(), Qt.AlignBottom, self.textRemarque)


    def drawLines(self, event, ligne):
          pen = QPen(Qt.white, 1, Qt.SolidLine)
          ligne.setPen(pen)
          # ligne.drawLine(200,200, 600,200)
          # ligne.drawLine(190, 100, 540, 100)

    def AddEqForm(self):
        # self.hide()
        # AjoutEquipement(self).show()
        # self.ajouterEquipement = MainWindow()
        # self.ajouterEquipement.show()
        # self.listeBouton.append(MainWindow())
        # self.listeBouton[0].show()
        self.estPresent(AjouterEquipementFenetre(self))

    def ouvrirFenetreAjoutBdT(self):
        # self.ajouterBdT = BonDeTravailFenetre()
        # self.ajouterBdT.show()
        # self.ajouterEquipement.hide()
        self.estPresent(BonDeTravailFenetre(self), 1)

    def ouvrirFenetreConsultationEquipement(self):
        # self.consulterModifierEquipement = ConsultationModificationEquipement()
        # self.consulterModifierEquipement.show()
        self.estPresent(ConsultationModificationEquipement())

    def ouvrirFenetreRechercheEquipement(self):
        # self.rechercherEquipement = rechercheEquipement()
        # self.rechercherEquipement.show()
        self.estPresent(RerchercherEquipementFenetre())

    def ouvrirFenetreSupport(self):
        # self.rechercherEquipement = rechercheEquipement()
        # self.rechercherEquipement.show()
        self.estPresent(Support(self))

    def ouvrirStatistique(self):
        self.estPresent(Statistique(self))

    def ouvrirRechercheBdT(self):
        self.estPresent(RechercheBdT())

    def estPresent(self,type, fenetre = 0):
        present = False
        indice = 0
        for bouton in self.listeBouton:
            if bouton is type:
                present = True
                indice += 1
                break
            indice += 1
        if not present:
            self.listeBouton.append(type)
        self.listeBouton[indice].show()
        if fenetre == 0:
            self.listeBouton[indice].center()

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # self.move(qr.center)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.center()
    sys.exit(app.exec_())

