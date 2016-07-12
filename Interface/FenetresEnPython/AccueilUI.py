# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accueil(object):
    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.setWindowModality(QtCore.Qt.NonModal)
        Accueil.setEnabled(True)
        Accueil.resize(1255, 1312)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        Accueil.setFont(font)
        Accueil.setStyleSheet("  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #85cafc, stop: 1  #36357F);")
        Accueil.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        Accueil.setWindowFilePath("")
        Accueil.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Accueil)
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
        self.layoutBoutonEquipement.addWidget(self.BoutonAccueil)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonEquipement.addItem(spacerItem2)
        self.BoutonAjouterEquipement = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonEquipement.addWidget(self.BoutonAjouterEquipement)
        self.BoutonModifierConsulterEquipement = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonEquipement.addWidget(self.BoutonModifierConsulterEquipement)
        self.BoutonRechercherEquipement = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonEquipement.addWidget(self.BoutonRechercherEquipement)
        self.layoutBouton.addLayout(self.layoutBoutonEquipement)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{ padding : 5px; border-radius: 8px; background-color: transparent ;color : white;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #cccccc , stop: 1#f2f2f2);\n"
"}\n"
"\n"
"QPushButton:pressed{ background-color: #cccccc; }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/piece_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.layoutBouton.addWidget(self.pushButton)
        self.layoutBoutonBdT = QtWidgets.QVBoxLayout()
        self.layoutBoutonBdT.setObjectName("layoutBoutonBdT")
        self.BoutonAjouterBonTravail = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonBdT.addWidget(self.BoutonAjouterBonTravail)
        self.BoutonRechercherBonTravail = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonBdT.addWidget(self.BoutonRechercherBonTravail)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonBdT.addItem(spacerItem5)
        self.layoutBouton.addLayout(self.layoutBoutonBdT)
        self.layoutBoutonExtra = QtWidgets.QVBoxLayout()
        self.layoutBoutonExtra.setObjectName("layoutBoutonExtra")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBoutonExtra.addItem(spacerItem6)
        self.BoutonImprimerInventaire = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonExtra.addWidget(self.BoutonImprimerInventaire)
        self.BoutonStatistiques = QtWidgets.QPushButton(self.centralwidget)
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
        self.layoutBoutonExtra.addWidget(self.BoutonStatistiques)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Images/PC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonSupportTecnique.setIcon(icon9)
        self.BoutonSupportTecnique.setIconSize(QtCore.QSize(40, 40))
        self.BoutonSupportTecnique.setAutoDefault(False)
        self.BoutonSupportTecnique.setDefault(False)
        self.BoutonSupportTecnique.setFlat(False)
        self.BoutonSupportTecnique.setObjectName("BoutonSupportTecnique")
        self.layoutBoutonSupport.addWidget(self.BoutonSupportTecnique)
        self.layoutBouton.addLayout(self.layoutBoutonSupport)
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutBouton.addItem(spacerItem9)
        self.layoutHorizontalPrincipal.addLayout(self.layoutBouton)
        self.layoutAffichagePrincipal = QtWidgets.QVBoxLayout()
        self.layoutAffichagePrincipal.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layoutAffichagePrincipal.setContentsMargins(0, -1, -1, -1)
        self.layoutAffichagePrincipal.setSpacing(0)
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonFlecheNavigation.setIcon(icon10)
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
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(600, 600))
        self.logo.setStyleSheet("background-color: transparent ;color : white;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Images/Logo_SIMM.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.layoutAffichagePrincipal.addWidget(self.logo)
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
        self.pushButton.setText(_translate("Accueil", " Ajouter une pièce"))
        self.BoutonAjouterBonTravail.setText(_translate("Accueil", "Ajouter un bon\n"
"de travail"))
        self.BoutonRechercherBonTravail.setText(_translate("Accueil", "Rechercher un\n"
"bon de travail"))
        self.BoutonImprimerInventaire.setText(_translate("Accueil", "Imprimer tout\n"
"l\'inventaire"))
        self.BoutonStatistiques.setText(_translate("Accueil", "Voir les\n"
"statistiques"))
        self.BoutonSupportTecnique.setText(_translate("Accueil", "Support\n"
"technique"))
        self.LabelSIMM20HopitalSaintMichel.setText(_translate("Accueil", "S.I.M.M. 2.0\n"
"Hôpital Saint-Michel "))
        self.LabelDefinitionSIMM.setText(_translate("Accueil", "S.I.M.M. : Système d\'Inventorisation du Matériel Médical "))

