# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuppressionBonDeTravail.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SuppressionBonDeTravail(object):
    def setupUi(self, SuppressionBonDeTravail):
        SuppressionBonDeTravail.setObjectName("SuppressionBonDeTravail")
        SuppressionBonDeTravail.resize(837, 710)
        SuppressionBonDeTravail.setStyleSheet("background: white;")
        self.gridLayout = QtWidgets.QGridLayout(SuppressionBonDeTravail)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPhotoPlus = QtWidgets.QLabel(SuppressionBonDeTravail)
        self.labelPhotoPlus.setMaximumSize(QtCore.QSize(100, 100))
        self.labelPhotoPlus.setStyleSheet("background:white;")
        self.labelPhotoPlus.setText("")
        self.labelPhotoPlus.setPixmap(QtGui.QPixmap("Images/garbage (1).png"))
        self.labelPhotoPlus.setScaledContents(False)
        self.labelPhotoPlus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPhotoPlus.setObjectName("labelPhotoPlus")
        self.horizontalLayout.addWidget(self.labelPhotoPlus)
        self.labelTitre = QtWidgets.QLabel(SuppressionBonDeTravail)
        self.labelTitre.setMaximumSize(QtCore.QSize(20000, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitre.setFont(font)
        self.labelTitre.setAutoFillBackground(False)
        self.labelTitre.setStyleSheet("background:white;")
        self.labelTitre.setObjectName("labelTitre")
        self.horizontalLayout.addWidget(self.labelTitre)
        spacerItem = QtWidgets.QSpacerItem(40, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_ID = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ID.setFont(font)
        self.label_ID.setStyleSheet("background:white;")
        self.label_ID.setObjectName("label_ID")
        self.verticalLayout_6.addWidget(self.label_ID)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(290, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)
        self.boutonActualiser = QtWidgets.QPushButton(SuppressionBonDeTravail)
        self.boutonActualiser.setMaximumSize(QtCore.QSize(42, 38))
        self.boutonActualiser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonActualiser.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 30px;\n"
"max-width:30px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        self.boutonActualiser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/actualize-arrows-couple-in-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon)
        self.boutonActualiser.setIconSize(QtCore.QSize(30, 30))
        self.boutonActualiser.setObjectName("boutonActualiser")
        self.gridLayout_2.addWidget(self.boutonActualiser, 1, 2, 1, 1)
        self.lineEditID = QtWidgets.QLineEdit(SuppressionBonDeTravail)
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
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.labelCategorieEquip = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorieEquip.setFont(font)
        self.labelCategorieEquip.setStyleSheet("background:white;")
        self.labelCategorieEquip.setObjectName("labelCategorieEquip")
        self.verticalLayout_6.addWidget(self.labelCategorieEquip)
        self.labelEcritureCatEquip = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureCatEquip.setFont(font)
        self.labelEcritureCatEquip.setStyleSheet(" QLabel{\n"
"max-width:200px;\n"
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
        self.labelSalle = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setStyleSheet("background:white;")
        self.labelSalle.setObjectName("labelSalle")
        self.gridLayout_3.addWidget(self.labelSalle, 3, 2, 1, 1)
        self.labelCentreService = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCentreService.setFont(font)
        self.labelCentreService.setStyleSheet("background:white;")
        self.labelCentreService.setObjectName("labelCentreService")
        self.gridLayout_3.addWidget(self.labelCentreService, 3, 1, 1, 1)
        self.labelModele = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelModele.setFont(font)
        self.labelModele.setStyleSheet("background:white;")
        self.labelModele.setObjectName("labelModele")
        self.gridLayout_3.addWidget(self.labelModele, 0, 2, 1, 1)
        self.labelEcritureMarque = QtWidgets.QLabel(SuppressionBonDeTravail)
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
        self.labelEcritureModele = QtWidgets.QLabel(SuppressionBonDeTravail)
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
        self.labelMarque = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMarque.setFont(font)
        self.labelMarque.setStyleSheet("background:white;")
        self.labelMarque.setObjectName("labelMarque")
        self.gridLayout_3.addWidget(self.labelMarque, 0, 1, 1, 1)
        self.labelEcritureCentreService = QtWidgets.QLabel(SuppressionBonDeTravail)
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
        self.labelEcritureSalle = QtWidgets.QLabel(SuppressionBonDeTravail)
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
        spacerItem3 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.boutonSupprimerBon = QtWidgets.QPushButton(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonSupprimerBon.setFont(font)
        self.boutonSupprimerBon.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 150px;\n"
"max-width:150px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/garbage (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSupprimerBon.setIcon(icon1)
        self.boutonSupprimerBon.setIconSize(QtCore.QSize(24, 24))
        self.boutonSupprimerBon.setObjectName("boutonSupprimerBon")
        self.horizontalLayout_4.addWidget(self.boutonSupprimerBon)
        self.boutonFlecheDoubleGauche = QtWidgets.QPushButton(SuppressionBonDeTravail)
        self.boutonFlecheDoubleGauche.setMaximumSize(QtCore.QSize(27, 38))
        self.boutonFlecheDoubleGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleGauche.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 15px;\n"
"max-width:15px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        self.boutonFlecheDoubleGauche.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/double-left-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleGauche.setIcon(icon2)
        self.boutonFlecheDoubleGauche.setObjectName("boutonFlecheDoubleGauche")
        self.horizontalLayout_4.addWidget(self.boutonFlecheDoubleGauche)
        self.boutonFlecheGauche = QtWidgets.QPushButton(SuppressionBonDeTravail)
        self.boutonFlecheGauche.setMaximumSize(QtCore.QSize(27, 38))
        self.boutonFlecheGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheGauche.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 15px;\n"
"max-width:15px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        self.boutonFlecheGauche.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/angle-pointing-to-left (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheGauche.setIcon(icon3)
        self.boutonFlecheGauche.setObjectName("boutonFlecheGauche")
        self.horizontalLayout_4.addWidget(self.boutonFlecheGauche)
        self.boutonFlecheDroite = QtWidgets.QPushButton(SuppressionBonDeTravail)
        self.boutonFlecheDroite.setMaximumSize(QtCore.QSize(27, 38))
        self.boutonFlecheDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDroite.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 15px;\n"
"max-width:15px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        self.boutonFlecheDroite.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/angle-arrow-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDroite.setIcon(icon4)
        self.boutonFlecheDroite.setObjectName("boutonFlecheDroite")
        self.horizontalLayout_4.addWidget(self.boutonFlecheDroite)
        self.boutonFlecheDoubleDroite = QtWidgets.QPushButton(SuppressionBonDeTravail)
        self.boutonFlecheDoubleDroite.setMaximumSize(QtCore.QSize(27, 38))
        self.boutonFlecheDoubleDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleDroite.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color:rgb(245, 245, 245);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 15px;\n"
"max-width:15px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        self.boutonFlecheDoubleDroite.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/double-angle-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleDroite.setIcon(icon5)
        self.boutonFlecheDoubleDroite.setObjectName("boutonFlecheDoubleDroite")
        self.horizontalLayout_4.addWidget(self.boutonFlecheDoubleDroite)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(220, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem6)
        self.labelBonTravail = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBonTravail.setFont(font)
        self.labelBonTravail.setStyleSheet("background:white;")
        self.labelBonTravail.setObjectName("labelBonTravail")
        self.verticalLayout_3.addWidget(self.labelBonTravail)
        self.labelEcritureBonTravail = QtWidgets.QLabel(SuppressionBonDeTravail)
        self.labelEcritureBonTravail.setMaximumSize(QtCore.QSize(104, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureBonTravail.setFont(font)
        self.labelEcritureBonTravail.setStyleSheet(" QLabel{\n"
"max-width:100px;\n"
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
        self.verticalLayout_3.addWidget(self.labelEcritureBonTravail)
        self.labelNomTechnicien = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNomTechnicien.setFont(font)
        self.labelNomTechnicien.setStyleSheet("background:white;")
        self.labelNomTechnicien.setObjectName("labelNomTechnicien")
        self.verticalLayout_3.addWidget(self.labelNomTechnicien)
        self.comboBoxNomTech = QtWidgets.QComboBox(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNomTech.setFont(font)
        self.comboBoxNomTech.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"backround:rgb(245, 245, 245);\n"
"}\n"
"    ")
        self.comboBoxNomTech.setObjectName("comboBoxNomTech")
        self.comboBoxNomTech.addItem("")
        self.verticalLayout_3.addWidget(self.comboBoxNomTech)
        self.labelCacheNomTech = QtWidgets.QLabel(SuppressionBonDeTravail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCacheNomTech.sizePolicy().hasHeightForWidth())
        self.labelCacheNomTech.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheNomTech.setFont(font)
        self.labelCacheNomTech.setStyleSheet("background:white;")
        self.labelCacheNomTech.setObjectName("labelCacheNomTech")
        self.verticalLayout_3.addWidget(self.labelCacheNomTech)
        self.labelDate = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.verticalLayout_3.addWidget(self.labelDate)
        self.dateEdit = QtWidgets.QDateEdit(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("max-width:100px;")
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2016, 2, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_3.addWidget(self.dateEdit)
        self.labelCacheDate = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDate.setFont(font)
        self.labelCacheDate.setStyleSheet("background:white;")
        self.labelCacheDate.setObjectName("labelCacheDate")
        self.verticalLayout_3.addWidget(self.labelCacheDate)
        self.labelTempsEstime = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTempsEstime.setFont(font)
        self.labelTempsEstime.setObjectName("labelTempsEstime")
        self.verticalLayout_3.addWidget(self.labelTempsEstime)
        self.timeEditTempsEstime = QtWidgets.QTimeEdit(SuppressionBonDeTravail)
        self.timeEditTempsEstime.setMaximumSize(QtCore.QSize(64, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEditTempsEstime.setFont(font)
        self.timeEditTempsEstime.setStyleSheet("QTimeEdit {\n"
"max-width:60px;\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}")
        self.timeEditTempsEstime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEditTempsEstime.setCalendarPopup(True)
        self.timeEditTempsEstime.setObjectName("timeEditTempsEstime")
        self.verticalLayout_3.addWidget(self.timeEditTempsEstime)
        self.labelCacheTemps = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheTemps.setFont(font)
        self.labelCacheTemps.setStyleSheet("background:white;")
        self.labelCacheTemps.setObjectName("labelCacheTemps")
        self.verticalLayout_3.addWidget(self.labelCacheTemps)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelDescSituation = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescSituation.setFont(font)
        self.labelDescSituation.setStyleSheet("background:white;")
        self.labelDescSituation.setObjectName("labelDescSituation")
        self.verticalLayout_4.addWidget(self.labelDescSituation)
        self.textEditDescSituation = QtWidgets.QTextEdit(SuppressionBonDeTravail)
        self.textEditDescSituation.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescSituation.setFont(font)
        self.textEditDescSituation.setStyleSheet("QTextEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)\n"
"}")
        self.textEditDescSituation.setObjectName("textEditDescSituation")
        self.verticalLayout_4.addWidget(self.textEditDescSituation)
        self.labelCacheDescSit = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDescSit.setFont(font)
        self.labelCacheDescSit.setStyleSheet("background:white;")
        self.labelCacheDescSit.setObjectName("labelCacheDescSit")
        self.verticalLayout_4.addWidget(self.labelCacheDescSit)
        spacerItem9 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem9)
        self.labelDescIntervention = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescIntervention.setFont(font)
        self.labelDescIntervention.setStyleSheet("background:white;")
        self.labelDescIntervention.setObjectName("labelDescIntervention")
        self.verticalLayout_4.addWidget(self.labelDescIntervention)
        self.textEditDescIntervention = QtWidgets.QTextEdit(SuppressionBonDeTravail)
        self.textEditDescIntervention.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescIntervention.setFont(font)
        self.textEditDescIntervention.setStyleSheet("QTextEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)\n"
"}")
        self.textEditDescIntervention.setObjectName("textEditDescIntervention")
        self.verticalLayout_4.addWidget(self.textEditDescIntervention)
        self.labelCacheDescInt = QtWidgets.QLabel(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDescInt.setFont(font)
        self.labelCacheDescInt.setStyleSheet("background:white;")
        self.labelCacheDescInt.setObjectName("labelCacheDescInt")
        self.verticalLayout_4.addWidget(self.labelCacheDescInt)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(40, 45, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.comboBoxOuvertFerme = QtWidgets.QComboBox(SuppressionBonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxOuvertFerme.setFont(font)
        self.comboBoxOuvertFerme.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    max-width: 55px;\n"
"backround:rgb(245, 245, 245);\n"
"}\n"
"    ")
        self.comboBoxOuvertFerme.setObjectName("comboBoxOuvertFerme")
        self.comboBoxOuvertFerme.addItem("")
        self.comboBoxOuvertFerme.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBoxOuvertFerme)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem11 = QtWidgets.QSpacerItem(50, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_10.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.verticalLayout_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 2)

        self.retranslateUi(SuppressionBonDeTravail)
        QtCore.QMetaObject.connectSlotsByName(SuppressionBonDeTravail)

    def retranslateUi(self, SuppressionBonDeTravail):
        _translate = QtCore.QCoreApplication.translate
        SuppressionBonDeTravail.setWindowTitle(_translate("SuppressionBonDeTravail", "Form"))
        self.labelTitre.setText(_translate("SuppressionBonDeTravail", "Assistant de Recherche - Suppression de Bons de travail"))
        self.label_ID.setText(_translate("SuppressionBonDeTravail", "ID équipement"))
        self.labelCategorieEquip.setText(_translate("SuppressionBonDeTravail", "Catégorie d\'équipement"))
        self.labelSalle.setText(_translate("SuppressionBonDeTravail", "Salle"))
        self.labelCentreService.setText(_translate("SuppressionBonDeTravail", "Centre de service"))
        self.labelModele.setText(_translate("SuppressionBonDeTravail", "Modèle"))
        self.labelMarque.setText(_translate("SuppressionBonDeTravail", "Marque"))
        self.boutonSupprimerBon.setText(_translate("SuppressionBonDeTravail", "Supprimer le Bon"))
        self.labelBonTravail.setText(_translate("SuppressionBonDeTravail", "ID bon de travail"))
        self.labelNomTechnicien.setText(_translate("SuppressionBonDeTravail", "Nom du technicien"))
        self.comboBoxNomTech.setItemText(0, _translate("SuppressionBonDeTravail", "Kerlin Hyppolite"))
        self.labelCacheNomTech.setText(_translate("SuppressionBonDeTravail", "Ce que j\'ai écrit"))
        self.labelDate.setText(_translate("SuppressionBonDeTravail", "Date"))
        self.dateEdit.setDisplayFormat(_translate("SuppressionBonDeTravail", "dd-MM-yyyy"))
        self.labelCacheDate.setText(_translate("SuppressionBonDeTravail", "Ce que j\'ai écrit"))
        self.labelTempsEstime.setText(_translate("SuppressionBonDeTravail", "Temps estimé (h:m)"))
        self.timeEditTempsEstime.setDisplayFormat(_translate("SuppressionBonDeTravail", "h:mm"))
        self.labelCacheTemps.setText(_translate("SuppressionBonDeTravail", "Ce que j\'ai écrit"))
        self.labelDescSituation.setText(_translate("SuppressionBonDeTravail", "Description de la situation"))
        self.labelCacheDescSit.setText(_translate("SuppressionBonDeTravail", "Ce que j\'ai écrit"))
        self.labelDescIntervention.setText(_translate("SuppressionBonDeTravail", "Description de l\'intervention"))
        self.labelCacheDescInt.setText(_translate("SuppressionBonDeTravail", "Ce que j\'ai écrit"))
        self.comboBoxOuvertFerme.setItemText(0, _translate("SuppressionBonDeTravail", "Ouvert"))
        self.comboBoxOuvertFerme.setItemText(1, _translate("SuppressionBonDeTravail", "Fermé"))

