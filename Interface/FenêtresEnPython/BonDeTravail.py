# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BdT3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager


class BonDeTravailUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1518, 1183)
        MainWindow.setMaximumSize(QtCore.QSize(167777, 16777215))
        MainWindow.setStyleSheet("QMainWindow \n"
" {\n"
"\n"
"background: white;\n"
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
"QPushButton::pressed {\n"
"padding: 1px;\n"
"color: black;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 8px;\n"
"background:rgb(169, 167, 170)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QTextEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}")
        # MainWindow.setIconSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTitre = QtWidgets.QLabel(self.centralwidget)
        self.labelTitre.setMaximumSize(QtCore.QSize(20000, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitre.setFont(font)
        self.labelTitre.setAutoFillBackground(False)
        self.labelTitre.setStyleSheet("")
        self.labelTitre.setObjectName("labelTitre")
        self.horizontalLayout.addWidget(self.labelTitre)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelPhotoPlus = QtWidgets.QLabel(self.centralwidget)
        self.labelPhotoPlus.setMaximumSize(QtCore.QSize(100, 100))
        self.labelPhotoPlus.setText("")
        self.labelPhotoPlus.setPixmap(QtGui.QPixmap("../../../GitHub/SIMM2.0-DEV/Interface/Images/plus.png"))
        self.labelPhotoPlus.setScaledContents(False)
        self.labelPhotoPlus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPhotoPlus.setObjectName("labelPhotoPlus")
        self.horizontalLayout.addWidget(self.labelPhotoPlus)
        spacerItem1 = QtWidgets.QSpacerItem(40, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelCategorieEquip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorieEquip.setFont(font)
        self.labelCategorieEquip.setObjectName("labelCategorieEquip")
        self.gridLayout_2.addWidget(self.labelCategorieEquip, 0, 2, 1, 1)
        self.lineEditID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditID.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditID.setFont(font)
        self.lineEditID.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}\n"
"")
        self.lineEditID.setObjectName("lineEditID")
        self.gridLayout_2.addWidget(self.lineEditID, 1, 1, 1, 1)
        self.labelEcritureCatEquip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureCatEquip.setFont(font)
        self.labelEcritureCatEquip.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247;)\n"
"}\n"
"")
        self.labelEcritureCatEquip.setObjectName("labelEcritureCatEquip")
        self.gridLayout_2.addWidget(self.labelEcritureCatEquip, 1, 2, 1, 1)
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ID.setFont(font)
        self.label_ID.setObjectName("label_ID")
        self.gridLayout_2.addWidget(self.label_ID, 0, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelSalle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setObjectName("labelSalle")
        self.gridLayout.addWidget(self.labelSalle, 3, 2, 1, 1)
        self.labelCentreService = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCentreService.setFont(font)
        self.labelCentreService.setStyleSheet("")
        self.labelCentreService.setObjectName("labelCentreService")
        self.gridLayout.addWidget(self.labelCentreService, 3, 1, 1, 1)
        self.labelModele = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelModele.setFont(font)
        self.labelModele.setObjectName("labelModele")
        self.gridLayout.addWidget(self.labelModele, 0, 2, 1, 1)
        self.labelEcritureMarque = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureMarque.setFont(font)
        self.labelEcritureMarque.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247;)\n"
"}\n"
"")
        self.labelEcritureMarque.setObjectName("labelEcritureMarque")
        self.gridLayout.addWidget(self.labelEcritureMarque, 2, 1, 1, 1)
        self.labelEcritureModele = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureModele.setFont(font)
        self.labelEcritureModele.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}\n"
"")
        self.labelEcritureModele.setObjectName("labelEcritureModele")
        self.gridLayout.addWidget(self.labelEcritureModele, 2, 2, 1, 1)
        self.labelMarque = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMarque.setFont(font)
        self.labelMarque.setObjectName("labelMarque")
        self.gridLayout.addWidget(self.labelMarque, 0, 1, 1, 1)
        self.labelEcritureCentreService = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureCentreService.setFont(font)
        self.labelEcritureCentreService.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247;)\n"
