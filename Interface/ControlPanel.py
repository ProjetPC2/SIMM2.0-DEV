# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlPannel_lun14juin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Interface.FenetresEnPython import AjoutEquipement, ConsultationEquipement, BonDeTravail

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(877, 786)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #85cafc, stop: 1  #36357F);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/printer- (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonImprimerInventaire.setIcon(icon)
        self.BoutonImprimerInventaire.setIconSize(QtCore.QSize(40, 40))
        self.BoutonImprimerInventaire.setObjectName("BoutonImprimerInventaire")
        self.gridLayout_2.addWidget(self.BoutonImprimerInventaire, 14, 0, 1, 1)
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
        # self.gridLayout_2.addWidget(self.LabelSIMM20HopitalSaintMichel, 1, 2, 19, 1)

        #####
        MainFrame = QtWidgets.QWidget()
        ui = BonDeTravail.Ui_MainWindow()
        ui.setupUi(MainFrame)
        self.widgetCentral = MainFrame
        self.gridLayout_2.addWidget(self.widgetCentral, 1, 2, 19, 1)

        ####
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
        self.gridLayout_2.addWidget(self.LabelDefinitionSIMM, 21, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 11, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 17, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 16, 0, 1, 1)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/magnifier (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherBonTravail.setIcon(icon1)
        self.BoutonRechercherBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherBonTravail.setObjectName("BoutonRechercherBonTravail")
        self.gridLayout_2.addWidget(self.BoutonRechercherBonTravail, 10, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 12, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 7, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 20, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 0, 0, 1, 1)
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
        icon2.addPixmap(QtGui.QPixmap("Images/pencil-edit-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonModifierConsulterEquipement.setIcon(icon2)
        self.BoutonModifierConsulterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonModifierConsulterEquipement.setObjectName("BoutonModifierConsulterEquipement")
        self.gridLayout_2.addWidget(self.BoutonModifierConsulterEquipement, 5, 0, 1, 1)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/plus (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterEquipement.setIcon(icon3)
        self.BoutonAjouterEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterEquipement.setFlat(False)
        self.BoutonAjouterEquipement.setObjectName("BoutonAjouterEquipement")
        self.gridLayout_2.addWidget(self.BoutonAjouterEquipement, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 697, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 1, 1, 18, 1)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/PC2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonSuportTecnique.setIcon(icon4)
        self.BoutonSuportTecnique.setIconSize(QtCore.QSize(40, 40))
        self.BoutonSuportTecnique.setAutoDefault(False)
        self.BoutonSuportTecnique.setDefault(False)
        self.BoutonSuportTecnique.setFlat(False)
        self.BoutonSuportTecnique.setObjectName("BoutonSuportTecnique")
        self.gridLayout_2.addWidget(self.BoutonSuportTecnique, 20, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 2, 0, 1, 1)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/pie-chart (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonStatistiques.setIcon(icon5)
        self.BoutonStatistiques.setIconSize(QtCore.QSize(40, 40))
        self.BoutonStatistiques.setObjectName("BoutonStatistiques")
        self.gridLayout_2.addWidget(self.BoutonStatistiques, 13, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 15, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 1, 0, 1, 1)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonRechercherEquipement.setIcon(icon6)
        self.BoutonRechercherEquipement.setIconSize(QtCore.QSize(40, 40))
        self.BoutonRechercherEquipement.setObjectName("BoutonRechercherEquipement")
        self.gridLayout_2.addWidget(self.BoutonRechercherEquipement, 6, 0, 1, 1)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonAjouterBonTravail.setIcon(icon7)
        self.BoutonAjouterBonTravail.setIconSize(QtCore.QSize(40, 40))
        self.BoutonAjouterBonTravail.setObjectName("BoutonAjouterBonTravail")
        self.gridLayout_2.addWidget(self.BoutonAjouterBonTravail, 9, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BoutonImprimerInventaire.setText(_translate("MainWindow", "Imprimer tout\n"
"l\'inventaire"))
        self.LabelSIMM20HopitalSaintMichel.setText(_translate("MainWindow", "S.I.M.M. 2.0\n"
"Hôpital Saint-Michel "))
        self.LabelDefinitionSIMM.setText(_translate("MainWindow", "S.I.M.M. : Système d\'Inventorisation du Matériel Médical "))
        self.BoutonRechercherBonTravail.setText(_translate("MainWindow", "Rechercher un\n"
"bon de travail"))
        self.BoutonModifierConsulterEquipement.setText(_translate("MainWindow", "Modifier ou\n"
"consulter\n"
"un équipement"))
        self.BoutonAjouterEquipement.setText(_translate("MainWindow", "Ajouter un\n"
"équipement"))
        self.BoutonSuportTecnique.setText(_translate("MainWindow", "Support\n"
"technique"))
        self.BoutonStatistiques.setText(_translate("MainWindow", "Voir les\n"
"statistiques"))
        self.BoutonRechercherEquipement.setText(_translate("MainWindow", "Rechercher un\n"
"équipement"))
        self.BoutonAjouterBonTravail.setText(_translate("MainWindow", "Ajouter un bon\n"
"de travail"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())


