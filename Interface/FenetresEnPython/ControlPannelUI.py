# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlPannel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1571, 703)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #85cafc, stop: 1  #36357F);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        MainWindow.setWindowFilePath("")
        MainWindow.setDocumentMode(False)
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
        self.boutonAccueil = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boutonAccueil.setFont(font)
        self.boutonAccueil.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonAccueil.setIcon(icon)
        self.boutonAccueil.setIconSize(QtCore.QSize(35, 35))
        self.boutonAccueil.setObjectName("boutonAccueil")
        self.layoutBoutonEquipement.addWidget(self.boutonAccueil)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem2)
        self.BoutonAjouterEquipement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonAjouterEquipement.sizePolicy().hasHeightForWidth())
        self.BoutonAjouterEquipement.setSizePolicy(sizePolicy)
        self.BoutonAjouterEquipement.setMinimumSize(QtCore.QSize(50, 50))
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
        icon1.addPixmap(QtGui.QPixmap("../Images/plus (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterEquipement.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/pencil-edit-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonModifierConsulterEquipement.setIcon(icon2)
        self.BoutonModifierConsulterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonModifierConsulterEquipement.setObjectName("BoutonModifierConsulterEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonModifierConsulterEquipement)
        self.BoutonRechercherEquipement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonRechercherEquipement.sizePolicy().hasHeightForWidth())
        self.BoutonRechercherEquipement.setSizePolicy(sizePolicy)
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
        icon3.addPixmap(QtGui.QPixmap("../Images/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherEquipement.setIcon(icon3)
        self.BoutonRechercherEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherEquipement.setObjectName("BoutonRechercherEquipement")
        self.layoutBoutonEquipement.addWidget(self.BoutonRechercherEquipement)
        self.layoutBouton.addLayout(self.layoutBoutonEquipement)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem3)
        self.layoutBoutonBdT = QtWidgets.QVBoxLayout()
        self.layoutBoutonBdT.setObjectName("layoutBoutonBdT")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonBdT.addItem(spacerItem4)
        self.BoutonRechercherBonTravail = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonRechercherBonTravail.sizePolicy().hasHeightForWidth())
        self.BoutonRechercherBonTravail.setSizePolicy(sizePolicy)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/magnifier (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherBonTravail.setIcon(icon4)
        self.BoutonRechercherBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherBonTravail.setObjectName("BoutonRechercherBonTravail")
        self.layoutBoutonBdT.addWidget(self.BoutonRechercherBonTravail)
        self.BoutonAjouterBonTravail = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonAjouterBonTravail.sizePolicy().hasHeightForWidth())
        self.BoutonAjouterBonTravail.setSizePolicy(sizePolicy)
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
        icon5.addPixmap(QtGui.QPixmap("../Images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterBonTravail.setIcon(icon5)
        self.BoutonAjouterBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterBonTravail.setObjectName("BoutonAjouterBonTravail")
        self.layoutBoutonBdT.addWidget(self.BoutonAjouterBonTravail)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonBdT.addItem(spacerItem5)
        self.layoutBouton.addLayout(self.layoutBoutonBdT)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem6)
        self.layoutBoutonExtra = QtWidgets.QVBoxLayout()
        self.layoutBoutonExtra.setObjectName("layoutBoutonExtra")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem7)
        self.BoutonImprimerInventaire = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonImprimerInventaire.sizePolicy().hasHeightForWidth())
        self.BoutonImprimerInventaire.setSizePolicy(sizePolicy)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Images/printer- (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonImprimerInventaire.setIcon(icon6)
        self.BoutonImprimerInventaire.setIconSize(QtCore.QSize(40, 40))
        self.BoutonImprimerInventaire.setObjectName("BoutonImprimerInventaire")
        self.layoutBoutonExtra.addWidget(self.BoutonImprimerInventaire)
        self.BoutonStatistiques = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonStatistiques.sizePolicy().hasHeightForWidth())
        self.BoutonStatistiques.setSizePolicy(sizePolicy)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Images/pie-chart (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonStatistiques.setIcon(icon7)
        self.BoutonStatistiques.setIconSize(QtCore.QSize(40, 40))
        self.BoutonStatistiques.setObjectName("BoutonStatistiques")
        self.layoutBoutonExtra.addWidget(self.BoutonStatistiques)
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
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images/Rapport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRapport.setIcon(icon8)
        self.BoutonRapport.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRapport.setObjectName("BoutonRapport")
        self.layoutBoutonExtra.addWidget(self.BoutonRapport)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem8)
        self.layoutBouton.addLayout(self.layoutBoutonExtra)
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem10)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../Images/PC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonSuportTecnique.setIcon(icon9)
        self.BoutonSuportTecnique.setIconSize(QtCore.QSize(40, 40))
        self.BoutonSuportTecnique.setAutoDefault(False)
        self.BoutonSuportTecnique.setDefault(False)
        self.BoutonSuportTecnique.setFlat(False)
        self.BoutonSuportTecnique.setObjectName("BoutonSuportTecnique")
        self.layoutBoutonSupport.addWidget(self.BoutonSuportTecnique)
        self.layoutBouton.addLayout(self.layoutBoutonSupport)
        spacerItem11 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem11)
        self.layoutHorizontalPrincipal.addLayout(self.layoutBouton)
        self.layoutAffichagePrincipal = QtWidgets.QVBoxLayout()
        self.layoutAffichagePrincipal.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layoutAffichagePrincipal.setContentsMargins(0, -1, -1, -1)
        self.layoutAffichagePrincipal.setSpacing(15)
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
        self.layoutAffichagePrincipal.addWidget(self.LabelDefinitionSIMM, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.layoutHorizontalPrincipal.addLayout(self.layoutAffichagePrincipal)
        self.gridLayout_2.addLayout(self.layoutHorizontalPrincipal, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boutonAccueil.setText(_translate("MainWindow", "Accueil"))
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
        self.BoutonRapport.setText(_translate("MainWindow", "Rapport"))
        self.BoutonSuportTecnique.setText(_translate("MainWindow", "Support\n"
"technique"))
        self.LabelSIMM20HopitalSaintMichel.setText(_translate("MainWindow", "S.I.M.M. 2.0\n"
"Hôpital Universitaire Justinien "))
        self.LabelDefinitionSIMM.setText(_translate("MainWindow", "S.I.M.M. : Système d\'Inventorisation du Matériel Médical "))

