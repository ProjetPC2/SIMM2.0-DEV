# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics

class Ui_Accueil(object):
    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.setWindowModality(QtCore.Qt.NonModal)
        Accueil.setEnabled(True)
        width = GetSystemMetrics(0)
        heigth = GetSystemMetrics(1)
        facteur_grandissement_width = 0.9
        facteur_grandissement_heigth = 0.7
        Accueil.resize(width * facteur_grandissement_width, heigth * facteur_grandissement_heigth)
        #Accueil.resize(1355, 689)
        # Accueil.resize(846, 729)
        Accueil.setMaximumSize(QtCore.QSize(11111112, 1111111))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        Accueil.setFont(font)
        Accueil.setStyleSheet("  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #85cafc, stop: 1  #36357F);")
        Accueil.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        Accueil.setWindowFilePath("")
        Accueil.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(2, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layoutHorizontalPrincipal = QtWidgets.QHBoxLayout()
        self.layoutHorizontalPrincipal.setSpacing(0)
        self.layoutHorizontalPrincipal.setObjectName("layoutHorizontalPrincipal")
        self.layoutBouton = QtWidgets.QVBoxLayout()
        self.layoutBouton.setObjectName("layoutBouton")
        self.layoutBoutonEquipement = QtWidgets.QVBoxLayout()
        self.layoutBoutonEquipement.setObjectName("layoutBoutonEquipement")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem1)
        self.BoutonAccueil = QtWidgets.QPushButton(self.centralwidget)
        self.BoutonAccueil.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonAccueil.setFont(font)
        self.BoutonAccueil.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAccueil.setIcon(icon)
        self.BoutonAccueil.setIconSize(QtCore.QSize(35, 35))
        self.BoutonAccueil.setObjectName("BoutonAccueil")
        self.layoutBoutonEquipement.addWidget(self.BoutonAccueil, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem2)
        self.BoutonAjouterEquipement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonAjouterEquipement.sizePolicy().hasHeightForWidth())
        self.BoutonAjouterEquipement.setSizePolicy(sizePolicy)
        self.BoutonAjouterEquipement.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/plus (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterEquipement.setIcon(icon1)
        self.BoutonAjouterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterEquipement.setFlat(False)
        self.BoutonAjouterEquipement.setObjectName("BoutonAjouterEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonAjouterEquipement, 0, QtCore.Qt.AlignLeft)
        self.BoutonModifierConsulterEquipement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonModifierConsulterEquipement.sizePolicy().hasHeightForWidth())
        self.BoutonModifierConsulterEquipement.setSizePolicy(sizePolicy)
        self.BoutonModifierConsulterEquipement.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/pencil-edit-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonModifierConsulterEquipement.setIcon(icon2)
        self.BoutonModifierConsulterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonModifierConsulterEquipement.setObjectName("BoutonModifierConsulterEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonModifierConsulterEquipement, 0, QtCore.Qt.AlignLeft)
        self.BoutonRechercherEquipement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonRechercherEquipement.sizePolicy().hasHeightForWidth())
        self.BoutonRechercherEquipement.setSizePolicy(sizePolicy)
        self.BoutonRechercherEquipement.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherEquipement.setIcon(icon3)
        self.BoutonRechercherEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherEquipement.setObjectName("BoutonRechercherEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonRechercherEquipement, 0, QtCore.Qt.AlignLeft)
        self.layoutBouton.addLayout(self.layoutBoutonEquipement)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem4)
        self.layoutBoutonBdT = QtWidgets.QVBoxLayout()
        self.layoutBoutonBdT.setObjectName("layoutBoutonBdT")
        self.BoutonAjouterPiece = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonAjouterPiece.sizePolicy().hasHeightForWidth())
        self.BoutonAjouterPiece.setSizePolicy(sizePolicy)
        self.BoutonAjouterPiece.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonAjouterPiece.setFont(font)
        self.BoutonAjouterPiece.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonAjouterPiece.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/piece_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterPiece.setIcon(icon4)
        self.BoutonAjouterPiece.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterPiece.setObjectName("BoutonAjouterPiece")
        self.layoutBoutonBdT.addWidget(self.BoutonAjouterPiece, 0, QtCore.Qt.AlignLeft)
        self.BoutonAjouterPiece.setEnabled(False)
        self.BoutonAjouterBonTravail = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonAjouterBonTravail.sizePolicy().hasHeightForWidth())
        self.BoutonAjouterBonTravail.setSizePolicy(sizePolicy)
        self.BoutonAjouterBonTravail.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterBonTravail.setIcon(icon5)
        self.BoutonAjouterBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterBonTravail.setObjectName("BoutonAjouterBonTravail")
        self.layoutBoutonBdT.addWidget(self.BoutonAjouterBonTravail, 0, QtCore.Qt.AlignLeft)
        self.BoutonRechercherBonTravail = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonRechercherBonTravail.sizePolicy().hasHeightForWidth())
        self.BoutonRechercherBonTravail.setSizePolicy(sizePolicy)
        self.BoutonRechercherBonTravail.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/magnifier (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherBonTravail.setIcon(icon6)
        self.BoutonRechercherBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherBonTravail.setObjectName("BoutonRechercherBonTravail")
        self.layoutBoutonBdT.addWidget(self.BoutonRechercherBonTravail, 0, QtCore.Qt.AlignLeft)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonBdT.addItem(spacerItem5)
        self.layoutBouton.addLayout(self.layoutBoutonBdT)
        self.layoutBoutonExtra = QtWidgets.QVBoxLayout()
        self.layoutBoutonExtra.setObjectName("layoutBoutonExtra")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem6)
        self.BoutonImprimerInventaire = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonImprimerInventaire.sizePolicy().hasHeightForWidth())
        self.BoutonImprimerInventaire.setSizePolicy(sizePolicy)
        self.BoutonImprimerInventaire.setMaximumSize(QtCore.QSize(350, 16777215))
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/printer- (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonImprimerInventaire.setIcon(icon7)
        self.BoutonImprimerInventaire.setIconSize(QtCore.QSize(40, 40))
        self.BoutonImprimerInventaire.setObjectName("BoutonImprimerInventaire")
        self.layoutBoutonExtra.addWidget(self.BoutonImprimerInventaire, 0, QtCore.Qt.AlignLeft)
        self.BoutonStatistiques = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonStatistiques.sizePolicy().hasHeightForWidth())
        self.BoutonStatistiques.setSizePolicy(sizePolicy)
        self.BoutonStatistiques.setMaximumSize(QtCore.QSize(350, 16777215))
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
        self.BoutonStatistiques.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images/pie-chart (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonStatistiques.setIcon(icon8)
        self.BoutonStatistiques.setIconSize(QtCore.QSize(40, 40))
        self.BoutonStatistiques.setObjectName("BoutonStatistiques")
        self.layoutBoutonExtra.addWidget(self.BoutonStatistiques, 0, QtCore.Qt.AlignLeft)
        self.BoutonRapport = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonRapport.sizePolicy().hasHeightForWidth())
        self.BoutonRapport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonRapport.setFont(font)
        self.BoutonRapport.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Images/Rapport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRapport.setIcon(icon9)
        self.BoutonRapport.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRapport.setObjectName("BoutonRapport")
        self.layoutBoutonExtra.addWidget(self.BoutonRapport, 0, QtCore.Qt.AlignLeft)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem7)
        self.layoutBouton.addLayout(self.layoutBoutonExtra)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem8)
        self.layoutBoutonSupport = QtWidgets.QVBoxLayout()
        self.layoutBoutonSupport.setObjectName("layoutBoutonSupport")
        self.BoutonSupportTecnique = QtWidgets.QPushButton(self.centralwidget)
        self.BoutonSupportTecnique.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonSupportTecnique.setFont(font)
        self.BoutonSupportTecnique.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonSupportTecnique.setStyleSheet("QPushButton{ padding : 20px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Images/PC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonSupportTecnique.setIcon(icon10)
        self.BoutonSupportTecnique.setIconSize(QtCore.QSize(40, 40))
        self.BoutonSupportTecnique.setAutoDefault(False)
        self.BoutonSupportTecnique.setDefault(False)
        self.BoutonSupportTecnique.setFlat(False)
        self.BoutonSupportTecnique.setObjectName("BoutonSupportTecnique")
        self.layoutBoutonSupport.addWidget(self.BoutonSupportTecnique, 0, QtCore.Qt.AlignLeft)
        self.layoutBouton.addLayout(self.layoutBoutonSupport)
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem9)
        self.layoutHorizontalPrincipal.addLayout(self.layoutBouton)
        self.layoutAffichagePrincipal = QtWidgets.QVBoxLayout()
        self.layoutAffichagePrincipal.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layoutAffichagePrincipal.setContentsMargins(0, -1, -1, -1)
        self.layoutAffichagePrincipal.setSpacing(0)
        self.layoutAffichagePrincipal.setObjectName("layoutAffichagePrincipal")
        spacerItem10 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutAffichagePrincipal.addItem(spacerItem10)
        self.LabelSIMM = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSIMM.setFont(font)
        self.LabelSIMM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LabelSIMM.setStyleSheet("\n"
"color: white;\n"
"\n"
" background-color: transparent ;")
        self.LabelSIMM.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LabelSIMM.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LabelSIMM.setObjectName("LabelSIMM")
        self.layoutAffichagePrincipal.addWidget(self.LabelSIMM)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BoutonFlecheNavigation = QtWidgets.QPushButton(self.centralwidget)
        self.BoutonFlecheNavigation.setMaximumSize(QtCore.QSize(60, 60))
        self.BoutonFlecheNavigation.setStyleSheet("\n"
"QPushButton{border-radius : 0px; padding : 5px ;background-color: white ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        self.BoutonFlecheNavigation.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonFlecheNavigation.setIcon(icon11)
        self.BoutonFlecheNavigation.setAutoDefault(False)
        self.BoutonFlecheNavigation.setDefault(False)
        self.BoutonFlecheNavigation.setFlat(False)
        self.BoutonFlecheNavigation.setObjectName("BoutonFlecheNavigation")
        self.horizontalLayout.addWidget(self.BoutonFlecheNavigation)
        self.frameFleche = QtWidgets.QFrame(self.centralwidget)
        self.frameFleche.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frameFleche.setStyleSheet("background-color: white;")
        self.frameFleche.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFleche.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFleche.setObjectName("frameFleche")
        self.horizontalLayout.addWidget(self.frameFleche)
        self.layoutAffichagePrincipal.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(600, 600))
        self.logo.setMaximumSize(QtCore.QSize(600, 600))
        self.logo.setStyleSheet(" background-color: transparent ;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Images/Logo_SIMM.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.logo)
        spacerItem12 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.layoutAffichagePrincipal.addLayout(self.horizontalLayout_2)
        self.LabelDefinitionSIMM = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LabelDefinitionSIMM.setFont(font)
        self.LabelDefinitionSIMM.setStyleSheet("\n"
"color: white;\n"
"\n"
" background-color: transparent ;")
        self.LabelDefinitionSIMM.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.LabelDefinitionSIMM.setObjectName("LabelDefinitionSIMM")
        self.layoutAffichagePrincipal.addWidget(self.LabelDefinitionSIMM, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.layoutHorizontalPrincipal.addLayout(self.layoutAffichagePrincipal)
        self.gridLayout_2.addLayout(self.layoutHorizontalPrincipal, 0, 0, 1, 1)
        Accueil.setCentralWidget(self.centralwidget)

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "Accueil"))
        self.BoutonAccueil.setText(_translate("Accueil", "Accueil"))
        self.BoutonAjouterEquipement.setText(_translate("Accueil", "Ajouter un\n"
"équipement"))
        self.BoutonModifierConsulterEquipement.setText(_translate("Accueil", "Modifier ou\n"
"consulter\n"
"un équipement"))
        self.BoutonRechercherEquipement.setText(_translate("Accueil", "Rechercher un\n"
"équipement"))
        self.BoutonAjouterPiece.setText(_translate("Accueil", " Ajouter une \n"
"pièce"))
        self.BoutonAjouterBonTravail.setText(_translate("Accueil", "Ajouter un bon\n"
"de travail"))
        self.BoutonRechercherBonTravail.setText(_translate("Accueil", "Rechercher un\n"
"bon de travail"))
        self.BoutonImprimerInventaire.setText(_translate("Accueil", "Imprimer tout\n"
"l\'inventaire"))
        self.BoutonStatistiques.setText(_translate("Accueil", "Voir les\n"
"statistiques"))
        self.BoutonRapport.setText(_translate("Accueil", "Rapport"))
        self.BoutonSupportTecnique.setText(_translate("Accueil", "Support\n"
"technique"))
       # self.LabelSIMM.setText(_translate("Accueil", "S.I.M.M. 2.1\n"
#"Hôpital Universitaire Justinien"))
        self.LabelDefinitionSIMM.setText(_translate("Accueil", "S.I.M.M. : Système d\'Inventorisation du Matériel Médical "))

