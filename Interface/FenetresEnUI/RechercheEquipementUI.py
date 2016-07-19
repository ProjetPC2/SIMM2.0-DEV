# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetreRechEquip.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 614)
        MainWindow.setStyleSheet("QWidget{\n"
"background: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}\n"
"\n"
"QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logoLoupe = QtWidgets.QLabel(self.centralwidget)
        self.logoLoupe.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logoLoupe.setFont(font)
        self.logoLoupe.setStyleSheet("background: white;")
        self.logoLoupe.setText("")
        self.logoLoupe.setPixmap(QtGui.QPixmap("../Documents/GitHub/SIMM2.0-DEV/Interface/FenetresEnUI/Images/magnifier.png"))
        self.logoLoupe.setObjectName("logoLoupe")
        self.gridLayout_2.addWidget(self.logoLoupe, 0, 0, 1, 1)
        self.labelTitre = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitre.setFont(font)
        self.labelTitre.setStyleSheet("background: white;")
        self.labelTitre.setObjectName("labelTitre")
        self.gridLayout_2.addWidget(self.labelTitre, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelCategorieEquipement = QtWidgets.QLabel(self.centralwidget)
        self.labelCategorieEquipement.setStyleSheet("background: white;")
        self.labelCategorieEquipement.setObjectName("labelCategorieEquipement")
        self.gridLayout.addWidget(self.labelCategorieEquipement, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.comboBoxCentreService = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCentreService.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCentreService.setFont(font)
        self.comboBoxCentreService.setObjectName("comboBoxCentreService")
        self.gridLayout.addWidget(self.comboBoxCentreService, 3, 2, 1, 1)
        self.comboBoxEtatService = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxEtatService.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBoxEtatService.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxEtatService.setFont(font)
        self.comboBoxEtatService.setObjectName("comboBoxEtatService")
        self.gridLayout.addWidget(self.comboBoxEtatService, 3, 0, 1, 1)
        self.labelEtatService = QtWidgets.QLabel(self.centralwidget)
        self.labelEtatService.setStyleSheet("background: white;")
        self.labelEtatService.setObjectName("labelEtatService")
        self.gridLayout.addWidget(self.labelEtatService, 2, 0, 1, 1)
        self.comboBoxProvenance = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxProvenance.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.gridLayout.addWidget(self.comboBoxProvenance, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.labelCentreService = QtWidgets.QLabel(self.centralwidget)
        self.labelCentreService.setStyleSheet("background: white;")
        self.labelCentreService.setObjectName("labelCentreService")
        self.gridLayout.addWidget(self.labelCentreService, 2, 2, 1, 1)
        self.comboBoxCategorieEquipement = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCategorieEquipement.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBoxCategorieEquipement.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCategorieEquipement.setFont(font)
        self.comboBoxCategorieEquipement.setObjectName("comboBoxCategorieEquipement")
        self.gridLayout.addWidget(self.comboBoxCategorieEquipement, 1, 0, 1, 1)
        self.lineEditNumeroSerie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumeroSerie.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditNumeroSerie.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNumeroSerie.setFont(font)
        self.lineEditNumeroSerie.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.lineEditNumeroSerie.setObjectName("lineEditNumeroSerie")
        self.gridLayout.addWidget(self.lineEditNumeroSerie, 1, 2, 1, 1)
        self.labelNumeroSerie = QtWidgets.QLabel(self.centralwidget)
        self.labelNumeroSerie.setStyleSheet("background: white;")
        self.labelNumeroSerie.setObjectName("labelNumeroSerie")
        self.gridLayout.addWidget(self.labelNumeroSerie, 0, 2, 1, 1)
        self.comboBoxSalle = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSalle.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBoxSalle.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxSalle.setFont(font)
        self.comboBoxSalle.setObjectName("comboBoxSalle")
        self.gridLayout.addWidget(self.comboBoxSalle, 5, 0, 1, 1)
        self.labelProvenance = QtWidgets.QLabel(self.centralwidget)
        self.labelProvenance.setStyleSheet("background: white;")
        self.labelProvenance.setObjectName("labelProvenance")
        self.gridLayout.addWidget(self.labelProvenance, 4, 2, 1, 1)
        self.labelSalle = QtWidgets.QLabel(self.centralwidget)
        self.labelSalle.setStyleSheet("background: white;")
        self.labelSalle.setObjectName("labelSalle")
        self.gridLayout.addWidget(self.labelSalle, 4, 0, 1, 1)
        self.boutonActualiser = QtWidgets.QPushButton(self.centralwidget)
        self.boutonActualiser.setMinimumSize(QtCore.QSize(47, 43))
        self.boutonActualiser.setMaximumSize(QtCore.QSize(47, 43))
        self.boutonActualiser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonActualiser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Documents/GitHub/SIMM2.0-DEV/Interface/FenetresEnUI/Images/refresh-button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon)
        self.boutonActualiser.setIconSize(QtCore.QSize(50, 50))
        self.boutonActualiser.setObjectName("boutonActualiser")
        self.gridLayout.addWidget(self.boutonActualiser, 1, 4, 1, 1)
        self.boutonNouvelleRecherche = QtWidgets.QPushButton(self.centralwidget)
        self.boutonNouvelleRecherche.setMinimumSize(QtCore.QSize(92, 43))
        self.boutonNouvelleRecherche.setMaximumSize(QtCore.QSize(92, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.boutonNouvelleRecherche.setFont(font)
        self.boutonNouvelleRecherche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonNouvelleRecherche.setObjectName("boutonNouvelleRecherche")
        self.gridLayout.addWidget(self.boutonNouvelleRecherche, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.tableResultats = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableResultats.setFont(font)
        self.tableResultats.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.tableResultats.setObjectName("tableResultats")
        self.tableResultats.setColumnCount(3)
        self.tableResultats.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(2, item)
        self.tableResultats.horizontalHeader().setDefaultSectionSize(200)
        self.tableResultats.horizontalHeader().setMinimumSectionSize(150)
        self.tableResultats.verticalHeader().setDefaultSectionSize(30)
        self.tableResultats.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout_3.addWidget(self.tableResultats, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitre.setText(_translate("MainWindow", "Assistant de recherche - Équipement"))
        self.labelCategorieEquipement.setText(_translate("MainWindow", "Catégorie d\'équipement"))
        self.labelEtatService.setText(_translate("MainWindow", "État de service"))
        self.labelCentreService.setText(_translate("MainWindow", "Centre de service"))
        self.labelNumeroSerie.setText(_translate("MainWindow", "Numéro de série"))
        self.labelProvenance.setText(_translate("MainWindow", "Provenance"))
        self.labelSalle.setText(_translate("MainWindow", "Salle"))
        self.boutonNouvelleRecherche.setText(_translate("MainWindow", "Nouvelle\n"
"fenêtre"))
        item = self.tableResultats.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableResultats.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableResultats.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableResultats.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableResultats.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableResultats.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Catégorie d\'équipement"))
        item = self.tableResultats.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marque"))

