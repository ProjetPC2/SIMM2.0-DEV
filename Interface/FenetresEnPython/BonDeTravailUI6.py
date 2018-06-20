# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BonDeTravail3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BonDeTravail(object):
    def setupUi(self, BonDeTravail):
        BonDeTravail.setObjectName("BonDeTravail")
        BonDeTravail.resize(1168, 839)
        BonDeTravail.setMinimumSize(QtCore.QSize(0, 0))
        BonDeTravail.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
"background:rgb(247,247,247);\n"
"}\n"
"\n"
"QSpinBox {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
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
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
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
"max-width: 30px;\n"
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
        spacerItem2 = QtWidgets.QSpacerItem(200, 19, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)
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
        self.boutonConsultation.setMaximumSize(QtCore.QSize(232, 38))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonConsultation.setFont(font)
        self.boutonConsultation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonConsultation.setStyleSheet("QPushButton {\n"
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
"min-width: 220px;\n"
"max-width: 220px;\n"
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
        icon1.addPixmap(QtGui.QPixmap("Images/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonConsultation.setIcon(icon1)
        self.boutonConsultation.setIconSize(QtCore.QSize(16, 16))
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
        self.labelUnite = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelUnite.setFont(font)
        self.labelUnite.setStyleSheet("background: white;")
        self.labelUnite.setObjectName("labelUnite")
        self.gridLayout_3.addWidget(self.labelUnite, 3, 1, 1, 1)
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
        self.labelEcritureUnite = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEcritureUnite.setFont(font)
        self.labelEcritureUnite.setStyleSheet(" QLabel{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: rgb(81, 81, 81);\n"
"}\n"
"")
        self.labelEcritureUnite.setText("")
        self.labelEcritureUnite.setObjectName("labelEcritureUnite")
        self.gridLayout_3.addWidget(self.labelEcritureUnite, 4, 1, 1, 1)
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
        spacerItem3 = QtWidgets.QSpacerItem(100, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelPieceAssociees = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPieceAssociees.setFont(font)
        self.labelPieceAssociees.setObjectName("labelPieceAssociees")
        self.verticalLayout_4.addWidget(self.labelPieceAssociees)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelCategoriePiece = QtWidgets.QLabel(BonDeTravail)
        self.labelCategoriePiece.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategoriePiece.setFont(font)
        self.labelCategoriePiece.setObjectName("labelCategoriePiece")
        self.horizontalLayout_4.addWidget(self.labelCategoriePiece)
        self.comboBoxCategoriePiece = QtWidgets.QComboBox(BonDeTravail)
        self.comboBoxCategoriePiece.setMinimumSize(QtCore.QSize(225, 20))
        self.comboBoxCategoriePiece.setMaximumSize(QtCore.QSize(225, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCategoriePiece.setFont(font)
        self.comboBoxCategoriePiece.setObjectName("comboBoxCategoriePiece")
        self.horizontalLayout_4.addWidget(self.comboBoxCategoriePiece)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelNomPiece = QtWidgets.QLabel(BonDeTravail)
        self.labelNomPiece.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNomPiece.setFont(font)
        self.labelNomPiece.setObjectName("labelNomPiece")
        self.horizontalLayout_5.addWidget(self.labelNomPiece)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.comboBoxNomPiece = QtWidgets.QComboBox(BonDeTravail)
        self.comboBoxNomPiece.setMinimumSize(QtCore.QSize(225, 20))
        self.comboBoxNomPiece.setMaximumSize(QtCore.QSize(225, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNomPiece.setFont(font)
        self.comboBoxNomPiece.setObjectName("comboBoxNomPiece")
        self.horizontalLayout_5.addWidget(self.comboBoxNomPiece)
        self.labelNomPiece_2 = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNomPiece_2.setFont(font)
        self.labelNomPiece_2.setObjectName("labelNomPiece_2")
        self.horizontalLayout_5.addWidget(self.labelNomPiece_2)
        self.spinBoxNombrePiece = QtWidgets.QSpinBox(BonDeTravail)
        self.spinBoxNombrePiece.setMaximumSize(QtCore.QSize(60, 16777215))
        self.spinBoxNombrePiece.setMaximum(999)
        self.spinBoxNombrePiece.setObjectName("spinBoxNombrePiece")
        self.horizontalLayout_5.addWidget(self.spinBoxNombrePiece)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButtonValider = QtWidgets.QPushButton(BonDeTravail)
        self.pushButtonValider.setMinimumSize(QtCore.QSize(110, 20))
        self.pushButtonValider.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonValider.setFont(font)
        self.pushButtonValider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/check-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonValider.setIcon(icon2)
        self.pushButtonValider.setObjectName("pushButtonValider")
        self.horizontalLayout_5.addWidget(self.pushButtonValider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidgetPiecesAssociees = QtWidgets.QTableWidget(BonDeTravail)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableWidgetPiecesAssociees.setFont(font)
        self.tableWidgetPiecesAssociees.setObjectName("tableWidgetPiecesAssociees")
        self.tableWidgetPiecesAssociees.setColumnCount(3)
        self.tableWidgetPiecesAssociees.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPiecesAssociees.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPiecesAssociees.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPiecesAssociees.setHorizontalHeaderItem(2, item)
        self.tableWidgetPiecesAssociees.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidgetPiecesAssociees.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_8.addWidget(self.tableWidgetPiecesAssociees)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.boutonAjoutBDT = QtWidgets.QPushButton(BonDeTravail)
        self.boutonAjoutBDT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonAjoutBDT.setStyleSheet("QPushButton {\n"
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
"max-width: 30px;\n"
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
        self.boutonAjoutBDT.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/plus_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonAjoutBDT.setIcon(icon3)
        self.boutonAjoutBDT.setIconSize(QtCore.QSize(35, 35))
        self.boutonAjoutBDT.setObjectName("boutonAjoutBDT")
        self.horizontalLayout_3.addWidget(self.boutonAjoutBDT)
        self.boutonSauvegarde = QtWidgets.QPushButton(BonDeTravail)
        self.boutonSauvegarde.setMaximumSize(QtCore.QSize(42, 38))
        self.boutonSauvegarde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonSauvegarde.setAutoFillBackground(False)
        self.boutonSauvegarde.setStyleSheet("QPushButton {\n"
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
"max-width: 30px;\n"
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
        self.boutonSauvegarde.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSauvegarde.setIcon(icon4)
        self.boutonSauvegarde.setIconSize(QtCore.QSize(35, 35))
        self.boutonSauvegarde.setObjectName("boutonSauvegarde")
        self.horizontalLayout_3.addWidget(self.boutonSauvegarde)
        self.boutonFlecheDoubleGauche = QtWidgets.QPushButton(BonDeTravail)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/double-left-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleGauche.setIcon(icon5)
        self.boutonFlecheDoubleGauche.setObjectName("boutonFlecheDoubleGauche")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleGauche)
        self.boutonFlecheGauche = QtWidgets.QPushButton(BonDeTravail)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/angle-pointing-to-left (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheGauche.setIcon(icon6)
        self.boutonFlecheGauche.setObjectName("boutonFlecheGauche")
        self.horizontalLayout_3.addWidget(self.boutonFlecheGauche)
        self.boutonFlecheDroite = QtWidgets.QPushButton(BonDeTravail)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/angle-arrow-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDroite.setIcon(icon7)
        self.boutonFlecheDroite.setObjectName("boutonFlecheDroite")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDroite)
        self.boutonFlecheDoubleDroite = QtWidgets.QPushButton(BonDeTravail)
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images/double-angle-pointing-to-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonFlecheDoubleDroite.setIcon(icon8)
        self.boutonFlecheDoubleDroite.setObjectName("boutonFlecheDoubleDroite")
        self.horizontalLayout_3.addWidget(self.boutonFlecheDoubleDroite)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(220, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem9)
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
        self.comboBoxNomTech.addItem("")
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
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
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
        self.labelCacheDescSit.setTextFormat(QtCore.Qt.AutoText)
        self.labelCacheDescSit.setWordWrap(True)
        self.labelCacheDescSit.setObjectName("labelCacheDescSit")
        self.verticalLayout_2.addWidget(self.labelCacheDescSit)
        spacerItem12 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem12)
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
        self.labelCacheDescInt.setWordWrap(True)
        self.labelCacheDescInt.setObjectName("labelCacheDescInt")
        self.verticalLayout_2.addWidget(self.labelCacheDescInt)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem13 = QtWidgets.QSpacerItem(40, 45, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.label = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
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
        spacerItem14 = QtWidgets.QSpacerItem(50, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)
        self.labelAssistance = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelAssistance.setFont(font)
        self.labelAssistance.setObjectName("labelAssistance")
        self.verticalLayout_5.addWidget(self.labelAssistance)
        self.checkBoxOutil = QtWidgets.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxOutil.setFont(font)
        self.checkBoxOutil.setObjectName("checkBoxOutil")
        self.verticalLayout_5.addWidget(self.checkBoxOutil)
        self.checkBoxPiece = QtWidgets.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxPiece.setFont(font)
        self.checkBoxPiece.setObjectName("checkBoxPiece")
        self.verticalLayout_5.addWidget(self.checkBoxPiece)
        self.checkBoxFormation = QtWidgets.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxFormation.setFont(font)
        self.checkBoxFormation.setObjectName("checkBoxFormation")
        self.verticalLayout_5.addWidget(self.checkBoxFormation)
        self.checkBoxManuel = QtWidgets.QCheckBox(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxManuel.setFont(font)
        self.checkBoxManuel.setObjectName("checkBoxManuel")
        self.verticalLayout_5.addWidget(self.checkBoxManuel)
        self.labelAssistanceCache = QtWidgets.QLabel(BonDeTravail)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelAssistanceCache.setFont(font)
        self.labelAssistanceCache.setObjectName("labelAssistanceCache")
        self.verticalLayout_5.addWidget(self.labelAssistanceCache)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
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
        self.labelUnite.setText(_translate("BonDeTravail", "Centre de service"))
        self.labelModele.setText(_translate("BonDeTravail", "Modèle"))
        self.labelMarque.setText(_translate("BonDeTravail", "Marque"))
        self.labelPieceAssociees.setText(_translate("BonDeTravail", "Pièces associées à la réparation"))
        self.labelCategoriePiece.setText(_translate("BonDeTravail", "Catégorie de la pièce"))
        self.labelNomPiece.setText(_translate("BonDeTravail", "Nom de la pièce"))
        self.labelNomPiece_2.setText(_translate("BonDeTravail", "Nombre de pièces"))
        self.pushButtonValider.setText(_translate("BonDeTravail", "Valider"))
        item = self.tableWidgetPiecesAssociees.horizontalHeaderItem(0)
        item.setText(_translate("BonDeTravail", "Categorie"))
        item = self.tableWidgetPiecesAssociees.horizontalHeaderItem(1)
        item.setText(_translate("BonDeTravail", "Nombre Piece"))
        item = self.tableWidgetPiecesAssociees.horizontalHeaderItem(2)
        item.setText(_translate("BonDeTravail", "Nombre"))
        self.labelBonTravail.setText(_translate("BonDeTravail", "ID bon de travail"))
        self.labelNomTechnicien.setText(_translate("BonDeTravail", "Nom du technicien"))
        self.comboBoxNomTech.setItemText(0, _translate("BonDeTravail", "Gary"))
        self.comboBoxNomTech.setItemText(1, _translate("BonDeTravail", "Sony"))
        self.comboBoxNomTech.setItemText(2, _translate("BonDeTravail", "Jean-Michel"))
        self.labelCacheNomTech.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelDate.setText(_translate("BonDeTravail", "Date"))
        self.dateEdit.setDisplayFormat(_translate("BonDeTravail", "dd-MM-yyyy"))
        self.labelCacheDate.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelTempsEstime.setText(_translate("BonDeTravail", "Temps estimé (h:m)"))
        self.timeEditTempsEstime.setDisplayFormat(_translate("BonDeTravail", "h:mm"))
        self.labelCacheTemps.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))
        self.labelDescSituation.setText(_translate("BonDeTravail", "Description de la situation"))
        self.labelCacheDescSit.setText(_translate("BonDeTravail", "Description Situation"))
        self.labelDescIntervention.setText(_translate("BonDeTravail", "Description de l\'intervention"))
        self.labelCacheDescInt.setText(_translate("BonDeTravail", "Description Intervention"))
        self.label.setText(_translate("BonDeTravail", "Réparé?"))
        self.comboBoxOuvertFerme.setItemText(0, _translate("BonDeTravail", "Non"))
        self.comboBoxOuvertFerme.setItemText(1, _translate("BonDeTravail", "Oui"))
        self.labelAssistance.setText(_translate("BonDeTravail", "Besoin d\'assistance?"))
        self.checkBoxOutil.setText(_translate("BonDeTravail", "Outils"))
        self.checkBoxPiece.setText(_translate("BonDeTravail", "Pièces"))
        self.checkBoxFormation.setText(_translate("BonDeTravail", "Aide exterieur"))
        self.checkBoxManuel.setText(_translate("BonDeTravail", "Manuel de service"))
        self.labelAssistanceCache.setText(_translate("BonDeTravail", "Ce que j\'ai écrit"))