"}\n"
"")
        self.labelEcritureCentreService.setObjectName("labelEcritureCentreService")
        self.gridLayout.addWidget(self.labelEcritureCentreService, 4, 1, 1, 1)
        self.labelEcritureSalle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureSalle.setFont(font)
        self.labelEcritureSalle.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247;)\n"
"}\n"
"")
        self.labelEcritureSalle.setObjectName("labelEcritureSalle")
        self.gridLayout.addWidget(self.labelEcritureSalle, 4, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.labelPhotoOutils = QtWidgets.QLabel(self.centralwidget)
        self.labelPhotoOutils.setText("")
        self.labelPhotoOutils.setPixmap(QtGui.QPixmap("../../../GitHub/SIMM2.0-DEV/Interface/Images/repair-tools (1).png"))
        self.labelPhotoOutils.setScaledContents(False)
        self.labelPhotoOutils.setObjectName("labelPhotoOutils")
        self.horizontalLayout_2.addWidget(self.labelPhotoOutils)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.boutonSauvegarde = QtWidgets.QPushButton(self.centralwidget)
        self.boutonSauvegarde.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonSauvegarde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonSauvegarde.setAutoFillBackground(False)
        self.boutonSauvegarde.setStyleSheet("")
        self.boutonSauvegarde.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSauvegarde.setIcon(icon)
        self.boutonSauvegarde.setIconSize(QtCore.QSize(35, 35))
        self.boutonSauvegarde.setObjectName("boutonSauvegarde")
        self.horizontalLayout_3.addWidget(self.boutonSauvegarde)
        self.boutonFlecheDoubleGauche = QtWidgets.QPushButton(self.centralwidget)
        self.boutonFlecheDoubleGauche.setMaximumSize(QtCore.QSize(50, 150))
        self.boutonFlecheDoubleGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleGauche.setStyleSheet("")
        self.boutonFlecheDoubleGauche.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/double-left-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleGauche.setIcon(icon1)
        self.boutonFlecheDoubleGauche.setObjectName("boutonFlecheDoubleGauche")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleGauche)
        self.boutonFlecheGauche = QtWidgets.QPushButton(self.centralwidget)
        self.boutonFlecheGauche.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonFlecheGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheGauche.setStyleSheet("")
        self.boutonFlecheGauche.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/angle-pointing-to-left (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheGauche.setIcon(icon2)
        self.boutonFlecheGauche.setObjectName("boutonFlecheGauche")
        self.horizontalLayout_3.addWidget(self.boutonFlecheGauche)
        self.boutonFlecheDroite = QtWidgets.QPushButton(self.centralwidget)
        self.boutonFlecheDroite.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonFlecheDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDroite.setStyleSheet("")
        self.boutonFlecheDroite.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/angle-arrow-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDroite.setIcon(icon3)
        self.boutonFlecheDroite.setObjectName("boutonFlecheDroite")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDroite)
        self.boutonFlecheDoubleDroite = QtWidgets.QPushButton(self.centralwidget)
        self.boutonFlecheDoubleDroite.setMaximumSize(QtCore.QSize(60, 180))
        self.boutonFlecheDoubleDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleDroite.setStyleSheet("")
        self.boutonFlecheDoubleDroite.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/double-angle-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleDroite.setIcon(icon4)
        self.boutonFlecheDoubleDroite.setObjectName("boutonFlecheDoubleDroite")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleDroite)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(220, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.labelBonTravail = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBonTravail.setFont(font)
        self.labelBonTravail.setObjectName("labelBonTravail")
        self.verticalLayout.addWidget(self.labelBonTravail)
        self.labelEcritureBonTravail = QtWidgets.QLabel(self.centralwidget)
        self.labelEcritureBonTravail.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureBonTravail.setFont(font)
        self.labelEcritureBonTravail.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247;)\n"
