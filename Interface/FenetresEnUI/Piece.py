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
        Piece.resize(817, 996)
        Piece.setStyleSheet("background:white;")
        self.gridLayout = QtWidgets.QGridLayout(Piece)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(Piece)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Piece)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: black\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Piece)
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"color: black;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.labelCategorieSelectionnee = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCategorieSelectionnee.setFont(font)
        self.labelCategorieSelectionnee.setObjectName("labelCategorieSelectionnee")
        self.gridLayout.addWidget(self.labelCategorieSelectionnee, 6, 0, 1, 1)
        self.comboBoxCategorieSelectionnee = QtWidgets.QComboBox(Piece)
        self.comboBoxCategorieSelectionnee.setMaximumSize(QtCore.QSize(300, 16777215))
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
        self.gridLayout.addWidget(self.comboBoxCategorieSelectionnee, 6, 1, 1, 1)
        self.titreLayout = QtWidgets.QHBoxLayout()
        self.titreLayout.setObjectName("titreLayout")
        self.label_3 = QtWidgets.QLabel(Piece)
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setStyleSheet("background:white;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Images/piece_image.png"))
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titreLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.titreLayout, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Piece)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.listViewPieceCategorie = QtWidgets.QListView(Piece)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.listViewPieceCategorie.setFont(font)
        self.listViewPieceCategorie.setObjectName("listViewPieceCategorie")
        self.gridLayout.addWidget(self.listViewPieceCategorie, 7, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Piece)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.retranslateUi(Piece)
        QtCore.QMetaObject.connectSlotsByName(Piece)

    def retranslateUi(self, Piece):
        _translate = QtCore.QCoreApplication.translate
        Piece.setWindowTitle(_translate("Piece", "Form"))
        self.label.setText(_translate("Piece", "Ajouter une pièce"))
        self.labelCategorieSelectionnee.setText(_translate("Piece", "Liste des pièces pour la catégorie sélectionnée"))
        self.labelTitreConsultationEquipement.setText(_translate("Piece", "Ajouter une pièce"))
        self.label_2.setText(_translate("Piece", "Sélectionner la catégorie à ajouter"))
        self.pushButton.setText(_translate("Piece", "Enregistrer la pièce"))

