# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Piece.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Piece(object):
    def setupUi(self, Piece):
        Piece.setObjectName("Piece")
        Piece.resize(1711, 697)
        Piece.setMaximumSize(QtCore.QSize(11111111, 1111111))
        Piece.setStyleSheet("QWidget {\n"
"background:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background: rgb(247,247,247);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"padding: 1px;\n"
"color: black;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 8px;\n"
"background:rgb(169, 167, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Piece)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxNombreEquipement = QtWidgets.QSpinBox(Piece)
        self.spinBoxNombreEquipement.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxNombreEquipement.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxNombreEquipement.setFont(font)
        self.spinBoxNombreEquipement.setStyleSheet("QSpinBox\n"
"{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: black;\n"
"}")
        self.spinBoxNombreEquipement.setMaximum(999)
        self.spinBoxNombreEquipement.setObjectName("spinBoxNombreEquipement")
        self.gridLayout.addWidget(self.spinBoxNombreEquipement, 4, 4, 1, 1)
        self.labelSelectionCategorie = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSelectionCategorie.setFont(font)
        self.labelSelectionCategorie.setStyleSheet("background: white;")
        self.labelSelectionCategorie.setObjectName("labelSelectionCategorie")
        self.gridLayout.addWidget(self.labelSelectionCategorie, 3, 0, 1, 1)
        self.BoutonValider = QtWidgets.QPushButton(Piece)
        self.BoutonValider.setMinimumSize(QtCore.QSize(140, 20))
        self.BoutonValider.setMaximumSize(QtCore.QSize(120, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonValider.setFont(font)
        self.BoutonValider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonValider.setStyleSheet("QPushButton {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background: rgb(247,247,247);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"padding: 1px;\n"
"color: black;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 8px;\n"
"background:rgb(169, 167, 170);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/check-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonValider.setIcon(icon)
        self.BoutonValider.setObjectName("BoutonValider")
        self.gridLayout.addWidget(self.BoutonValider, 4, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(700, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 5, 1, 2)
        self.labelCategorieSelectionnee = QtWidgets.QLabel(Piece)
        self.labelCategorieSelectionnee.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorieSelectionnee.setFont(font)
        self.labelCategorieSelectionnee.setStyleSheet("background: white;")
        self.labelCategorieSelectionnee.setObjectName("labelCategorieSelectionnee")
        self.gridLayout.addWidget(self.labelCategorieSelectionnee, 11, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.BoutonEnregistrerPiece = QtWidgets.QPushButton(Piece)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoutonEnregistrerPiece.sizePolicy().hasHeightForWidth())
        self.BoutonEnregistrerPiece.setSizePolicy(sizePolicy)
        self.BoutonEnregistrerPiece.setMinimumSize(QtCore.QSize(140, 25))
        self.BoutonEnregistrerPiece.setMaximumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BoutonEnregistrerPiece.setFont(font)
        self.BoutonEnregistrerPiece.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonEnregistrerPiece.setStyleSheet("")
        self.BoutonEnregistrerPiece.setObjectName("BoutonEnregistrerPiece")
        self.horizontalLayout.addWidget(self.BoutonEnregistrerPiece)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 8)
        self.labelResumePiece = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResumePiece.setFont(font)
        self.labelResumePiece.setStyleSheet("background: white;")
        self.labelResumePiece.setObjectName("labelResumePiece")
        self.gridLayout.addWidget(self.labelResumePiece, 10, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 3, 1, 1)
        self.labelNombrePiece = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNombrePiece.setFont(font)
        self.labelNombrePiece.setStyleSheet("background: white;")
        self.labelNombrePiece.setObjectName("labelNombrePiece")
        self.gridLayout.addWidget(self.labelNombrePiece, 4, 3, 1, 1)
        self.titreLayout = QtWidgets.QHBoxLayout()
        self.titreLayout.setObjectName("titreLayout")
        self.label_3 = QtWidgets.QLabel(Piece)
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setStyleSheet("background:white;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/piece_image.png"))
        self.label_3.setObjectName("label_3")
        self.titreLayout.addWidget(self.label_3)
        self.labelTitreConsultationEquipement = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelTitreConsultationEquipement.setFont(font)
        self.labelTitreConsultationEquipement.setStyleSheet("background:white;")
        self.labelTitreConsultationEquipement.setObjectName("labelTitreConsultationEquipement")
        self.titreLayout.addWidget(self.labelTitreConsultationEquipement)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titreLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.titreLayout, 0, 0, 1, 8)
        self.labelNomPiece = QtWidgets.QLabel(Piece)
        self.labelNomPiece.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNomPiece.setFont(font)
        self.labelNomPiece.setStyleSheet("background: white;")
        self.labelNomPiece.setObjectName("labelNomPiece")
        self.gridLayout.addWidget(self.labelNomPiece, 4, 0, 1, 1)
        self.comboBoxCategorieSelectionnee = QtWidgets.QComboBox(Piece)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCategorieSelectionnee.sizePolicy().hasHeightForWidth())
        self.comboBoxCategorieSelectionnee.setSizePolicy(sizePolicy)
        self.comboBoxCategorieSelectionnee.setMinimumSize(QtCore.QSize(300, 20))
        self.comboBoxCategorieSelectionnee.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCategorieSelectionnee.setFont(font)
        self.comboBoxCategorieSelectionnee.setStyleSheet("QComboBox{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: black;\n"
"}\n"
"")
        self.comboBoxCategorieSelectionnee.setObjectName("comboBoxCategorieSelectionnee")
        self.gridLayout.addWidget(self.comboBoxCategorieSelectionnee, 11, 1, 1, 1)
        self.comboBoxSelectionCategoriePiece = QtWidgets.QComboBox(Piece)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSelectionCategoriePiece.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectionCategoriePiece.setSizePolicy(sizePolicy)
        self.comboBoxSelectionCategoriePiece.setMinimumSize(QtCore.QSize(300, 20))
        self.comboBoxSelectionCategoriePiece.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxSelectionCategoriePiece.setFont(font)
        self.comboBoxSelectionCategoriePiece.setStyleSheet("QComboBox{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: black;\n"
"}")
        self.comboBoxSelectionCategoriePiece.setEditable(True)
        self.comboBoxSelectionCategoriePiece.setObjectName("comboBoxSelectionCategoriePiece")
        self.gridLayout.addWidget(self.comboBoxSelectionCategoriePiece, 3, 1, 1, 1)
        self.comboBoxNomPiece = QtWidgets.QComboBox(Piece)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxNomPiece.sizePolicy().hasHeightForWidth())
        self.comboBoxNomPiece.setSizePolicy(sizePolicy)
        self.comboBoxNomPiece.setMinimumSize(QtCore.QSize(300, 20))
        self.comboBoxNomPiece.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNomPiece.setFont(font)
        self.comboBoxNomPiece.setStyleSheet("QComboBox{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: black;\n"
"}")
        self.comboBoxNomPiece.setEditable(True)
        self.comboBoxNomPiece.setObjectName("comboBoxNomPiece")
        self.gridLayout.addWidget(self.comboBoxNomPiece, 4, 1, 1, 1)
        self.tableCategoriePiece = QtWidgets.QTableWidget(Piece)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableCategoriePiece.setFont(font)
        self.tableCategoriePiece.setStyleSheet("background: white;")
        self.tableCategoriePiece.setObjectName("tableCategoriePiece")
        self.tableCategoriePiece.setColumnCount(0)
        self.tableCategoriePiece.setRowCount(0)
        self.gridLayout.addWidget(self.tableCategoriePiece, 7, 0, 1, 8)
        self.tableResume = QtWidgets.QTableWidget(Piece)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableResume.setFont(font)
        self.tableResume.setStyleSheet("background: white;")
        self.tableResume.setObjectName("tableResume")
        self.tableResume.setColumnCount(0)
        self.tableResume.setRowCount(0)
        self.gridLayout.addWidget(self.tableResume, 12, 0, 1, 8)

        self.retranslateUi(Piece)
        QtCore.QMetaObject.connectSlotsByName(Piece)

    def retranslateUi(self, Piece):
        _translate = QtCore.QCoreApplication.translate
        Piece.setWindowTitle(_translate("Piece", "Form"))
        self.labelSelectionCategorie.setText(_translate("Piece", "Sélectionner la catégorie de la pièce"))
        self.BoutonValider.setText(_translate("Piece", "Valider"))
        self.labelCategorieSelectionnee.setText(_translate("Piece", "Liste des pièces pour la catégorie sélectionnée"))
        self.BoutonEnregistrerPiece.setText(_translate("Piece", "Enregistrer la pièce"))
        self.labelResumePiece.setText(_translate("Piece", "Résumé des pièces pour chaque catégorie"))
        self.labelNombrePiece.setText(_translate("Piece", "Nombre de pièces"))
        self.labelTitreConsultationEquipement.setText(_translate("Piece", "Ajouter une pièce"))
        self.labelNomPiece.setText(_translate("Piece", "Nom de la pièce"))

