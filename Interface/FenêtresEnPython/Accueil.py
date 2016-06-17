# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlPannel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Interface.FenêtresEnPython import BonDeTravail
from Interface.FenêtresEnPython.AjoutEquipement import AjoutEquipementUI
from Interface.FenêtresEnPython.BonDeTravail import BonDeTravailUI
from Interface.FenêtresEnPython.ConsultationEquipement import ConsultationEquipementUI
from Interface.FenêtresEnPython.ModificationEquipement import ModificationEquipementUI
from Interface.FenêtresEnPython.RechercheBonDeTravail import RechercheBonDeTravailUI
from Interface.FenêtresEnPython.RechercheEquipement import RechercheEquipementUI
from Interface.FenêtresEnPython.StatistiqueFenetre import Statistique
from Interface.FenêtresEnPython.SupportPC2 import SupportPC2UI


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1725, 1283)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #85cafc, stop: 1  #36357F);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layoutHorizontalPrincipal = QtWidgets.QHBoxLayout()
        self.layoutHorizontalPrincipal.setObjectName("layoutHorizontalPrincipal")
        self.layoutBouton = QtWidgets.QVBoxLayout()
        self.layoutBouton.setObjectName("layoutBouton")
        self.layoutBoutonEquipement = QtWidgets.QVBoxLayout()
        self.layoutBoutonEquipement.setObjectName("layoutBoutonEquipement")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem1)
        self.BoutonAjouterEquipement = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BoutonAjouterEquipement.setFont(font)
        self.BoutonAjouterEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonAjouterEquipement.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/plus (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterEquipement.setIcon(icon)
        self.BoutonAjouterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterEquipement.setFlat(False)
        self.BoutonAjouterEquipement.setObjectName("BoutonAjouterEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonAjouterEquipement)
        self.BoutonModifierConsulterEquipement = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonModifierConsulterEquipement.setFont(font)
        self.BoutonModifierConsulterEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonModifierConsulterEquipement.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/pencil-edit-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonModifierConsulterEquipement.setIcon(icon1)
        self.BoutonModifierConsulterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonModifierConsulterEquipement.setObjectName("BoutonModifierConsulterEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonModifierConsulterEquipement)
        self.BoutonRechercherEquipement = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)


        self.BoutonRechercherEquipement.setFont(font)
        self.BoutonRechercherEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonRechercherEquipement.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherEquipement.setIcon(icon2)
        self.BoutonRechercherEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherEquipement.setObjectName("BoutonRechercherEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonRechercherEquipement)
        self.layoutBouton.addLayout(self.layoutBoutonEquipement)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem2)
        self.layoutBoutonBdT = QtWidgets.QVBoxLayout()
        self.layoutBoutonBdT.setObjectName("layoutBoutonBdT")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonBdT.addItem(spacerItem3)
        self.BoutonRechercherBonTravail = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonRechercherBonTravail.setFont(font)
        self.BoutonRechercherBonTravail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonRechercherBonTravail.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/magnifier (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherBonTravail.setIcon(icon3)
        self.BoutonRechercherBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherBonTravail.setObjectName("BoutonRechercherBonTravail")
        self.BoutonAjouterBonTravail = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)


        self.BoutonAjouterBonTravail.setFont(font)
        self.BoutonAjouterBonTravail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonAjouterBonTravail.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterBonTravail.setIcon(icon4)
        self.BoutonAjouterBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterBonTravail.setObjectName("BoutonAjouterBonTravail")
        self.layoutBoutonBdT.addWidget(self.BoutonAjouterBonTravail)

        self.layoutBoutonBdT.addWidget(self.BoutonRechercherBonTravail)


        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonBdT.addItem(spacerItem4)
        self.layoutBouton.addLayout(self.layoutBoutonBdT)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem5)
        self.layoutBoutonExtra = QtWidgets.QVBoxLayout()
        self.layoutBoutonExtra.setObjectName("layoutBoutonExtra")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem6)
        self.BoutonImprimerInventaire = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonImprimerInventaire.setFont(font)
        self.BoutonImprimerInventaire.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonImprimerInventaire.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/printer- (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonImprimerInventaire.setIcon(icon5)
        self.BoutonImprimerInventaire.setIconSize(QtCore.QSize(40, 40))
        self.BoutonImprimerInventaire.setObjectName("BoutonImprimerInventaire")
        self.layoutBoutonExtra.addWidget(self.BoutonImprimerInventaire)
        self.BoutonStatistiques = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonStatistiques.setFont(font)
        self.BoutonStatistiques.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonStatistiques.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Images/pie-chart (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonStatistiques.setIcon(icon6)
        self.BoutonStatistiques.setIconSize(QtCore.QSize(40, 40))
        self.BoutonStatistiques.setObjectName("BoutonStatistiques")
        self.layoutBoutonExtra.addWidget(self.BoutonStatistiques)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem7)
        self.layoutBouton.addLayout(self.layoutBoutonExtra)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem9)
        self.layoutBoutonSupport = QtWidgets.QVBoxLayout()
        self.layoutBoutonSupport.setObjectName("layoutBoutonSupport")
        self.BoutonSuportTecnique = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonSuportTecnique.setFont(font)
        self.BoutonSuportTecnique.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonSuportTecnique.setStyleSheet("QPushButton{ padding : 20px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Images/PC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonSuportTecnique.setIcon(icon7)
        self.BoutonSuportTecnique.setIconSize(QtCore.QSize(40, 40))
        self.BoutonSuportTecnique.setAutoDefault(False)
        self.BoutonSuportTecnique.setDefault(False)
        self.BoutonSuportTecnique.setFlat(False)
        self.BoutonSuportTecnique.setObjectName("BoutonSuportTecnique")
        self.layoutBoutonSupport.addWidget(self.BoutonSuportTecnique)
        self.layoutBouton.addLayout(self.layoutBoutonSupport)
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem10)
        self.layoutHorizontalPrincipal.addLayout(self.layoutBouton)
        self.layoutAffichagePrincipal = QtWidgets.QVBoxLayout()
        self.layoutAffichagePrincipal.setObjectName("layoutAffichagePrincipal")
        self.LabelSIMM20HopitalSaintMichel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSIMM20HopitalSaintMichel.setFont(font)
        self.LabelSIMM20HopitalSaintMichel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LabelSIMM20HopitalSaintMichel.setStyleSheet("\n"
"color: white;\n"
"\n"
" background-color: transparent ;")
        self.LabelSIMM20HopitalSaintMichel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LabelSIMM20HopitalSaintMichel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LabelSIMM20HopitalSaintMichel.setObjectName("LabelSIMM20HopitalSaintMichel")
        self.layoutAffichagePrincipal.addWidget(self.LabelSIMM20HopitalSaintMichel)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.layoutAffichagePrincipal.addWidget(self.graphicsView)


        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutAffichagePrincipal.addItem(spacerItem11)
        self.LabelDefinitionSIMM = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LabelDefinitionSIMM.setFont(font)
        self.LabelDefinitionSIMM.setStyleSheet("\n"
"color: white;\n"
"\n"
" background-color: transparent ;")
        self.LabelDefinitionSIMM.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelDefinitionSIMM.setObjectName("LabelDefinitionSIMM")
        self.layoutAffichagePrincipal.addWidget(self.LabelDefinitionSIMM)
        self.layoutHorizontalPrincipal.addLayout(self.layoutAffichagePrincipal)
        self.gridLayout_2.addLayout(self.layoutHorizontalPrincipal, 0, 0, 1, 1)

        #Pour enlever les marges de la fenetre
        self.gridLayout_2.setContentsMargins(0,0,0,0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BoutonAjouterEquipement.setText(_translate("MainWindow", "Ajouter un\n"
"équipement"))
        self.BoutonModifierConsulterEquipement.setText(_translate("MainWindow", "Modifier ou\n"
"consulter\n"
"un équipement"))
        self.BoutonRechercherEquipement.setText(_translate("MainWindow", "Rechercher un\n"
"équipement"))
        self.BoutonRechercherBonTravail.setText(_translate("MainWindow", "Rechercher un\n"
"bon de travail"))
        self.BoutonAjouterBonTravail.setText(_translate("MainWindow", "Ajouter un bon\n"
"de travail"))
        self.BoutonImprimerInventaire.setText(_translate("MainWindow", "Imprimer tout\n"
"l\'inventaire"))
        self.BoutonStatistiques.setText(_translate("MainWindow", "Voir les\n"
"statistiques"))
        self.BoutonSuportTecnique.setText(_translate("MainWindow", "Support\n"
"technique"))
        self.LabelSIMM20HopitalSaintMichel.setText(_translate("MainWindow", "S.I.M.M. 2.0\n"
"Hôpital Saint-Michel "))
        # self.LabelSIMM20HopitalSaintMichel.hide()
        self.LabelDefinitionSIMM.setText(_translate("MainWindow", "S.I.M.M. : Système d\'Inventorisation du Matériel Médical "))

        #Creation d'une liste pour le contenu par defaut
        self.listeElementParDefaut = list()
        self.listeElementParDefaut.append(self.LabelSIMM20HopitalSaintMichel)
        # Rajouter le logo de SIMM
        self.listeElementParDefaut.append(self.graphicsView)
        self.listeElementParDefaut.append(self.LabelDefinitionSIMM)

        self.ajoutEquipement = QtWidgets.QWidget()
        self.ajoutEquipementUI = AjoutEquipementUI()
        self.ajoutEquipementUI.setupUi(self.ajoutEquipement)

        self.BoutonAjouterEquipement.clicked.connect(self.afficherAjoutEquipement)
        self.BoutonModifierConsulterEquipement.clicked.connect(self.afficherConsultationEquipement)
        self.BoutonRechercherEquipement.clicked.connect(self.afficherRechercheEquipement)


        self.ajoutEquipement = None
        self.consultationEquipement = None
        self.rechercheEquipement = None
        self.modificationEquipement = None

        self.ajoutBonDeTravail = None
        self.rechercheBonDeTravail = None

        self.BoutonAjouterBonTravail.clicked.connect(self.afficherAjoutBonDeTravail)
        self.BoutonRechercherBonTravail.clicked.connect(self.afficherRechercheBonDeTravail)

        self.statistique = None
        self.BoutonStatistiques.clicked.connect(self.afficherStatistique)

        self.support = None
        self.BoutonSuportTecnique.clicked.connect(self.afficherSupport)


    def connectionBouton(self):
        #Connection a faire
        self.BoutonAjouterEquipement.clicked.connect(self.afficherAjoutEquipement)
        self.BoutonModifierConsulterEquipement.clicked.connect(self.afficherConsultationEquipement)
        self.BoutonRechercherEquipement.clicked.connect(self.afficherRechercheEquipement)

        self.BoutonAjouterBonTravail.clicked.connect(self.afficherAjoutBonDeTravail)
        self.BoutonRechercherBonTravail.clicked.connect()

        self.BoutonImprimerInventaire.clicked.connect()
        self.BoutonStatistiques.clicked.connect()

        self.BoutonSuportTecnique.clicked.connect(self.afficherSupport)

    def afficherAjoutEquipement(self):
        print("Appuie sur bouton Ajouter Equipement")
        self.masquerElementGraphique()

        if self.ajoutEquipement is None :
            self.ajoutEquipement = QtWidgets.QWidget()
            self.ajoutEquipementUI = AjoutEquipementUI()
            self.ajoutEquipementUI.setupUi(self.ajoutEquipement)
            self.ajoutEquipement.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.ajoutEquipement)
            self.layoutAffichagePrincipal.addWidget(self.ajoutEquipement)
        else:
            self.ajoutEquipement.show()

    def afficherConsultationEquipement(self):
        print("Appuie sur bouton Consultation Equipement")
        self.masquerElementGraphique()
        if self.consultationEquipement is None:
            self.consultationEquipement = QtWidgets.QWidget()
            self.consultationEquipementUI = ConsultationEquipementUI()
            self.consultationEquipementUI.setupUi(self.consultationEquipement)
            self.consultationEquipement.setStyleSheet("background: white;")

            self.consultationEquipementUI.boutonModifierEquipement.clicked.connect(self.modifierEquipement)

            self.listeElementParDefaut.append(self.consultationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.consultationEquipement)
        else:
            self.consultationEquipement.show()

    def afficherRechercheEquipement(self):
        print("Appuie sur bouton Recherche Equipement")
        self.masquerElementGraphique()
        if self.rechercheEquipement is None:
            self.rechercheEquipement = QtWidgets.QWidget()
            self.rechercheEquipementUI = RechercheEquipementUI()
            self.rechercheEquipementUI.setupUi(self.rechercheEquipement)
            self.rechercheEquipement.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.rechercheEquipement)
            self.layoutAffichagePrincipal.addWidget(self.rechercheEquipement)
        else:
            self.rechercheEquipement.show()


    def afficherAjoutBonDeTravail(self):
        print("Appuie sur bouton ajout Equipement")
        self.masquerElementGraphique()
        if self.ajoutBonDeTravail is None:
            self.ajoutBonDeTravail = QtWidgets.QWidget()
            self.bonDeTravailUI = BonDeTravailUI()
            self.bonDeTravailUI.setupUi(self.ajoutBonDeTravail)
            self.ajoutBonDeTravail.setStyleSheet("background: white;")


            self.listeElementParDefaut.append(self.ajoutBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.ajoutBonDeTravail)
        else:
            self.ajoutBonDeTravail.show()

    def afficherRechercheBonDeTravail(self):
        print("Appuie sur bouton ajout RechercheBonDeTravail")
        self.masquerElementGraphique()
        if self.rechercheBonDeTravail is None:
            self.rechercheBonDeTravail = QtWidgets.QWidget()
            self.rechercheBonDeTravailUI = RechercheBonDeTravailUI()
            self.rechercheBonDeTravailUI.setupUi(self.rechercheBonDeTravail)
            self.rechercheBonDeTravail.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.rechercheBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.rechercheBonDeTravail)
        else:
            self.rechercheBonDeTravail.show()

    def afficherStatistique(self):
        print("Appuie sur bouton ajout Statistique")
        self.masquerElementGraphique()

        if self.statistique is None:

            self.statistique = QtWidgets.QWidget()
            statistique = Statistique(self.statistique)
            self.statistique.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.statistique)
            self.layoutAffichagePrincipal.addWidget(self.statistique)
        else:
            self.statistique.show()


    def afficherSupport(self):
        print("Appuie sur bouton ajout Support")
        self.masquerElementGraphique()
        if self.support is None:
            self.support = QtWidgets.QWidget()
            self.supportPC2UI = SupportPC2UI()
            self.supportPC2UI.setupUi(self.support)
            self.support.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.support)
            self.layoutAffichagePrincipal.addWidget(self.support)
        else:
            self.support.show()

    def masquerElementGraphique(self):
        for elementGraphique in self.listeElementParDefaut:
            elementGraphique.hide()

    def modifierEquipement(self):
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.modificationEquipement is None:
            self.modificationEquipement = QtWidgets.QWidget()
            self.modificationEquipementUI = ModificationEquipementUI()
            self.modificationEquipementUI.setupUi(self.modificationEquipement, equipement)
            self.modificationEquipement.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.modificationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipement)
        else:
            self.modificationEquipement.show()
            self.modificationEquipementUI.equipementRecherche = equipement
            self.modificationEquipementUI.remplirEquipement()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
