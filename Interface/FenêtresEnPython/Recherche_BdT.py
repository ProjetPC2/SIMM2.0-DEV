# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rbdt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PC2(object):
    def setupUi(self, PC2):
        PC2.setObjectName("PC2")
        PC2.resize(900, 504)
        PC2.setMaximumSize(QtCore.QSize(900, 765))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../SIMM2.0-DEV/Interface/Images/PC2_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        PC2.setWindowIcon(icon)
        PC2.setStyleSheet("QPushButton {\n"
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
"QMainWindow\n"
"{\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(PC2)
        self.gridLayout.setObjectName("gridLayout")
        self.LabelTitre = QtWidgets.QLabel(PC2)
        self.LabelTitre.setMaximumSize(QtCore.QSize(781, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTitre.setFont(font)
        self.LabelTitre.setObjectName("LabelTitre")
        self.gridLayout.addWidget(self.LabelTitre, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Labelcategorie = QtWidgets.QLabel(PC2)
        self.Labelcategorie.setMaximumSize(QtCore.QSize(197, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labelcategorie.setFont(font)
        self.Labelcategorie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Labelcategorie.setObjectName("Labelcategorie")
        self.horizontalLayout_2.addWidget(self.Labelcategorie)
        self.Labelapres = QtWidgets.QLabel(PC2)
        self.Labelapres.setMaximumSize(QtCore.QSize(115, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labelapres.setFont(font)
        self.Labelapres.setObjectName("Labelapres")
        self.horizontalLayout_2.addWidget(self.Labelapres)
        self.Labelavant = QtWidgets.QLabel(PC2)
        self.Labelavant.setMaximumSize(QtCore.QSize(115, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labelavant.setFont(font)
        self.Labelavant.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Labelavant.setObjectName("Labelavant")
        self.horizontalLayout_2.addWidget(self.Labelavant)
        self.Labeletat = QtWidgets.QLabel(PC2)
        self.Labeletat.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labeletat.setFont(font)
        self.Labeletat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Labeletat.setObjectName("Labeletat")
        self.horizontalLayout_2.addWidget(self.Labeletat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCategorie = QtWidgets.QComboBox(PC2)
        self.buttonCategorie.setMaximumSize(QtCore.QSize(197, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonCategorie.setFont(font)
        self.buttonCategorie.setObjectName("buttonCategorie")
        self.horizontalLayout.addWidget(self.buttonCategorie)
        self.calendrierApres = QtWidgets.QDateEdit(PC2)
        self.calendrierApres.setMaximumSize(QtCore.QSize(115, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendrierApres.setFont(font)
        self.calendrierApres.setCalendarPopup(True)
        self.calendrierApres.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierApres.setObjectName("calendrierApres")
        self.horizontalLayout.addWidget(self.calendrierApres)
        self.calendrierAvant = QtWidgets.QDateEdit(PC2)
        self.calendrierAvant.setMaximumSize(QtCore.QSize(115, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendrierAvant.setFont(font)
        self.calendrierAvant.setCalendarPopup(True)
        self.calendrierAvant.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierAvant.setObjectName("calendrierAvant")
        self.horizontalLayout.addWidget(self.calendrierAvant)
        self.buttonAvant = QtWidgets.QComboBox(PC2)
        self.buttonAvant.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonAvant.setFont(font)
        self.buttonAvant.setObjectName("buttonAvant")
        self.horizontalLayout.addWidget(self.buttonAvant)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        self.buttonRechercher = QtWidgets.QCommandLinkButton(PC2)
        self.buttonRechercher.setMaximumSize(QtCore.QSize(113, 39))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.buttonRechercher.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../SIMM2.0-DEV/Interface/Images/PdC_Bouton_Rechercher2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRechercher.setIcon(icon1)
        self.buttonRechercher.setObjectName("buttonRechercher")
        self.gridLayout.addWidget(self.buttonRechercher, 3, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LabelCdS = QtWidgets.QLabel(PC2)
        self.LabelCdS.setMaximumSize(QtCore.QSize(146, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelCdS.setFont(font)
        self.LabelCdS.setObjectName("LabelCdS")
        self.horizontalLayout_4.addWidget(self.LabelCdS)
        self.Labeldescription = QtWidgets.QLabel(PC2)
        self.Labeldescription.setMaximumSize(QtCore.QSize(193, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labeldescription.setFont(font)
        self.Labeldescription.setObjectName("Labeldescription")
        self.horizontalLayout_4.addWidget(self.Labeldescription)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonCdS = QtWidgets.QComboBox(PC2)
        self.buttonCdS.setMaximumSize(QtCore.QSize(145, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonCdS.setFont(font)
        self.buttonCdS.setObjectName("buttonCdS")
        self.horizontalLayout_3.addWidget(self.buttonCdS)
        self.lineEditDescription = QtWidgets.QPlainTextEdit(PC2)
        self.lineEditDescription.setMaximumSize(QtCore.QSize(194, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditDescription.setFont(font)
        self.lineEditDescription.setObjectName("lineEditDescription")
        self.horizontalLayout_3.addWidget(self.lineEditDescription)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.tableResultats = QtWidgets.QTableWidget(PC2)
        self.tableResultats.setMinimumSize(QtCore.QSize(200, 0))
        self.tableResultats.setMaximumSize(QtCore.QSize(900, 16777215))
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
        self.tableResultats.horizontalHeader().setDefaultSectionSize(134)
        self.tableResultats.horizontalHeader().setMinimumSectionSize(15)
        self.tableResultats.verticalHeader().setDefaultSectionSize(30)
        self.tableResultats.verticalHeader().setMinimumSectionSize(20)
        self.tableResultats.verticalHeader().setSortIndicatorShown(False)
        self.tableResultats.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableResultats, 6, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.tableResultats.raise_()
        self.buttonRechercher.raise_()

        self.retranslateUi(PC2)
        QtCore.QMetaObject.connectSlotsByName(PC2)

    def retranslateUi(self, PC2):
        _translate = QtCore.QCoreApplication.translate
        PC2.setWindowTitle(_translate("PC2", "PC2"))
        self.LabelTitre.setText(_translate("PC2", "Assistant de Recherche-Bon de travail"))
        self.Labelcategorie.setText(_translate("PC2", "Catégorie d\'équipement"))
        self.Labelapres.setText(_translate("PC2", "Après le"))
        self.Labelavant.setText(_translate("PC2", "Avant le"))
        self.Labeletat.setText(_translate("PC2", "État"))
        self.calendrierApres.setDisplayFormat(_translate("PC2", "dd-MM-yyyy"))
        self.buttonRechercher.setText(_translate("PC2", "Rechercher"))
        self.LabelCdS.setText(_translate("PC2", "Centre de service"))
        self.Labeldescription.setText(_translate("PC2", "Description de la situation"))
        item = self.tableResultats.verticalHeaderItem(0)
        item.setText(_translate("PC2", "1"))
        item = self.tableResultats.verticalHeaderItem(1)
        item.setText(_translate("PC2", "2"))
        item = self.tableResultats.verticalHeaderItem(2)
        item.setText(_translate("PC2", "3"))
        item = self.tableResultats.horizontalHeaderItem(0)
        item.setText(_translate("PC2", "ID"))
        item = self.tableResultats.horizontalHeaderItem(1)
        item.setText(_translate("PC2", "Catégorie d\'équipement"))
        item = self.tableResultats.horizontalHeaderItem(2)
        item.setText(_translate("PC2", "Modèle"))
        item = self.tableResultats.horizontalHeaderItem(3)
        item.setText(_translate("PC2", "Centre de service"))
        item = self.tableResultats.horizontalHeaderItem(4)
        item.setText(_translate("PC2", "État"))
        item = self.tableResultats.horizontalHeaderItem(5)
        item.setText(_translate("PC2", "Date"))
        item = self.tableResultats.horizontalHeaderItem(6)
        item.setText(_translate("PC2", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PC2 = QtWidgets.QWidget()
    ui = Ui_PC2()
    ui.setupUi(PC2)
    PC2.show()
    sys.exit(app.exec_())