"}\n"
"")
        self.labelEcritureBonTravail.setObjectName("labelEcritureBonTravail")
        self.verticalLayout.addWidget(self.labelEcritureBonTravail)
        self.labelDate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.verticalLayout.addWidget(self.labelDate)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QDateEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"color: black;\n"
"background:rgb(247,247,247)\n"
"}\n"
"\n"
"\n"
"")
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2016, 2, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.labelTempsEstime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTempsEstime.setFont(font)
        self.labelTempsEstime.setObjectName("labelTempsEstime")
        self.verticalLayout.addWidget(self.labelTempsEstime)
        self.timeEditTempsEstime = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEditTempsEstime.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEditTempsEstime.setFont(font)
        self.timeEditTempsEstime.setStyleSheet("QTimeEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}")
        self.timeEditTempsEstime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEditTempsEstime.setCalendarPopup(True)
        self.timeEditTempsEstime.setObjectName("timeEditTempsEstime")
        self.verticalLayout.addWidget(self.timeEditTempsEstime)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelDescSituation = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescSituation.setFont(font)
        self.labelDescSituation.setObjectName("labelDescSituation")
        self.verticalLayout_2.addWidget(self.labelDescSituation)
        self.textEditDescSituation = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditDescSituation.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescSituation.setFont(font)
        self.textEditDescSituation.setStyleSheet("")
        self.textEditDescSituation.setObjectName("textEditDescSituation")
        self.verticalLayout_2.addWidget(self.textEditDescSituation)
        spacerItem9 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem9)
        self.labelDescIntervention = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescIntervention.setFont(font)
        self.labelDescIntervention.setObjectName("labelDescIntervention")
        self.verticalLayout_2.addWidget(self.labelDescIntervention)
        self.textEditDescIntervention = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditDescIntervention.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescIntervention.setFont(font)
        self.textEditDescIntervention.setStyleSheet("")
        self.textEditDescIntervention.setObjectName("textEditDescIntervention")
        self.verticalLayout_2.addWidget(self.textEditDescIntervention)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(40, 45, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.comboBoxOuvertFerme = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxOuvertFerme.setFont(font)
        self.comboBoxOuvertFerme.setStyleSheet("QComboBox {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}")
        self.comboBoxOuvertFerme.setObjectName("comboBoxOuvertFerme")
        self.comboBoxOuvertFerme.addItem("")
        self.comboBoxOuvertFerme.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBoxOuvertFerme)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(50, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(self.centralwidget)
        MainWindow.setLayout(layoutVertical)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitre.setText(_translate("MainWindow", "Bon de travail - Maintenance & réparation"))
        self.labelCategorieEquip.setText(_translate("MainWindow", "Catégorie d\'équipement"))
        self.labelEcritureCatEquip.setText(_translate("MainWindow", "Respirateur"))
        self.label_ID.setText(_translate("MainWindow", "ID"))
        self.labelSalle.setText(_translate("MainWindow", "Salle"))
        self.labelCentreService.setText(_translate("MainWindow", "Centre de service"))
        self.labelModele.setText(_translate("MainWindow", "Modèle"))
        self.labelEcritureMarque.setText(_translate("MainWindow", "GE"))
        self.labelEcritureModele.setText(_translate("MainWindow", "2.0"))
        self.labelMarque.setText(_translate("MainWindow", "Marque"))
        self.labelEcritureCentreService.setText(_translate("MainWindow", "xxx"))
        self.labelEcritureSalle.setText(_translate("MainWindow", "Urgence"))
        self.labelBonTravail.setText(_translate("MainWindow", "# Bon de travail"))
        self.labelEcritureBonTravail.setText(_translate("MainWindow", "62-2"))
        self.labelDate.setText(_translate("MainWindow", "Date"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.labelTempsEstime.setText(_translate("MainWindow", "Temps estimé (h:m)"))
        self.timeEditTempsEstime.setDisplayFormat(_translate("MainWindow", "h:mm"))
        self.labelDescSituation.setText(_translate("MainWindow", "Description de la situation"))
        self.labelDescIntervention.setText(_translate("MainWindow", "Description de l\'intervention"))
        self.comboBoxOuvertFerme.setItemText(0, _translate("MainWindow", "Ouvert"))
        self.comboBoxOuvertFerme.setItemText(1, _translate("MainWindow", "Fermé"))

        self.labelEcritureBonTravail.setText("")

        self.lineEditID.returnPressed.connect(self.chercherEquipement)
        self.equipementManager = EquipementManager('DataBase_Equipement.json')
        self.bonDeTravailManager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')
        self.equipementDictionnaire = dict()
        self.listeBonDeTravail = list()
        self.indiceBonDeTravail = 0

        self.boutonSauvegarde.clicked.connect(self.sauvegarderBonDeTravail)
        self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
        self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
        self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
        self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)

    def chercherEquipement(self):
        # chercherEquipementParId(self.identifiantEdit.text())
        # self.remplissageFormulaire()
        # print(self.equipementManager.RechercherEquipement(self.identifiantEdit.text()))
        dic_request = dict()
        dic_request['ID'] = self.lineEditID.text()
        listeTrouve = self.equipementManager.RechercherEquipement(dic_request)
        if(any(listeTrouve)):
            self.equipementDictionnaire = listeTrouve[0]
            self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
            self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
            self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
            self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
            self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])
            self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"ID-EQ": self.lineEditID.text()})
            self.indiceBonDeTravail = 0
            self.chargerBonTravail()
        else:
            self.labelEcritureCatEquip.setText("")
            self.labelEcritureCentreService.setText("")
            self.labelEcritureMarque.setText("")
            self.labelEcritureSalle.setText("")
            self.labelEcritureModele.setText("")
            self.listeBonDeTravail.clear()
        print(self.listeBonDeTravail)


    def sauvegarderBonDeTravail(self):
        dictionnaireDonnees = dict()
        dictionnaireDonnees["Date"] = self.dateEdit.date().toPyDate()
        dictionnaireDonnees["TempsEstime"] = str(self.timeEditTempsEstime.time().toPyTime())
        dictionnaireDonnees["DescriptionSituation"] = self.textEditDescSituation.toPlainText()
        dictionnaireDonnees["DescriptionIntervention"] = self.textEditDescIntervention.toPlainText()
        dictionnaireDonnees["EtatBDT"] = self.comboBoxOuvertFerme.currentText()
        if(any(self.equipementDictionnaire)):
            self.bonDeTravailManager.AjouterBonTravail(self.equipementDictionnaire["ID"], dictionnaireDonnees)

    def chargerBonTravail(self):
        if(any(self.listeBonDeTravail)):
            self.dateEdit.setDate(self.listeBonDeTravail[self.indiceBonDeTravail]["Date"])
            self.textEditDescSituation.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"])
            self.textEditDescSituation.wordWrapMode()
            self.textEditDescIntervention.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"])
            self.textEditDescIntervention.wordWrapMode()
            #Remplir le temps estime
            #self.timeEditTempsEstime.setTime("")
            self.comboBoxOuvertFerme.setCurrentText(self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"])
            idBDT = str(self.equipementDictionnaire["ID"]) + "-" + str(self.indiceBonDeTravail + 1)
            self.labelEcritureBonTravail.setText(idBDT)

    def bonTravailSuivant(self):
        if(self.indiceBonDeTravail < len(self.listeBonDeTravail) - 1):
            self.indiceBonDeTravail += 1
            self.chargerBonTravail()

    def bonTravailPrecedent(self):
        if (self.indiceBonDeTravail > 0):
            self.indiceBonDeTravail -= 1
            self.chargerBonTravail()

    def bonTravailPremier(self):
        self.indiceBonDeTravail = 0
        self.chargerBonTravail()

    def bonTravailDernier(self):
        self.indiceBonDeTravail = len(self.listeBonDeTravail) - 1
        self.chargerBonTravail()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = BonDeTravailUI()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())


