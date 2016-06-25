# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlPannel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

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
        self.LabelDefinitionSIMM.setText(_translate("MainWindow", "S.I.M.M. : Système d\'Inventorisation du Matériel Médical "))

        self.ajoutAccueil()

    def ajoutAccueil(self):
        '''
            Ajout des differents elements a la page d'accueil
            :param:
            :return:
        '''
        #Creation d'une liste contenant les elements destines
        #A l'affichage dans la partie centrale
        self.listeElementParDefaut = list()
        self.listeElementParDefaut.append(self.LabelSIMM20HopitalSaintMichel)
        # Rajouter le logo de SIMM
        self.listeElementParDefaut.append(self.graphicsView)
        self.listeElementParDefaut.append(self.LabelDefinitionSIMM)

        #Connexion des actions aux cliques des boutons de la partie Equipement
        self.BoutonAjouterEquipement.clicked.connect(self.afficherAjoutEquipement)
        self.BoutonModifierConsulterEquipement.clicked.connect(self.afficherConsultationEquipement)
        self.BoutonRechercherEquipement.clicked.connect(self.afficherRechercheEquipement)

        #Creation des differents conteneur pour les widgets a afficher
        #Partie Equipement
        self.ajoutEquipement = None
        self.consultationEquipement = None
        self.rechercheEquipement = None
        self.modificationEquipement = None
        #Partie Bon de Travail
        self.ajoutBonDeTravail = None
        self.rechercheBonDeTravail = None
        self.modificationEquipementRecherche = None
        #Connexion des actions aux cliques des boutons de la partie Bon de Travail
        self.BoutonAjouterBonTravail.clicked.connect(self.afficherAjoutBonDeTravail)
        self.BoutonRechercherBonTravail.clicked.connect(self.afficherRechercheBonDeTravail)

        #Creation du conteneur de la page statistique
        self.statistique = None
        # self.BoutonStatistiques.clicked.connect(self.afficherStatistique)

        #Creation de la partie Support
        self.support = None
        self.BoutonSuportTecnique.clicked.connect(self.afficherSupport)


    def connectionBouton(self):
        '''
            Methode qui va faire la connection des differents boutons
            :param:
            :return:
        '''
        self.BoutonAjouterEquipement.clicked.connect(self.afficherAjoutEquipement)
        self.BoutonModifierConsulterEquipement.clicked.connect(self.afficherConsultationEquipement)
        self.BoutonRechercherEquipement.clicked.connect(self.afficherRechercheEquipement)

        self.BoutonAjouterBonTravail.clicked.connect(self.afficherAjoutBonDeTravail)
        self.BoutonRechercherBonTravail.clicked.connect()

        self.BoutonImprimerInventaire.clicked.connect()
        self.BoutonStatistiques.clicked.connect()

        self.BoutonSuportTecnique.clicked.connect(self.afficherSupport)

    def afficherAjoutEquipement(self):
        '''
            Affichage du widget permet l'ajout d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        #On masque les autres elements
        self.masquerElementGraphique()

        if self.ajoutEquipement is None :
            #Creation du widget s'il n'existe pas deja
            self.ajoutEquipement = QtWidgets.QWidget()
            self.ajoutEquipementUI = AjoutEquipementUI()
            self.ajoutEquipementUI.setupUi(self.ajoutEquipement)
            self.ajoutEquipement.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.ajoutEquipement)
            self.layoutAffichagePrincipal.addWidget(self.ajoutEquipement)
        else:
            #Affichage du widget s'il existe deja
            self.ajoutEquipement.show()

    def afficherConsultationEquipement(self):
        '''
            Affichage du widget permet la consultation d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.consultationEquipement is None:
            #Creation du widget s'il n'existe pas encore
            self.consultationEquipement = QtWidgets.QWidget()
            self.consultationEquipementUI = ConsultationEquipementUI()
            self.consultationEquipementUI.setupUi(self.consultationEquipement)
            self.consultationEquipement.setStyleSheet("background: white;")

            #connexion de l'action a l'appuye du bouton modification equipement
            self.consultationEquipementUI.boutonModifierEquipement.clicked.connect(self.modifierEquipement)

            self.listeElementParDefaut.append(self.consultationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.consultationEquipement)
        else:
            #Affichage de l'element s'il existe deja
            self.consultationEquipement.show()

    def afficherRechercheEquipement(self):
        '''
            Affichage du widget permet la recherche d'un equipement
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.rechercheEquipement is None:
            #Creation du widget s'il n'existe pas
            self.rechercheEquipement = QtWidgets.QWidget()
            self.rechercheEquipementUI = RechercheEquipementUI()
            self.rechercheEquipementUI.setupUi(self.rechercheEquipement)
            self.rechercheEquipement.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.rechercheEquipement)
            self.layoutAffichagePrincipal.addWidget(self.rechercheEquipement)
            self.rechercheEquipementUI.tableResultats.doubleClicked.connect(self.choisirEquipement)
        else:
            #Affichage du widget s'il existe deja
            self.rechercheEquipement.show()

    def choisirEquipement(self):
        # print("ligne", ligne)
        # print("colonne", colonne)
        # print(self.tableResultats.item(ligne, 0).data(0))
        # equipement = dict()
        # indice = 0
        # for cle in self.listeCleDonnees:
        #     if (cle == "ID"):
        #         equipement[cle] = int(self.tableResultats.item(ligne, indice).data(0))
        #     elif cle == "DateAcquisition" or cle == "DateDernierEntretien":
        #         equipement[cle] = datetime.datetime.strptime(self.tableResultats.item(ligne, indice).data(0),
        #                                                      '%Y-%m-%d')
        #     else:
        #         equipement[cle] = self.tableResultats.item(ligne, indice).data(0)
        #     indice += 1
        # On masque les autres elements
        self.masquerElementGraphique()
        equipement = self.rechercheEquipementUI.equipementSelectionne
        if self.modificationEquipementRecherche is None:
            # Creation du widget s'il n'existe pas
            self.modificationEquipementRecherche = QtWidgets.QWidget()
            self.modificationEquipementRechercheUI = ModificationEquipementUI()
            self.modificationEquipementRechercheUI.setupUi(self.modificationEquipementRecherche, equipement)
            self.modificationEquipementRecherche.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.modificationEquipementRecherche)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipementRecherche)
        else:
            # Affichage du widget s'il existe deja
            self.modificationEquipementRecherche.show()
            self.modificationEquipementRechercheUI.equipementRecherche = equipement
            self.modificationEquipementRechercheUI.remplirEquipement()

    def afficherAjoutBonDeTravail(self):
        '''
            Affichage du widget permet l'ajout d'un bon de travail
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.ajoutBonDeTravail is None:
            #Creation du widget s'il n'existe pas
            self.ajoutBonDeTravail = QtWidgets.QWidget()
            self.bonDeTravailUI = BonDeTravailUI()
            self.bonDeTravailUI.setupUi(self.ajoutBonDeTravail)
            self.ajoutBonDeTravail.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.ajoutBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.ajoutBonDeTravail)
        else:
            #Affichage de l'element s'il existe deja
            self.ajoutBonDeTravail.show()

    def afficherRechercheBonDeTravail(self):
        '''
            Affichage du widget permet la recherche d'un bon de travail
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.rechercheBonDeTravail is None:
            #Creation du widget s'il n'existe pas
            self.rechercheBonDeTravail = QtWidgets.QWidget()
            self.rechercheBonDeTravailUI = RechercheBonDeTravailUI()
            self.rechercheBonDeTravailUI.setupUi(self.rechercheBonDeTravail)
            self.rechercheBonDeTravail.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.rechercheBonDeTravail)
            self.layoutAffichagePrincipal.addWidget(self.rechercheBonDeTravail)
        else:
            #Affichage du widget s'il existe deja
            self.rechercheBonDeTravail.show()

    def afficherStatistique(self):
        '''
            Affichage du widget Statistique
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()

        if self.statistique is None:
            #Creation du widget Statistique s'il n'existe pas
            self.statistique = QtWidgets.QWidget()
            statistique = Statistique(self.statistique)
            self.statistique.setStyleSheet("background: white;")
            self.listeElementParDefaut.append(self.statistique)
            self.layoutAffichagePrincipal.addWidget(self.statistique)
        else:
            #Affichage du widget s'il existe deja
            self.statistique.show()


    def afficherSupport(self):
        '''
            Affichage du widget Support
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        if self.support is None:
            #Creation du widget support s'il n'existe pas
            self.support = QtWidgets.QWidget()
            self.supportPC2UI = SupportPC2UI()
            self.supportPC2UI.setupUi(self.support)
            self.support.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.support)
            self.layoutAffichagePrincipal.addWidget(self.support)
        else:
            #Affichage du widget support
            self.support.show()

    def masquerElementGraphique(self):
        '''
            Masquage les elements graphiques de listeELementParDefaut
            :param: None
            :return:
        '''
        # On masque les autres elements
        for elementGraphique in self.listeElementParDefaut:
            elementGraphique.hide()

    def modifierEquipement(self):
        '''
            Affichage du widget recapitulant l'equipement que l'on souhaite ajouter
            Masquage des autres elements graphiques de la partie principale
            :param: None
            :return:
        '''
        # On masque les autres elements
        self.masquerElementGraphique()
        equipement = self.consultationEquipementUI.equipement
        if self.modificationEquipement is None:
            #Creation du widget s'il n'existe pas
            self.modificationEquipement = QtWidgets.QWidget()
            self.modificationEquipementUI = ModificationEquipementUI()
            self.modificationEquipementUI.setupUi(self.modificationEquipement, equipement)
            self.modificationEquipement.setStyleSheet("background: white;")

            self.listeElementParDefaut.append(self.modificationEquipement)
            self.layoutAffichagePrincipal.addWidget(self.modificationEquipement)
        else:
            #Affichage du widget s'il existe deja
            self.modificationEquipement.show()
            self.modificationEquipementUI.equipementRecherche = equipement
            self.modificationEquipementUI.remplirEquipement()

class SIMM():
    '''
        Fonction de lancement de la page d'accueil de SIMM
        :param: None
        :return:
    '''
    # On masque les autres elements
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainFrame = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainFrame)
        MainFrame.show()
        sys.exit(app.exec_())
        os.system("pause")

if __name__ == "__main__":
    SIMM()

