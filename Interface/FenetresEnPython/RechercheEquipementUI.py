# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetreRechEquip.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RechercheEquipement(object):
    def setupUi(self, RechercheEquipement):
        RechercheEquipement.setObjectName("RechercheEquipement")
        RechercheEquipement.resize(930, 658)
        RechercheEquipement.setStyleSheet("background: white;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RechercheEquipement)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.logoLoupe = QtWidgets.QLabel(RechercheEquipement)
        self.logoLoupe.setMaximumSize(QtCore.QSize(50, 80))
        self.logoLoupe.setText("")
        self.logoLoupe.setPixmap(QtGui.QPixmap("Images/magnifier.png"))
        self.logoLoupe.setObjectName("logoLoupe")
        self.gridLayout_6.addWidget(self.logoLoupe, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 3, 1, 1)
        self.labelTitre = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitre.setFont(font)
        self.labelTitre.setStyleSheet("background: white;")
        self.labelTitre.setObjectName("labelTitre")
        self.gridLayout_6.addWidget(self.labelTitre, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.boutonActualiser = QtWidgets.QPushButton(RechercheEquipement)
        self.boutonActualiser.setMinimumSize(QtCore.QSize(47, 43))
        self.boutonActualiser.setMaximumSize(QtCore.QSize(47, 43))
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
"min-width: 35px;\n"
"max-width:35px;\n"
"min-height: 35px;\n"
"max-height: 35px;\n"
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
        icon.addPixmap(QtGui.QPixmap("Images/refresh-button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonActualiser.setIcon(icon)
        self.boutonActualiser.setIconSize(QtCore.QSize(50, 50))
        self.boutonActualiser.setObjectName("boutonActualiser")
        self.gridLayout_5.addWidget(self.boutonActualiser, 0, 4, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.labelCategorieEquipement = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.labelCategorieEquipement.setFont(font)
        self.labelCategorieEquipement.setStyleSheet("background: white;")
        self.labelCategorieEquipement.setObjectName("labelCategorieEquipement")
        self.gridLayout_9.addWidget(self.labelCategorieEquipement, 0, 0, 1, 1)
        self.lineEditNumeroSerie = QtWidgets.QLineEdit(RechercheEquipement)
        self.lineEditNumeroSerie.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNumeroSerie.setFont(font)
        self.lineEditNumeroSerie.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.lineEditNumeroSerie.setObjectName("lineEditNumeroSerie")
        self.gridLayout_9.addWidget(self.lineEditNumeroSerie, 1, 2, 1, 1)
        self.comboBoxCategorieEquipement = QtWidgets.QComboBox(RechercheEquipement)
        self.comboBoxCategorieEquipement.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCategorieEquipement.setFont(font)
        self.comboBoxCategorieEquipement.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.comboBoxCategorieEquipement.setObjectName("comboBoxCategorieEquipement")
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItem("")
        self.gridLayout_9.addWidget(self.comboBoxCategorieEquipement, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 1, 1, 1, 1)
        self.labelNumeroSerie = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.labelNumeroSerie.setFont(font)
        self.labelNumeroSerie.setStyleSheet("background: white;")
        self.labelNumeroSerie.setObjectName("labelNumeroSerie")
        self.gridLayout_9.addWidget(self.labelNumeroSerie, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_9, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 6, 1, 1)
        self.boutonNouvelleRecherche = QtWidgets.QPushButton(RechercheEquipement)
        self.boutonNouvelleRecherche.setMinimumSize(QtCore.QSize(92, 43))
        self.boutonNouvelleRecherche.setMaximumSize(QtCore.QSize(92, 43))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonNouvelleRecherche.setFont(font)
        self.boutonNouvelleRecherche.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boutonNouvelleRecherche.setStyleSheet("QPushButton {\n"
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
"min-width: 80px;\n"
"max-width: 80px;\n"
"min-height: 35px;\n"
"max-height: 35px;\n"
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
        self.boutonNouvelleRecherche.setObjectName("boutonNouvelleRecherche")
        self.gridLayout_5.addWidget(self.boutonNouvelleRecherche, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBoxCentreService = QtWidgets.QComboBox(RechercheEquipement)
        self.comboBoxCentreService.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCentreService.setFont(font)
        self.comboBoxCentreService.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.comboBoxCentreService.setObjectName("comboBoxCentreService")
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxCentreService, 1, 2, 1, 1)
        self.labelEtatService = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.labelEtatService.setFont(font)
        self.labelEtatService.setStyleSheet("background: white;")
        self.labelEtatService.setObjectName("labelEtatService")
        self.gridLayout_3.addWidget(self.labelEtatService, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(230, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 3, 1, 1)
        self.labelCentreService = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.labelCentreService.setFont(font)
        self.labelCentreService.setStyleSheet("background: white;")
        self.labelCentreService.setObjectName("labelCentreService")
        self.gridLayout_3.addWidget(self.labelCentreService, 0, 2, 1, 1)
        self.comboBoxEtatService = QtWidgets.QComboBox(RechercheEquipement)
        self.comboBoxEtatService.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxEtatService.setFont(font)
        self.comboBoxEtatService.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.comboBoxEtatService.setObjectName("comboBoxEtatService")
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxEtatService, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxProvenance = QtWidgets.QComboBox(RechercheEquipement)
        self.comboBoxProvenance.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxProvenance.setFont(font)
        self.comboBoxProvenance.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("")
        self.gridLayout.addWidget(self.comboBoxProvenance, 1, 2, 1, 1)
        self.comboBoxSalle = QtWidgets.QComboBox(RechercheEquipement)
        self.comboBoxSalle.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxSalle.setFont(font)
        self.comboBoxSalle.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);")
        self.comboBoxSalle.setObjectName("comboBoxSalle")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.gridLayout.addWidget(self.comboBoxSalle, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(230, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.labelProvenance = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.labelProvenance.setFont(font)
        self.labelProvenance.setStyleSheet("background: white;")
        self.labelProvenance.setObjectName("labelProvenance")
        self.gridLayout.addWidget(self.labelProvenance, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        self.labelSalle = QtWidgets.QLabel(RechercheEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.labelSalle.setFont(font)
        self.labelSalle.setStyleSheet("background: white;")
        self.labelSalle.setObjectName("labelSalle")
        self.gridLayout.addWidget(self.labelSalle, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableResultats = QtWidgets.QTableWidget(RechercheEquipement)
        self.tableResultats.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
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
        self.tableResultats.horizontalHeader().setDefaultSectionSize(300)
        self.gridLayout_2.addWidget(self.tableResultats, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RechercheEquipement)
        QtCore.QMetaObject.connectSlotsByName(RechercheEquipement)

    def retranslateUi(self, RechercheEquipement):
        _translate = QtCore.QCoreApplication.translate
        RechercheEquipement.setWindowTitle(_translate("RechercheEquipement", "Form"))
        self.labelTitre.setText(_translate("RechercheEquipement", "Assistant de recherche - Équipement"))
        self.labelCategorieEquipement.setText(_translate("RechercheEquipement", "Catégorie d\'équipement"))
        self.comboBoxCategorieEquipement.setItemText(0, _translate("RechercheEquipement", "Catégorie 1"))
        self.comboBoxCategorieEquipement.setItemText(1, _translate("RechercheEquipement", "Catégorie 2"))
        self.comboBoxCategorieEquipement.setItemText(2, _translate("RechercheEquipement", "Catégorie 3"))
        self.comboBoxCategorieEquipement.setItemText(3, _translate("RechercheEquipement", "Catégorie 4"))
        self.labelNumeroSerie.setText(_translate("RechercheEquipement", "Numéro de série"))
        self.boutonNouvelleRecherche.setText(_translate("RechercheEquipement", "Nouvelle\n"
"Recherche"))
        self.comboBoxCentreService.setItemText(0, _translate("RechercheEquipement", "Centre 1"))
        self.comboBoxCentreService.setItemText(1, _translate("RechercheEquipement", "Centre 2"))
        self.comboBoxCentreService.setItemText(2, _translate("RechercheEquipement", "Centre 3"))
        self.labelEtatService.setText(_translate("RechercheEquipement", "État de service"))
        self.labelCentreService.setText(_translate("RechercheEquipement", "Centre de service"))
        self.comboBoxEtatService.setItemText(0, _translate("RechercheEquipement", "En maintenance"))
        self.comboBoxEtatService.setItemText(1, _translate("RechercheEquipement", "En réparation"))
        self.comboBoxEtatService.setItemText(2, _translate("RechercheEquipement", "Au rebus"))
        self.comboBoxProvenance.setItemText(0, _translate("RechercheEquipement", "Provenance 1"))
        self.comboBoxProvenance.setItemText(1, _translate("RechercheEquipement", "Provenance 2"))
        self.comboBoxProvenance.setItemText(2, _translate("RechercheEquipement", "Provenance 3"))
        self.comboBoxSalle.setItemText(0, _translate("RechercheEquipement", "Salle 1"))
        self.comboBoxSalle.setItemText(1, _translate("RechercheEquipement", "Salle 2"))
        self.comboBoxSalle.setItemText(2, _translate("RechercheEquipement", "Salle 3"))
        self.labelProvenance.setText(_translate("RechercheEquipement", "Provenance"))
        self.labelSalle.setText(_translate("RechercheEquipement", "Salle"))
        item = self.tableResultats.verticalHeaderItem(0)
        item.setText(_translate("RechercheEquipement", "1"))
        item = self.tableResultats.verticalHeaderItem(1)
        item.setText(_translate("RechercheEquipement", "2"))
        item = self.tableResultats.verticalHeaderItem(2)
        item.setText(_translate("RechercheEquipement", "3"))
        item = self.tableResultats.verticalHeaderItem(3)
        item.setText(_translate("RechercheEquipement", "4"))
        item = self.tableResultats.horizontalHeaderItem(0)
        item.setText(_translate("RechercheEquipement", "ID"))
        item = self.tableResultats.horizontalHeaderItem(1)
        item.setText(_translate("RechercheEquipement", "Catégorie d\'équipement"))
        item = self.tableResultats.horizontalHeaderItem(2)
        item.setText(_translate("RechercheEquipement", "Marque"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RechercheEquipement = QtWidgets.QWidget()
    ui = Ui_RechercheEquipement()
    ui.setupUi(RechercheEquipement)
    RechercheEquipement.show()
    sys.exit(app.exec_())

