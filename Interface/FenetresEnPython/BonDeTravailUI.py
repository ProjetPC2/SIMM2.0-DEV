# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BondeTravail.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from win32api import GetSystemMetrics
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BonDeTravail(object):
    def setupUi(self, BonDeTravail):
        BonDeTravail.setObjectName(_fromUtf8("BonDeTravail"))
        width = GetSystemMetrics(0)
        heigth = GetSystemMetrics(1)
        facteur_grandissement_width = 0.9
        facteur_grandissement_heigth = 0.7
        BonDeTravail.resize(width * facteur_grandissement_width, heigth * facteur_grandissement_heigth)
        #BonDeTravail.resize(1440, 921)
        BonDeTravail.setMaximumSize(QtCore.QSize(16777125, 16777125))
        BonDeTravail.setStyleSheet(_fromUtf8("QWidget\n"
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
"}"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(BonDeTravail)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelPhotoPlus = QtGui.QLabel(BonDeTravail)
        self.labelPhotoPlus.setMaximumSize(QtCore.QSize(100, 100))
        self.labelPhotoPlus.setStyleSheet(_fromUtf8("background: white;\n"
""))
        self.labelPhotoPlus.setText(_fromUtf8(""))
        self.labelPhotoPlus.setPixmap(QtGui.QPixmap(_fromUtf8("Images/plus.png")))
        self.labelPhotoPlus.setScaledContents(False)
        self.labelPhotoPlus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPhotoPlus.setObjectName(_fromUtf8("labelPhotoPlus"))
        self.horizontalLayout.addWidget(self.labelPhotoPlus)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTitre = QtGui.QLabel(BonDeTravail)
        self.labelTitre.setMaximumSize(QtCore.QSize(20000, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitre.setFont(font)
        self.labelTitre.setAutoFillBackground(False)
        self.labelTitre.setStyleSheet(_fromUtf8("background: white;"))
        self.labelTitre.setObjectName(_fromUtf8("labelTitre"))
        self.horizontalLayout.addWidget(self.labelTitre)
        spacerItem1 = QtGui.QSpacerItem(40, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 23, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_ID = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ID.setFont(font)
        self.label_ID.setStyleSheet(_fromUtf8("background: white;\n"
""))
        self.label_ID.setObjectName(_fromUtf8("label_ID"))
        self.verticalLayout_6.addWidget(self.label_ID)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.boutonActualiser = QtGui.QPushButton(BonDeTravail)
        self.boutonActualiser.setMaximumSize(QtCore.QSize(100, 40))
        self.boutonActualiser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonActualiser.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/actualize-arrows-couple-in-circle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon)
        self.boutonActualiser.setIconSize(QtCore.QSize(30, 30))
        self.boutonActualiser.setObjectName(_fromUtf8("boutonActualiser"))
        self.gridLayout_2.addWidget(self.boutonActualiser, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(200, 19, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        self.lineEditID = QtGui.QLineEdit(BonDeTravail)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditID.sizePolicy().hasHeightForWidth())
        self.lineEditID.setSizePolicy(sizePolicy)
        self.lineEditID.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditID.setFont(font)
        self.lineEditID.setStyleSheet(_fromUtf8("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid rgb(145, 220, 90);\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}\n"
""))
        self.lineEditID.setObjectName(_fromUtf8("lineEditID"))
        self.gridLayout_2.addWidget(self.lineEditID, 1, 0, 1, 1)
        self.boutonConsultation = QtGui.QPushButton(BonDeTravail)
        self.boutonConsultation.setMaximumSize(QtCore.QSize(500, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boutonConsultation.setFont(font)
        self.boutonConsultation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonConsultation.setIconSize(QtCore.QSize(20, 16))
        self.boutonConsultation.setObjectName(_fromUtf8("boutonConsultation"))
        self.gridLayout_2.addWidget(self.boutonConsultation, 1, 4, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.labelCategorieEquip = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorieEquip.setFont(font)
        self.labelCategorieEquip.setStyleSheet(_fromUtf8("background: white;"))
        self.labelCategorieEquip.setObjectName(_fromUtf8("labelCategorieEquip"))
        self.verticalLayout_6.addWidget(self.labelCategorieEquip)
        self.labelEcritureCatEquip = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureCatEquip.setFont(font)
        self.labelEcritureCatEquip.setStyleSheet(_fromUtf8(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"\n"
""))
        self.labelEcritureCatEquip.setText(_fromUtf8(""))
        self.labelEcritureCatEquip.setObjectName(_fromUtf8("labelEcritureCatEquip"))
        self.verticalLayout_6.addWidget(self.labelEcritureCatEquip)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelSalle = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setStyleSheet(_fromUtf8("background: white;"))
        self.labelSalle.setObjectName(_fromUtf8("labelSalle"))
        self.gridLayout_3.addWidget(self.labelSalle, 3, 2, 1, 1)
        self.labelUnite = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelUnite.setFont(font)
        self.labelUnite.setStyleSheet(_fromUtf8("background: white;"))
        self.labelUnite.setObjectName(_fromUtf8("labelUnite"))
        self.gridLayout_3.addWidget(self.labelUnite, 3, 1, 1, 1)
        self.labelModele = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelModele.setFont(font)
        self.labelModele.setStyleSheet(_fromUtf8("background: white;"))
        self.labelModele.setObjectName(_fromUtf8("labelModele"))
        self.gridLayout_3.addWidget(self.labelModele, 0, 2, 1, 1)
        self.labelEcritureMarque = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureMarque.setFont(font)
        self.labelEcritureMarque.setStyleSheet(_fromUtf8(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
""))
        self.labelEcritureMarque.setText(_fromUtf8(""))
        self.labelEcritureMarque.setObjectName(_fromUtf8("labelEcritureMarque"))
        self.gridLayout_3.addWidget(self.labelEcritureMarque, 2, 1, 1, 1)
        self.labelEcritureModele = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureModele.setFont(font)
        self.labelEcritureModele.setStyleSheet(_fromUtf8(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
""))
        self.labelEcritureModele.setText(_fromUtf8(""))
        self.labelEcritureModele.setObjectName(_fromUtf8("labelEcritureModele"))
        self.gridLayout_3.addWidget(self.labelEcritureModele, 2, 2, 1, 1)
        self.labelMarque = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMarque.setFont(font)
        self.labelMarque.setStyleSheet(_fromUtf8("background: white;"))
        self.labelMarque.setObjectName(_fromUtf8("labelMarque"))
        self.gridLayout_3.addWidget(self.labelMarque, 0, 1, 1, 1)
        self.labelEcritureUnite = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureUnite.setFont(font)
        self.labelEcritureUnite.setStyleSheet(_fromUtf8(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
""))
        self.labelEcritureUnite.setText(_fromUtf8(""))
        self.labelEcritureUnite.setObjectName(_fromUtf8("labelEcritureUnite"))
        self.gridLayout_3.addWidget(self.labelEcritureUnite, 4, 1, 1, 1)
        self.labelEcritureSalle = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureSalle.setFont(font)
        self.labelEcritureSalle.setStyleSheet(_fromUtf8(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
""))
        self.labelEcritureSalle.setText(_fromUtf8(""))
        self.labelEcritureSalle.setObjectName(_fromUtf8("labelEcritureSalle"))
        self.gridLayout_3.addWidget(self.labelEcritureSalle, 4, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem4 = QtGui.QSpacerItem(30, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        spacerItem6 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem6)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.boutonAjoutBDT = QtGui.QPushButton(BonDeTravail)
        self.boutonAjoutBDT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonAjoutBDT.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Images/plus_64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonAjoutBDT.setIcon(icon1)
        self.boutonAjoutBDT.setIconSize(QtCore.QSize(35, 35))
        self.boutonAjoutBDT.setObjectName(_fromUtf8("boutonAjoutBDT"))
        self.horizontalLayout_3.addWidget(self.boutonAjoutBDT)
        self.boutonSauvegarde = QtGui.QPushButton(BonDeTravail)
        self.boutonSauvegarde.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonSauvegarde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonSauvegarde.setAutoFillBackground(False)
        self.boutonSauvegarde.setStyleSheet(_fromUtf8(""))
        self.boutonSauvegarde.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Images/save (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSauvegarde.setIcon(icon2)
        self.boutonSauvegarde.setIconSize(QtCore.QSize(35, 35))
        self.boutonSauvegarde.setObjectName(_fromUtf8("boutonSauvegarde"))
        self.horizontalLayout_3.addWidget(self.boutonSauvegarde)
        self.boutonFlecheDoubleGauche = QtGui.QPushButton(BonDeTravail)
        self.boutonFlecheDoubleGauche.setMaximumSize(QtCore.QSize(50, 150))
        self.boutonFlecheDoubleGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleGauche.setStyleSheet(_fromUtf8(""))
        self.boutonFlecheDoubleGauche.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Images/double-left-chevron.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleGauche.setIcon(icon3)
        self.boutonFlecheDoubleGauche.setObjectName(_fromUtf8("boutonFlecheDoubleGauche"))
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleGauche)
        self.boutonFlecheGauche = QtGui.QPushButton(BonDeTravail)
        self.boutonFlecheGauche.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonFlecheGauche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheGauche.setStyleSheet(_fromUtf8(""))
        self.boutonFlecheGauche.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Images/angle-pointing-to-left (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheGauche.setIcon(icon4)
        self.boutonFlecheGauche.setObjectName(_fromUtf8("boutonFlecheGauche"))
        self.horizontalLayout_3.addWidget(self.boutonFlecheGauche)
        self.boutonFlecheDroite = QtGui.QPushButton(BonDeTravail)
        self.boutonFlecheDroite.setMaximumSize(QtCore.QSize(50, 180))
        self.boutonFlecheDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDroite.setStyleSheet(_fromUtf8(""))
        self.boutonFlecheDroite.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Images/angle-arrow-pointing-to-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDroite.setIcon(icon5)
        self.boutonFlecheDroite.setObjectName(_fromUtf8("boutonFlecheDroite"))
        self.horizontalLayout_3.addWidget(self.boutonFlecheDroite)
        self.boutonFlecheDoubleDroite = QtGui.QPushButton(BonDeTravail)
        self.boutonFlecheDoubleDroite.setMaximumSize(QtCore.QSize(60, 180))
        self.boutonFlecheDoubleDroite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonFlecheDoubleDroite.setStyleSheet(_fromUtf8(""))
        self.boutonFlecheDoubleDroite.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Images/double-angle-pointing-to-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleDroite.setIcon(icon6)
        self.boutonFlecheDoubleDroite.setObjectName(_fromUtf8("boutonFlecheDoubleDroite"))
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleDroite)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtGui.QSpacerItem(220, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.labelBonTravail = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBonTravail.setFont(font)
        self.labelBonTravail.setStyleSheet(_fromUtf8("background: white;"))
        self.labelBonTravail.setObjectName(_fromUtf8("labelBonTravail"))
        self.verticalLayout.addWidget(self.labelBonTravail)
        self.labelEcritureBonTravail = QtGui.QLabel(BonDeTravail)
        self.labelEcritureBonTravail.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureBonTravail.setFont(font)
        self.labelEcritureBonTravail.setStyleSheet(_fromUtf8(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
""))
        self.labelEcritureBonTravail.setText(_fromUtf8(""))
        self.labelEcritureBonTravail.setObjectName(_fromUtf8("labelEcritureBonTravail"))
        self.verticalLayout.addWidget(self.labelEcritureBonTravail)
        self.labelNomTechnicien = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNomTechnicien.setFont(font)
        self.labelNomTechnicien.setStyleSheet(_fromUtf8("background: white;"))
        self.labelNomTechnicien.setObjectName(_fromUtf8("labelNomTechnicien"))
        self.verticalLayout.addWidget(self.labelNomTechnicien)
        self.comboBoxNomTech = QtGui.QComboBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNomTech.setFont(font)
        self.comboBoxNomTech.setStyleSheet(_fromUtf8(""))
        self.comboBoxNomTech.setObjectName(_fromUtf8("comboBoxNomTech"))
        self.comboBoxNomTech.addItem(_fromUtf8(""))
        self.comboBoxNomTech.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxNomTech)
        self.labelCacheNomTech = QtGui.QLabel(BonDeTravail)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCacheNomTech.sizePolicy().hasHeightForWidth())
        self.labelCacheNomTech.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheNomTech.setFont(font)
        self.labelCacheNomTech.setStyleSheet(_fromUtf8("background: white;"))
        self.labelCacheNomTech.setObjectName(_fromUtf8("labelCacheNomTech"))
        self.verticalLayout.addWidget(self.labelCacheNomTech)
        self.labelDate = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDate.setFont(font)
        self.labelDate.setStyleSheet(_fromUtf8("background: white;"))
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.verticalLayout.addWidget(self.labelDate)
        self.dateEdit = QtGui.QDateEdit(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(_fromUtf8("QDateEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"color: black;\n"
"background:rgb(247,247,247)\n"
"}\n"
"\n"
"\n"
""))
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(2016, 2, 1))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.labelCacheDate = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDate.setFont(font)
        self.labelCacheDate.setStyleSheet(_fromUtf8("background: white;"))
        self.labelCacheDate.setObjectName(_fromUtf8("labelCacheDate"))
        self.verticalLayout.addWidget(self.labelCacheDate)
        self.labelTempsEstime = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTempsEstime.setFont(font)
        self.labelTempsEstime.setStyleSheet(_fromUtf8("background: white;"))
        self.labelTempsEstime.setObjectName(_fromUtf8("labelTempsEstime"))
        self.verticalLayout.addWidget(self.labelTempsEstime)
        self.timeEditTempsEstime = QtGui.QTimeEdit(BonDeTravail)
        self.timeEditTempsEstime.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEditTempsEstime.setFont(font)
        self.timeEditTempsEstime.setStyleSheet(_fromUtf8("QTimeEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247)\n"
"}"))
        self.timeEditTempsEstime.setCurrentSection(QtGui.QDateTimeEdit.HourSection)
        self.timeEditTempsEstime.setCalendarPopup(True)
        self.timeEditTempsEstime.setObjectName(_fromUtf8("timeEditTempsEstime"))
        self.verticalLayout.addWidget(self.timeEditTempsEstime)
        self.labelCacheTemps = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheTemps.setFont(font)
        self.labelCacheTemps.setStyleSheet(_fromUtf8("background: white;"))
        self.labelCacheTemps.setObjectName(_fromUtf8("labelCacheTemps"))
        self.verticalLayout.addWidget(self.labelCacheTemps)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem9 = QtGui.QSpacerItem(43, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelDescSituation = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescSituation.setFont(font)
        self.labelDescSituation.setStyleSheet(_fromUtf8("background: white;"))
        self.labelDescSituation.setObjectName(_fromUtf8("labelDescSituation"))
        self.verticalLayout_2.addWidget(self.labelDescSituation)
        self.textEditDescSituation = QtGui.QTextEdit(BonDeTravail)
        self.textEditDescSituation.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescSituation.setFont(font)
        self.textEditDescSituation.setStyleSheet(_fromUtf8(""))
        self.textEditDescSituation.setObjectName(_fromUtf8("textEditDescSituation"))
        self.verticalLayout_2.addWidget(self.textEditDescSituation)
        self.labelCacheDescSit = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDescSit.setFont(font)
        self.labelCacheDescSit.setStyleSheet(_fromUtf8("background: white;"))
        self.labelCacheDescSit.setObjectName(_fromUtf8("labelCacheDescSit"))
        self.verticalLayout_2.addWidget(self.labelCacheDescSit)
        spacerItem10 = QtGui.QSpacerItem(30, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem10)
        self.labelDescIntervention = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDescIntervention.setFont(font)
        self.labelDescIntervention.setStyleSheet(_fromUtf8("background: white;"))
        self.labelDescIntervention.setObjectName(_fromUtf8("labelDescIntervention"))
        self.verticalLayout_2.addWidget(self.labelDescIntervention)
        self.textEditDescIntervention = QtGui.QTextEdit(BonDeTravail)
        self.textEditDescIntervention.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditDescIntervention.setFont(font)
        self.textEditDescIntervention.setStyleSheet(_fromUtf8(""))
        self.textEditDescIntervention.setObjectName(_fromUtf8("textEditDescIntervention"))
        self.verticalLayout_2.addWidget(self.textEditDescIntervention)
        self.labelCacheDescInt = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheDescInt.setFont(font)
        self.labelCacheDescInt.setStyleSheet(_fromUtf8("background: white;"))
        self.labelCacheDescInt.setObjectName(_fromUtf8("labelCacheDescInt"))
        self.verticalLayout_2.addWidget(self.labelCacheDescInt)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem11 = QtGui.QSpacerItem(50, 45, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.Assistancelabel = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Assistancelabel.setFont(font)
        self.Assistancelabel.setObjectName(_fromUtf8("Assistancelabel"))
        self.verticalLayout_5.addWidget(self.Assistancelabel)
        self.checkBox = QtGui.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_5.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_5.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_5.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout_5.addWidget(self.checkBox_4)
        self.labelCacheBesoinAssistance = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCacheBesoinAssistance.setFont(font)
        self.labelCacheBesoinAssistance.setObjectName(_fromUtf8("labelCacheBesoinAssistance"))
        self.verticalLayout_5.addWidget(self.labelCacheBesoinAssistance)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.SiReparelabel = QtGui.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SiReparelabel.setFont(font)
        self.SiReparelabel.setObjectName(_fromUtf8("SiReparelabel"))
        self.horizontalLayout_9.addWidget(self.SiReparelabel)
        self.comboBoxOuvertFerme = QtGui.QComboBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxOuvertFerme.setFont(font)
        self.comboBoxOuvertFerme.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBoxOuvertFerme.setStyleSheet(_fromUtf8(""))
        self.comboBoxOuvertFerme.setObjectName(_fromUtf8("comboBoxOuvertFerme"))
        self.comboBoxOuvertFerme.addItem(_fromUtf8(""))
        self.comboBoxOuvertFerme.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.comboBoxOuvertFerme)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.retranslateUi(BonDeTravail)
        QtCore.QMetaObject.connectSlotsByName(BonDeTravail)

    def retranslateUi(self, BonDeTravail):
        BonDeTravail.setWindowTitle(_translate("BonDeTravail", "Form", None))
        self.labelTitre.setText(_translate("BonDeTravail", "Bon de travail - Maintenance & réparation", None))
        self.label_ID.setText(_translate("BonDeTravail", "ID équipement", None))
        self.boutonConsultation.setText(_translate("BonDeTravail", "Consultation d\'un bon de travail", None))
        self.labelCategorieEquip.setText(_translate("BonDeTravail", "Catégorie d\'équipement", None))
        self.labelSalle.setText(_translate("BonDeTravail", "Salle", None))
        self.labelUnite.setText(_translate("BonDeTravail", "Unité", None))
        self.labelModele.setText(_translate("BonDeTravail", "Modèle", None))
        self.labelMarque.setText(_translate("BonDeTravail", "Marque", None))
        self.labelBonTravail.setText(_translate("BonDeTravail", "ID bon de travail", None))
        self.labelNomTechnicien.setText(_translate("BonDeTravail", "Nom du technicien", None))
        self.comboBoxNomTech.setItemText(0, _translate("BonDeTravail", "Gary", None))
        self.comboBoxNomTech.setItemText(1, _translate("BonDeTravail", "Sony", None))
        self.labelCacheNomTech.setText(_translate("BonDeTravail", "Ce que j\'ai écrit", None))
        self.labelDate.setText(_translate("BonDeTravail", "Date", None))
        self.dateEdit.setDisplayFormat(_translate("BonDeTravail", "dd-MM-yyyy", None))
        self.labelCacheDate.setText(_translate("BonDeTravail", "Ce que j\'ai écrit", None))
        self.labelTempsEstime.setText(_translate("BonDeTravail", "Temps estimé (h:m)", None))
        self.timeEditTempsEstime.setDisplayFormat(_translate("BonDeTravail", "h:mm", None))
        self.labelCacheTemps.setText(_translate("BonDeTravail", "Ce que j\'ai écrit", None))
        self.labelDescSituation.setText(_translate("BonDeTravail", "Description de la situation", None))
        self.labelCacheDescSit.setText(_translate("BonDeTravail", "Ce que j\'ai écrit", None))
        self.labelDescIntervention.setText(_translate("BonDeTravail", "Description de l\'intervention", None))
        self.labelCacheDescInt.setText(_translate("BonDeTravail", "Ce que j\'ai écrit", None))
        self.Assistancelabel.setText(_translate("BonDeTravail", "Besoin d\'assistance ?", None))
        self.checkBox.setText(_translate("BonDeTravail", "Outil", None))
        self.checkBox_2.setText(_translate("BonDeTravail", "Pièce", None))
        self.checkBox_3.setText(_translate("BonDeTravail", "Formation", None))
        self.checkBox_4.setText(_translate("BonDeTravail", "Manuel d\'utilisation", None))
        self.labelCacheBesoinAssistance.setText(_translate("BonDeTravail", "Ce que j\'ai écrit", None))
        self.SiReparelabel.setText(_translate("BonDeTravail", "Réparé: ", None))
        self.comboBoxOuvertFerme.setCurrentText(_translate("BonDeTravail", "Ouvert", None))
        self.comboBoxOuvertFerme.setItemText(0, _translate("BonDeTravail", "Ouvert", None))
        self.comboBoxOuvertFerme.setItemText(1, _translate("BonDeTravail", "Fermé", None))

