# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rbdt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RechercheBonDeTravail(object):
    def setupUi(self, RechercheBonDeTravail):
        RechercheBonDeTravail.setObjectName("RechercheBonDeTravail")
        RechercheBonDeTravail.resize(939, 738)
        RechercheBonDeTravail.setMaximumSize(QtCore.QSize(2000, 2000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../SIMM2.0-DEV/Interface/Images/PC2_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        RechercheBonDeTravail.setWindowIcon(icon)
        RechercheBonDeTravail.setStyleSheet("background: white;")
        self.gridLayout = QtWidgets.QGridLayout(RechercheBonDeTravail)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(RechercheBonDeTravail)
        self.label.setMaximumSize(QtCore.QSize(38, 34))
        self.label.setStyleSheet("background: white;")
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelCategorie = QtWidgets.QLabel(RechercheBonDeTravail)
        self.labelCategorie.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCategorie.setFont(font)
        self.labelCategorie.setStyleSheet("background: white;")
        self.labelCategorie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCategorie.setObjectName("labelCategorie")
        self.verticalLayout_4.addWidget(self.labelCategorie)
        self.comboBoxCategorieEquipement = QtWidgets.QComboBox(RechercheBonDeTravail)
        self.comboBoxCategorieEquipement.setMaximumSize(QtCore.QSize(243, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxCategorieEquipement.setFont(font)
        self.comboBoxCategorieEquipement.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 220px;\n"
"backround:rgb(245, 245, 245);\n"
"}\n"
"    ")
        self.comboBoxCategorieEquipement.setObjectName("comboBoxCategorieEquipement")
        self.verticalLayout_4.addWidget(self.comboBoxCategorieEquipement)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.LabelAvant = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelAvant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelAvant.setFont(font)
        self.LabelAvant.setStyleSheet("background: white;")
        self.LabelAvant.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LabelAvant.setObjectName("LabelAvant")
        self.verticalLayout_7.addWidget(self.LabelAvant)
        self.calendrierAvant = QtWidgets.QDateEdit(RechercheBonDeTravail)
        self.calendrierAvant.setMaximumSize(QtCore.QSize(224, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendrierAvant.setFont(font)
        self.calendrierAvant.setStyleSheet("QDateEdit{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background :white;\n"
"max-width:220px;\n"
"}\n"
"")
        self.calendrierAvant.setCalendarPopup(True)
        self.calendrierAvant.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierAvant.setObjectName("calendrierAvant")
        self.verticalLayout_7.addWidget(self.calendrierAvant)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LabelApres = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelApres.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelApres.setFont(font)
        self.LabelApres.setStyleSheet("background: white;")
        self.LabelApres.setObjectName("LabelApres")
        self.verticalLayout_5.addWidget(self.LabelApres)
        self.calendrierApres = QtWidgets.QDateEdit(RechercheBonDeTravail)
        self.calendrierApres.setMaximumSize(QtCore.QSize(224, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendrierApres.setFont(font)
        self.calendrierApres.setStyleSheet("QDateEdit{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background :white;\n"
"max-width:220px;\n"
"}\n"
"")
        self.calendrierApres.setCalendarPopup(True)
        self.calendrierApres.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierApres.setObjectName("calendrierApres")
        self.verticalLayout_5.addWidget(self.calendrierApres)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.LabelEtat = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelEtat.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelEtat.setFont(font)
        self.LabelEtat.setStyleSheet("background: white;")
        self.LabelEtat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelEtat.setObjectName("LabelEtat")
        self.verticalLayout_8.addWidget(self.LabelEtat)
        self.comboBoxEtat = QtWidgets.QComboBox(RechercheBonDeTravail)
        self.comboBoxEtat.setMaximumSize(QtCore.QSize(223, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxEtat.setFont(font)
        self.comboBoxEtat.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"backround:rgb(245, 245, 245);\n"
"}\n"
"    ")
        self.comboBoxEtat.setObjectName("comboBoxEtat")
        self.verticalLayout_8.addWidget(self.comboBoxEtat)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LabelCentreService = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelCentreService.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelCentreService.setFont(font)
        self.LabelCentreService.setStyleSheet("background: white;")
        self.LabelCentreService.setObjectName("LabelCentreService")
        self.verticalLayout_2.addWidget(self.LabelCentreService)
        self.comboBoxCentreService = QtWidgets.QComboBox(RechercheBonDeTravail)
        self.comboBoxCentreService.setMaximumSize(QtCore.QSize(223, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxCentreService.setFont(font)
        self.comboBoxCentreService.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"backround:rgb(245, 245, 245);\n"
"}\n"
"    ")
        self.comboBoxCentreService.setObjectName("comboBoxCentreService")
        self.verticalLayout_2.addWidget(self.comboBoxCentreService)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelDescription = QtWidgets.QLabel(RechercheBonDeTravail)
        self.LabelDescription.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelDescription.setFont(font)
        self.LabelDescription.setStyleSheet("background: white;")
        self.LabelDescription.setObjectName("LabelDescription")
        self.verticalLayout.addWidget(self.LabelDescription)
        self.lineEditDescriptionSituation = QtWidgets.QLineEdit(RechercheBonDeTravail)
        self.lineEditDescriptionSituation.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:white;\n"
"min-width: 50px;\n"
"max-width: 300px;\n"
"}")
        self.lineEditDescriptionSituation.setObjectName("lineEditDescriptionSituation")
        self.verticalLayout.addWidget(self.lineEditDescriptionSituation)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
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
        self.tableResultats.horizontalHeader().setDefaultSectionSize(180)
        self.tableResultats.horizontalHeader().setMinimumSectionSize(30)
        self.tableResultats.verticalHeader().setDefaultSectionSize(30)
        self.tableResultats.verticalHeader().setMinimumSectionSize(20)
        self.tableResultats.verticalHeader().setSortIndicatorShown(False)
        self.tableResultats.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.tableResultats)
        self.gridLayout.addLayout(self.verticalLayout_11, 5, 0, 1, 1)

        self.retranslateUi(RechercheBonDeTravail)
        QtCore.QMetaObject.connectSlotsByName(RechercheBonDeTravail)

    def retranslateUi(self, RechercheBonDeTravail):
        _translate = QtCore.QCoreApplication.translate
        RechercheBonDeTravail.setWindowTitle(_translate("RechercheBonDeTravail", "PC2"))
        self.LabelTitre.setText(_translate("RechercheBonDeTravail", "Assistant de Recherche-Bon de travail"))
        self.labelCategorie.setText(_translate("RechercheBonDeTravail", "Catégorie d\'équipement"))
        self.LabelAvant.setText(_translate("RechercheBonDeTravail", "Avant le"))
        self.calendrierAvant.setDisplayFormat(_translate("RechercheBonDeTravail", "dd-MM-yyyy"))
        self.LabelApres.setText(_translate("RechercheBonDeTravail", "Après le"))
        self.calendrierApres.setDisplayFormat(_translate("RechercheBonDeTravail", "dd-MM-yyyy"))
        self.LabelEtat.setText(_translate("RechercheBonDeTravail", "État"))
        self.LabelCentreService.setText(_translate("RechercheBonDeTravail", "Centre de service"))
        self.LabelDescription.setText(_translate("RechercheBonDeTravail", "Description de la situation"))
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
        item.setText(_translate("RechercheBonDeTravail", "Centre de service"))
        item = self.tableResultats.horizontalHeaderItem(4)
        item.setText(_translate("RechercheBonDeTravail", "État"))
        item = self.tableResultats.horizontalHeaderItem(5)
        item.setText(_translate("RechercheBonDeTravail", "Date"))
        item = self.tableResultats.horizontalHeaderItem(6)
        item.setText(_translate("RechercheBonDeTravail", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RechercheBonDeTravail = QtWidgets.QWidget()
    ui = Ui_RechercheBonDeTravail()
    ui.setupUi(RechercheBonDeTravail)
    RechercheBonDeTravail.show()
    sys.exit(app.exec_())

