# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BdT3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BonDeTravail(object):
    def setupUi(self, BonDeTravail):
        BonDeTravail.setObjectName("BonDeTravail")
        BonDeTravail.resize(1157, 876)
        BonDeTravail.setStyleSheet("QWidget\n"
" {\n"
"\n"
"background:white;\n"
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
"}\n"
"\n"
"QComboBox {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BonDeTravail)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPhotoPlus = QtWidgets.QLabel(BonDeTravail)
        self.labelPhotoPlus.setMaximumSize(QtCore.QSize(100, 100))
        self.labelPhotoPlus.setStyleSheet("background: white;\n"
"")
        self.labelPhotoPlus.setText("")
        self.labelPhotoPlus.setPixmap(QtGui.QPixmap("Images/plus.png"))
        self.labelPhotoPlus.setScaledContents(False)
        self.labelPhotoPlus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPhotoPlus.setObjectName("labelPhotoPlus")
        self.horizontalLayout.addWidget(self.labelPhotoPlus)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTitre = QtWidgets.QLabel(BonDeTravail)
        self.labelTitre.setMaximumSize(QtCore.QSize(20000, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitre.setFont(font)
        self.labelTitre.setAutoFillBackground(False)
        self.labelTitre.setStyleSheet("background: white;")
        self.labelTitre.setObjectName("labelTitre")
        self.horizontalLayout.addWidget(self.labelTitre)
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_ID = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ID.setFont(font)
        self.label_ID.setStyleSheet("background: white;\n"
"")
        self.label_ID.setObjectName("label_ID")
        self.verticalLayout_6.addWidget(self.label_ID)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.boutonActualiser = QtWidgets.QPushButton(BonDeTravail)
        self.boutonActualiser.setMaximumSize(QtCore.QSize(100, 40))
        self.boutonActualiser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonActualiser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/actualize-arrows-couple-in-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon)
        self.boutonActualiser.setIconSize(QtCore.QSize(30, 30))
        self.boutonActualiser.setObjectName("boutonActualiser")
        self.gridLayout_2.addWidget(self.boutonActualiser, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(200, 19, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        self.lineEditID = QtWidgets.QLineEdit(BonDeTravail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditID.sizePolicy().hasHeightForWidth())
        self.lineEditID.setSizePolicy(sizePolicy)
        self.lineEditID.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditID.setFont(font)
        self.lineEditID.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid rgb(145, 220, 90);\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}\n"
"")
        self.lineEditID.setObjectName("lineEditID")
        self.gridLayout_2.addWidget(self.lineEditID, 1, 0, 1, 1)
        self.boutonConsultation = QtWidgets.QPushButton(BonDeTravail)
        self.boutonConsultation.setMaximumSize(QtCore.QSize(500, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boutonConsultation.setFont(font)
        self.boutonConsultation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonConsultation.setIconSize(QtCore.QSize(20, 16))
        self.boutonConsultation.setObjectName("boutonConsultation")
        self.gridLayout_2.addWidget(self.boutonConsultation, 1, 4, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.labelCategorieEquip = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorieEquip.setFont(font)
        self.labelCategorieEquip.setStyleSheet("background: white;")
        self.labelCategorieEquip.setObjectName("labelCategorieEquip")
        self.verticalLayout_6.addWidget(self.labelCategorieEquip)
        self.labelEcritureCatEquip = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureCatEquip.setFont(font)
        self.labelEcritureCatEquip.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"\n"
"")
        self.labelEcritureCatEquip.setText("")
        self.labelEcritureCatEquip.setObjectName("labelEcritureCatEquip")
        self.verticalLayout_6.addWidget(self.labelEcritureCatEquip)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelSalle = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setStyleSheet("background: white;")
        self.labelSalle.setObjectName("labelSalle")
        self.gridLayout_3.addWidget(self.labelSalle, 3, 2, 1, 1)
        self.labelCentreService = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCentreService.setFont(font)
        self.labelCentreService.setStyleSheet("background: white;")
        self.labelCentreService.setObjectName("labelCentreService")
        self.gridLayout_3.addWidget(self.labelCentreService, 3, 1, 1, 1)
        self.labelModele = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelModele.setFont(font)
        self.labelModele.setStyleSheet("background: white;")
        self.labelModele.setObjectName("labelModele")
        self.gridLayout_3.addWidget(self.labelModele, 0, 2, 1, 1)
        self.labelEcritureMarque = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureMarque.setFont(font)
        self.labelEcritureMarque.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"")
        self.labelEcritureMarque.setText("")
        self.labelEcritureMarque.setObjectName("labelEcritureMarque")
        self.gridLayout_3.addWidget(self.labelEcritureMarque, 2, 1, 1, 1)
        self.labelEcritureModele = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureModele.setFont(font)
        self.labelEcritureModele.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"")
        self.labelEcritureModele.setText("")
        self.labelEcritureModele.setObjectName("labelEcritureModele")
        self.gridLayout_3.addWidget(self.labelEcritureModele, 2, 2, 1, 1)
        self.labelMarque = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMarque.setFont(font)
        self.labelMarque.setStyleSheet("background: white;")
        self.labelMarque.setObjectName("labelMarque")
        self.gridLayout_3.addWidget(self.labelMarque, 0, 1, 1, 1)
        self.labelEcritureCentreService = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureCentreService.setFont(font)
        self.labelEcritureCentreService.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"")
        self.labelEcritureCentreService.setText("")
        self.labelEcritureCentreService.setObjectName("labelEcritureCentreService")
        self.gridLayout_3.addWidget(self.labelEcritureCentreService, 4, 1, 1, 1)
        self.labelEcritureSalle = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureSalle.setFont(font)
        self.labelEcritureSalle.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"")
        self.labelEcritureSalle.setText("")
        self.labelEcritureSalle.setObjectName("labelEcritureSalle")
        self.gridLayout_3.addWidget(self.labelEcritureSalle, 4, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.boutonAjoutBDT = QtWidgets.QPushButton(BonDeTravail)
        self.boutonAjoutBDT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonAjoutBDT.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/plus_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonAjoutBDT.setIcon(icon1)
        self.boutonAjoutBDT.setIconSize(QtCore.QSize(35, 35))
        self.boutonAjoutBDT.setObjectName("boutonAjoutBDT")
        self.horizontalLayout_3.addWidget(self.boutonAjoutBDT)
        self.boutonSauvegarde = QtWidgets.QPushButton(BonDeTravail)
        self.boutonSauvegarde.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonSauvegarde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonSauvegarde.setAutoFillBackground(False)
        self.boutonSauvegarde.setStyleSheet("")
        self.boutonSauvegarde.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSauvegarde.setIcon(icon2)
        self.boutonSauvegarde.setIconSize(QtCore.QSize(35, 35))
        self.boutonSauvegarde.setObjectName("boutonSauvegarde")
        self.horizontalLayout_3.addWidget(self.boutonSauvegarde)
        self.boutonFlecheDoubleGauche = QtWidgets.QPushButton(BonDeTravail)
        self.boutonFlecheDoubleGauche.setMaximumSize(QtCore.QSize(50, 150))
        self.boutonFlecheDoubleGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleGauche.setStyleSheet("")
        self.boutonFlecheDoubleGauche.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/double-left-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleGauche.setIcon(icon3)
        self.boutonFlecheDoubleGauche.setObjectName("boutonFlecheDoubleGauche")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleGauche)
        self.boutonFlecheGauche = QtWidgets.QPushButton(BonDeTravail)
        self.boutonFlecheGauche.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonFlecheGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheGauche.setStyleSheet("")
        self.boutonFlecheGauche.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/angle-pointing-to-left (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheGauche.setIcon(icon4)
        self.boutonFlecheGauche.setObjectName("boutonFlecheGauche")
        self.horizontalLayout_3.addWidget(self.boutonFlecheGauche)
        self.boutonFlecheDroite = QtWidgets.QPushButton(BonDeTravail)
        self.boutonFlecheDroite.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonFlecheDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDroite.setStyleSheet("")
        self.boutonFlecheDroite.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/angle-arrow-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDroite.setIcon(icon5)
        self.boutonFlecheDroite.setObjectName("boutonFlecheDroite")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDroite)
        self.boutonFlecheDoubleDroite = QtWidgets.QPushButton(BonDeTravail)
        self.boutonFlecheDoubleDroite.setMaximumSize(QtCore.QSize(60, 180))
        self.boutonFlecheDoubleDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleDroite.setStyleSheet("")
        self.boutonFlecheDoubleDroite.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/double-angle-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleDroite.setIcon(icon6)
        self.boutonFlecheDoubleDroite.setObjectName("boutonFlecheDoubleDroite")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleDroite)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(220, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.labelBonTravail = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBonTravail.setFont(font)
        self.labelBonTravail.setStyleSheet("background: white;")
        self.labelBonTravail.setObjectName("labelBonTravail")
        self.verticalLayout.addWidget(self.labelBonTravail)
        self.labelEcritureBonTravail = QtWidgets.QLabel(BonDeTravail)
        self.labelEcritureBonTravail.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureBonTravail.setFont(font)
        self.labelEcritureBonTravail.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"")
        self.labelEcritureBonTravail.setText("")
        self.labelEcritureBonTravail.setObjectName("labelEcritureBonTravail")
        self.verticalLayout.addWidget(self.labelEcritureBonTravail)
        self.labelNomTechnicien = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNomTechnicien.setFont(font)
        self.labelNomTechnicien.setStyleSheet("background: white;")
        self.labelNomTechnicien.setObjectName("labelNomTechnicien")
        self.verticalLayout.addWidget(self.labelNomTechnicien)
        self.comboBoxNomTech = QtWidgets.QComboBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNomTech.setFont(font)
        self.comboBoxNomTech.setStyleSheet("")
        self.comboBoxNomTech.setObjectName("comboBoxNomTech")
        self.comboBoxNomTech.addItem("")
        self.verticalLayout.addWidget(self.comboBoxNomTech)
        self.labelCacheNomTech = QtWidgets.QLabel(BonDeTravail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCacheNomTech.sizePolicy().hasHeightForWidth())
        self.labelCacheNomTech.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheNomTech.setFont(font)
        self.labelCacheNomTech.setStyleSheet("background: white;")
        self.labelCacheNomTech.setObjectName("labelCacheNomTech")
        self.verticalLayout.addWidget(self.labelCacheNomTech)
        self.labelDate = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDate.setFont(font)
        self.labelDate.setStyleSheet("background: white;")
        self.labelDate.setObjectName("labelDate")
        self.verticalLayout.addWidget(self.labelDate)
        self.dateEdit = QtWidgets.QDateEdit(BonDeTravail)
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
        self.labelCacheDate = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDate.setFont(font)
        self.labelCacheDate.setStyleSheet("background: white;")
        self.labelCacheDate.setObjectName("labelCacheDate")
        self.verticalLayout.addWidget(self.labelCacheDate)
        self.labelTempsEstime = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTempsEstime.setFont(font)
        self.labelTempsEstime.setStyleSheet("background: white;")
        self.labelTempsEstime.setObjectName("labelTempsEstime")
        self.verticalLayout.addWidget(self.labelTempsEstime)
        self.timeEditTempsEstime = QtWidgets.QTimeEdit(BonDeTravail)
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
        self.labelCacheTemps = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheTemps.setFont(font)
        self.labelCacheTemps.setStyleSheet("background: white;")
        self.labelCacheTemps.setObjectName("labelCacheTemps")
        self.verticalLayout.addWidget(self.labelCacheTemps)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelDescSituation = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescSituation.setFont(font)
        self.labelDescSituation.setStyleSheet("background: white;")
        self.labelDescSituation.setObjectName("labelDescSituation")
        self.verticalLayout_2.addWidget(self.labelDescSituation)
        self.textEditDescSituation = QtWidgets.QTextEdit(BonDeTravail)
        self.textEditDescSituation.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescSituation.setFont(font)
        self.textEditDescSituation.setStyleSheet("")
        self.textEditDescSituation.setObjectName("textEditDescSituation")
        self.verticalLayout_2.addWidget(self.textEditDescSituation)
        self.labelCacheDescSit = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDescSit.setFont(font)
        self.labelCacheDescSit.setStyleSheet("background: white;")
        self.labelCacheDescSit.setObjectName("labelCacheDescSit")
        self.verticalLayout_2.addWidget(self.labelCacheDescSit)
        spacerItem10 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem10)
        self.labelDescIntervention = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescIntervention.setFont(font)
        self.labelDescIntervention.setStyleSheet("background: white;")
        self.labelDescIntervention.setObjectName("labelDescIntervention")
        self.verticalLayout_2.addWidget(self.labelDescIntervention)
        self.textEditDescIntervention = QtWidgets.QTextEdit(BonDeTravail)
        self.textEditDescIntervention.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescIntervention.setFont(font)
        self.textEditDescIntervention.setStyleSheet("")
        self.textEditDescIntervention.setObjectName("textEditDescIntervention")
        self.verticalLayout_2.addWidget(self.textEditDescIntervention)
        self.labelCacheDescInt = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDescInt.setFont(font)
        self.labelCacheDescInt.setStyleSheet("background: white;")
        self.labelCacheDescInt.setObjectName("labelCacheDescInt")
        self.verticalLayout_2.addWidget(self.labelCacheDescInt)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(40, 45, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.comboBoxOuvertFerme = QtWidgets.QComboBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxOuvertFerme.setFont(font)
        self.comboBoxOuvertFerme.setStyleSheet("")
        self.comboBoxOuvertFerme.setObjectName("comboBoxOuvertFerme")
        self.comboBoxOuvertFerme.addItem("")
        self.comboBoxOuvertFerme.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBoxOuvertFerme)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem12 = QtWidgets.QSpacerItem(50, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.retranslateUi(BonDeTravail)
        QtCore.QMetaObject.connectSlotsByName(BonDeTravail)

    def retranslateUi(self, BonDeTravail):
        _translate = QtCore.QCoreApplication.translate
        BonDeTravail.setWindowTitle(_translate("BonDeTravail", "Form"))
        self.labelTitre.setText(_translate("BonDeTravail", "Bon de travail - Maintenance & réparation"))
        self.label_ID.setText(_translate("BonDeTravail", "ID équipement"))
        self.boutonConsultation.setText(_translate("BonDeTravail", "Consultation d\'un bon de travail"))
        self.labelCategorieEquip.setText(_translate("BonDeTravail", "Catégorie d\'équipement"))
        self.labelSalle.setText(_translate("BonDeTravail", "Salle"))
        self.labelCentreService.setText(_translate("BonDeTravail", "Centre de service"))
        self.labelModele.setText(_translate("BonDeTravail", "Modèle"))
        self.labelMarque.setText(_translate("BonDeTravail", "Marque"))
        self.labelBonTravail.setText(_translate("BonDeTravail", "ID bon de travail"))
        self.labelNomTechnicien.setText(_translate("BonDeTravail", "Nom du technicien"))
        self.comboBoxNomTech.setItemText(0, _translate("BonDeTravail", "Kerlin Hyppolite"))
        self.labelCacheNomTech.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelDate.setText(_translate("BonDeTravail", "Date"))
        self.dateEdit.setDisplayFormat(_translate("BonDeTravail", "dd-MM-yyyy"))
        self.labelCacheDate.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelTempsEstime.setText(_translate("BonDeTravail", "Temps estimé (h:m)"))
        self.timeEditTempsEstime.setDisplayFormat(_translate("BonDeTravail", "h:mm"))
        self.labelCacheTemps.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelDescSituation.setText(_translate("BonDeTravail", "Description de la situation"))
        self.labelCacheDescSit.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelDescIntervention.setText(_translate("BonDeTravail", "Description de l\'intervention"))
        self.labelCacheDescInt.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.comboBoxOuvertFerme.setItemText(0, _translate("BonDeTravail", "Ouvert"))
        self.comboBoxOuvertFerme.setItemText(1, _translate("BonDeTravail", "Fermé"))

