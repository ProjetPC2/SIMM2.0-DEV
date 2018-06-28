# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rbdt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from win32api import GetSystemMetrics

class Ui_RechercheBonDeTravail(object):
    def setupUi(self, RechercheBonDeTravail):
        RechercheBonDeTravail.setObjectName("RechercheBonDeTravail")

        #width = GetSystemMetrics(0)
        #heigth = GetSystemMetrics(1)
        #facteur_grandissement = 0.80
        #RechercheBonDeTravail.resize(1355, 689)

        RechercheBonDeTravail.setMaximumSize(QtCore.QSize(11111112, 1111111))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../SIMM2.0-DEV/Interface/Images/PC2_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        RechercheBonDeTravail.setWindowIcon(icon)
        RechercheBonDeTravail.setStyleSheet("QWidget{\n"
"background:white;\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background: rgb(247,247,247)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"padding: 1px;\n"
"color: black;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(169, 167, 170)\n"
"}\n"
"\n"
"QComboBox{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background: rgb(247,247,247)\n"
"}\n"
"\n"
"\n"
"QDateEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background: rgb(247,247,247)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(RechercheBonDeTravail)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableResultats = QtWidgets.QTableWidget(RechercheBonDeTravail)
        self.tableResultats.setMinimumSize(QtCore.QSize(200, 500))
        self.tableResultats.setMaximumSize(QtCore.QSize(2000, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableResultats.setFont(font)
        self.tableResultats.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.tableResultats.setLineWidth(10)
        self.tableResultats.setMidLineWidth(9)
        self.tableResultats.setProperty("showDropIndicator", True)
        self.tableResultats.setShowGrid(True)
        self.tableResultats.setGridStyle(QtCore.Qt.SolidLine)
        self.tableResultats.setWordWrap(True)
        self.tableResultats.setObjectName("tableResultats")
        self.tableResultats.setColumnCount(7)
        self.tableResultats.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableResultats.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultats.setHorizontalHeaderItem(6, item)
        self.tableResultats.horizontalHeader().setCascadingSectionResizes(True)
        self.tableResultats.horizontalHeader().setDefaultSectionSize(200)
        self.tableResultats.horizontalHeader().setMinimumSectionSize(30)
        self.tableResultats.horizontalHeader().setStretchLastSection(True)
        self.tableResultats.verticalHeader().setDefaultSectionSize(30)
        self.tableResultats.verticalHeader().setMinimumSectionSize(20)
        self.tableResultats.verticalHeader().setSortIndicatorShown(False)
        self.tableResultats.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.tableResultats)
        self.gridLayout.addLayout(self.verticalLayout_11, 4, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBoxCategorieEquipement = QtWidgets.QComboBox(RechercheBonDeTravail)
        self.comboBoxCategorieEquipement.setMinimumSize(QtCore.QSize(150, 20))
        self.comboBoxCategorieEquipement.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCategorieEquipement.setFont(font)
        self.comboBoxCategorieEquipement.setObjectName("comboBoxCategorieEquipement")
        self.gridLayout_3.addWidget(self.comboBoxCategorieEquipement, 1, 0, 1, 1)
        self.calendrierAvant = QtWidgets.QDateEdit(RechercheBonDeTravail)
        self.calendrierAvant.setMinimumSize(QtCore.QSize(150, 20))
        self.calendrierAvant.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendrierAvant.setFont(font)
        self.calendrierAvant.setCalendarPopup(True)
        self.calendrierAvant.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierAvant.setObjectName("calendrierAvant")
        self.gridLayout_3.addWidget(self.calendrierAvant, 1, 1, 1, 1)
        self.calendrierApres = QtWidgets.QDateEdit(RechercheBonDeTravail)
        self.calendrierApres.setMinimumSize(QtCore.QSize(150, 20))
        self.calendrierApres.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendrierApres.setFont(font)
        self.calendrierApres.setCalendarPopup(True)
        self.calendrierApres.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierApres.setObjectName("calendrierApres")
        self.gridLayout_3.addWidget(self.calendrierApres, 1, 2, 1, 1)
        self.boutonNouvelleRecherche = QtWidgets.QPushButton(RechercheBonDeTravail)
        self.boutonNouvelleRecherche.setMinimumSize(QtCore.QSize(92, 43))
        self.boutonNouvelleRecherche.setMaximumSize(QtCore.QSize(92, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.boutonNouvelleRecherche.setFont(font)
        self.boutonNouvelleRecherche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonNouvelleRecherche.setObjectName("boutonNouvelleRecherche")
        self.gridLayout_3.addWidget(self.boutonNouvelleRecherche, 4, 3, 1, 1)
        self.LabelApres = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelApres.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelApres.setFont(font)
        self.LabelApres.setStyleSheet("background: white;")
        self.LabelApres.setObjectName("LabelApres")
        self.gridLayout_3.addWidget(self.LabelApres, 0, 2, 1, 1)
        self.LabelAvant = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelAvant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelAvant.setFont(font)
        self.LabelAvant.setStyleSheet("background: white;")
        self.LabelAvant.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LabelAvant.setObjectName("LabelAvant")
        self.gridLayout_3.addWidget(self.LabelAvant, 0, 1, 1, 1)
        self.labelCategorie = QtWidgets.QLabel(RechercheBonDeTravail)
        self.labelCategorie.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorie.setFont(font)
        self.labelCategorie.setStyleSheet("background: white;")
        self.labelCategorie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCategorie.setObjectName("labelCategorie")
        self.gridLayout_3.addWidget(self.labelCategorie, 0, 0, 1, 1)
        self.comboBoxEtat = QtWidgets.QComboBox(RechercheBonDeTravail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxEtat.sizePolicy().hasHeightForWidth())
        self.comboBoxEtat.setSizePolicy(sizePolicy)
        self.comboBoxEtat.setMinimumSize(QtCore.QSize(150, 20))
        self.comboBoxEtat.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxEtat.setFont(font)
        self.comboBoxEtat.setObjectName("comboBoxEtat")
        self.gridLayout_3.addWidget(self.comboBoxEtat, 4, 2, 1, 1)
        self.LabelDescription = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelDescription.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelDescription.setFont(font)
        self.LabelDescription.setStyleSheet("background: white;")
        self.LabelDescription.setObjectName("LabelDescription")
        self.gridLayout_3.addWidget(self.LabelDescription, 3, 1, 1, 1)
        self.lineEditDescriptionSituation = QtWidgets.QLineEdit(RechercheBonDeTravail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDescriptionSituation.sizePolicy().hasHeightForWidth())
        self.lineEditDescriptionSituation.setSizePolicy(sizePolicy)
        self.lineEditDescriptionSituation.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEditDescriptionSituation.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDescriptionSituation.setFont(font)
        self.lineEditDescriptionSituation.setStyleSheet("\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background: rgb(247,247,247);")
        self.lineEditDescriptionSituation.setObjectName("lineEditDescriptionSituation")
        self.gridLayout_3.addWidget(self.lineEditDescriptionSituation, 4, 1, 1, 1)
        self.LabelUnite = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelUnite.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelUnite.setFont(font)
        self.LabelUnite.setStyleSheet("background: white;")
        self.LabelUnite.setObjectName("LabelUnite")
        self.gridLayout_3.addWidget(self.LabelUnite, 3, 0, 1, 1)
        self.LabelEtat = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelEtat.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelEtat.setFont(font)
        self.LabelEtat.setStyleSheet("background: white;")
        self.LabelEtat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelEtat.setObjectName("LabelEtat")
        self.gridLayout_3.addWidget(self.LabelEtat, 3, 2, 1, 1)
        self.boutonActualiser = QtWidgets.QPushButton(RechercheBonDeTravail)
        self.boutonActualiser.setMinimumSize(QtCore.QSize(47, 43))
        self.boutonActualiser.setMaximumSize(QtCore.QSize(47, 43))
        self.boutonActualiser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonActualiser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/refresh-button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon1)
        self.boutonActualiser.setIconSize(QtCore.QSize(50, 50))
        self.boutonActualiser.setObjectName("boutonActualiser")
        self.gridLayout_3.addWidget(self.boutonActualiser, 1, 3, 1, 1)
        self.comboBoxUnite = QtWidgets.QComboBox(RechercheBonDeTravail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUnite.sizePolicy().hasHeightForWidth())
        self.comboBoxUnite.setSizePolicy(sizePolicy)
        self.comboBoxUnite.setMinimumSize(QtCore.QSize(150, 20))
        self.comboBoxUnite.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxUnite.setFont(font)
        self.comboBoxUnite.setObjectName("comboBoxUnite")
        self.gridLayout_3.addWidget(self.comboBoxUnite, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(RechercheBonDeTravail)
        self.label.setMaximumSize(QtCore.QSize(38, 34))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/magnifier (1).png"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.LabelTitre = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelTitre.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTitre.setFont(font)
        self.LabelTitre.setStyleSheet("background: white;")
        self.LabelTitre.setObjectName("LabelTitre")
        self.horizontalLayout_3.addWidget(self.LabelTitre)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(RechercheBonDeTravail)
        QtCore.QMetaObject.connectSlotsByName(RechercheBonDeTravail)

    def retranslateUi(self, RechercheBonDeTravail):
        _translate = QtCore.QCoreApplication.translate
        RechercheBonDeTravail.setWindowTitle(_translate("RechercheBonDeTravail", "PC2"))
        self.tableResultats.setSortingEnabled(False)
        item = self.tableResultats.verticalHeaderItem(0)
        item.setText(_translate("RechercheBonDeTravail", "1"))
        item = self.tableResultats.verticalHeaderItem(1)
        item.setText(_translate("RechercheBonDeTravail", "2"))
        item = self.tableResultats.verticalHeaderItem(2)
        item.setText(_translate("RechercheBonDeTravail", "3"))
        item = self.tableResultats.horizontalHeaderItem(0)
        item.setText(_translate("RechercheBonDeTravail", "ID"))
        item = self.tableResultats.horizontalHeaderItem(1)
        item.setText(_translate("RechercheBonDeTravail", "Catégorie d\'équipement"))
        item = self.tableResultats.horizontalHeaderItem(2)
        item.setText(_translate("RechercheBonDeTravail", "Modèle"))
        item = self.tableResultats.horizontalHeaderItem(3)
        item.setText(_translate("RechercheBonDeTravail", "Unite"))
        item = self.tableResultats.horizontalHeaderItem(4)
        item.setText(_translate("RechercheBonDeTravail", "État"))
        item = self.tableResultats.horizontalHeaderItem(5)
        item.setText(_translate("RechercheBonDeTravail", "Date"))
        item = self.tableResultats.horizontalHeaderItem(6)
        item.setText(_translate("RechercheBonDeTravail", "Description"))
        self.calendrierAvant.setDisplayFormat(_translate("RechercheBonDeTravail", "dd-MM-yyyy"))
        self.calendrierApres.setDisplayFormat(_translate("RechercheBonDeTravail", "dd-MM-yyyy"))
        self.boutonNouvelleRecherche.setText(_translate("RechercheBonDeTravail", "Nouvelle\n"
"recherche"))
        self.LabelApres.setText(_translate("RechercheBonDeTravail", "Après le"))
        self.LabelAvant.setText(_translate("RechercheBonDeTravail", "Avant le"))
        self.labelCategorie.setText(_translate("RechercheBonDeTravail", "Catégorie d\'équipement"))
        self.LabelDescription.setText(_translate("RechercheBonDeTravail", "Description de la situation"))
        self.LabelUnite.setText(_translate("RechercheBonDeTravail", "Unité"))
        self.LabelEtat.setText(_translate("RechercheBonDeTravail", "État"))
        self.LabelTitre.setText(_translate("RechercheBonDeTravail", "Assistant de Recherche - Bon de travail"))

