# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Statistique.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Statistique(object):
    def setupUi(self, Statistique):
        Statistique.setObjectName("Statistique")
        Statistique.resize(1514, 1271)
        Statistique.setStyleSheet("QPushButton {\n"
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
"border-radius: 8px;\n"
"background:rgb(169, 167, 170)\n"
"}\n"
"#MainFrame {\n"
"\n"
"background: white;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Statistique)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Statistique)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pie-chart (1).png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Statistique)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/pie-chart (1).png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Labeltitre = QtWidgets.QLabel(Statistique)
        self.Labeltitre.setMaximumSize(QtCore.QSize(800, 150))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Labeltitre.setFont(font)
        self.Labeltitre.setObjectName("Labeltitre")
        self.horizontalLayout.addWidget(self.Labeltitre)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LabelnombreTotalEquipement = QtWidgets.QLabel(Statistique)
        self.LabelnombreTotalEquipement.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelnombreTotalEquipement.setFont(font)
        self.LabelnombreTotalEquipement.setObjectName("LabelnombreTotalEquipement")
        self.horizontalLayout_2.addWidget(self.LabelnombreTotalEquipement)
        self.textBrowserNombreTotalEquipements = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserNombreTotalEquipements.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserNombreTotalEquipements.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserNombreTotalEquipements.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserNombreTotalEquipements.setObjectName("textBrowserNombreTotalEquipements")
        self.horizontalLayout_2.addWidget(self.textBrowserNombreTotalEquipements)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.nombreEtatdeService = QtWidgets.QLabel(Statistique)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nombreEtatdeService.setFont(font)
        self.nombreEtatdeService.setObjectName("nombreEtatdeService")
        self.horizontalLayout_6.addWidget(self.nombreEtatdeService)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.LabelMaintenance = QtWidgets.QLabel(Statistique)
        self.LabelMaintenance.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelMaintenance.setFont(font)
        self.LabelMaintenance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelMaintenance.setObjectName("LabelMaintenance")
        self.verticalLayout_6.addWidget(self.LabelMaintenance)
        self.LabelService = QtWidgets.QLabel(Statistique)
        self.LabelService.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelService.setFont(font)
        self.LabelService.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelService.setObjectName("LabelService")
        self.verticalLayout_6.addWidget(self.LabelService)
        self.LabelRebus = QtWidgets.QLabel(Statistique)
        self.LabelRebus.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelRebus.setFont(font)
        self.LabelRebus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelRebus.setObjectName("LabelRebus")
        self.verticalLayout_6.addWidget(self.LabelRebus)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowserEnMaintenance = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserEnMaintenance.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserEnMaintenance.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserEnMaintenance.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserEnMaintenance.setObjectName("textBrowserEnMaintenance")
        self.verticalLayout_7.addWidget(self.textBrowserEnMaintenance)
        self.textBrowserEnService = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserEnService.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserEnService.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserEnService.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserEnService.setObjectName("textBrowserEnService")
        self.verticalLayout_7.addWidget(self.textBrowserEnService)
        self.textBrowserAuRebus = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserAuRebus.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserAuRebus.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserAuRebus.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserAuRebus.setObjectName("textBrowserAuRebus")
        self.verticalLayout_7.addWidget(self.textBrowserAuRebus)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LabelnombreProvenance = QtWidgets.QLabel(Statistique)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelnombreProvenance.setFont(font)
        self.LabelnombreProvenance.setObjectName("LabelnombreProvenance")
        self.horizontalLayout_3.addWidget(self.LabelnombreProvenance)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LabelProvenance = QtWidgets.QLabel(Statistique)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelProvenance.setFont(font)
        self.LabelProvenance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelProvenance.setObjectName("LabelProvenance")
        self.horizontalLayout_4.addWidget(self.LabelProvenance)
        self.comboBoxProvenance = QtWidgets.QComboBox(Statistique)
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.horizontalLayout_4.addWidget(self.comboBoxProvenance)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LabelNombreProvenance = QtWidgets.QLabel(Statistique)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelNombreProvenance.setFont(font)
        self.LabelNombreProvenance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelNombreProvenance.setObjectName("LabelNombreProvenance")
        self.horizontalLayout_5.addWidget(self.LabelNombreProvenance)
        self.textBrowserEquipementProvenance = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserEquipementProvenance.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserEquipementProvenance.setObjectName("textBrowserEquipementProvenance")
        self.horizontalLayout_5.addWidget(self.textBrowserEquipementProvenance)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 2, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(Statistique)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LabelQuasiNeuf = QtWidgets.QLabel(Statistique)
        self.LabelQuasiNeuf.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelQuasiNeuf.setFont(font)
        self.LabelQuasiNeuf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelQuasiNeuf.setObjectName("LabelQuasiNeuf")
        self.verticalLayout_2.addWidget(self.LabelQuasiNeuf)
        self.LabelAcceptable = QtWidgets.QLabel(Statistique)
        self.LabelAcceptable.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelAcceptable.setFont(font)
        self.LabelAcceptable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelAcceptable.setObjectName("LabelAcceptable")
        self.verticalLayout_2.addWidget(self.LabelAcceptable)
        self.LabelFinDeVie = QtWidgets.QLabel(Statistique)
        self.LabelFinDeVie.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelFinDeVie.setFont(font)
        self.LabelFinDeVie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelFinDeVie.setObjectName("LabelFinDeVie")
        self.verticalLayout_2.addWidget(self.LabelFinDeVie)
        self.LabelDesuet = QtWidgets.QLabel(Statistique)
        self.LabelDesuet.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LabelDesuet.setFont(font)
        self.LabelDesuet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelDesuet.setObjectName("LabelDesuet")
        self.verticalLayout_2.addWidget(self.LabelDesuet)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowserQuasiNeuf = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserQuasiNeuf.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserQuasiNeuf.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserQuasiNeuf.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserQuasiNeuf.setObjectName("textBrowserQuasiNeuf")
        self.verticalLayout_3.addWidget(self.textBrowserQuasiNeuf)
        self.textBrowserAcceptable = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserAcceptable.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserAcceptable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserAcceptable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserAcceptable.setObjectName("textBrowserAcceptable")
        self.verticalLayout_3.addWidget(self.textBrowserAcceptable)
        self.textBrowserEnFinDeVie = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserEnFinDeVie.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserEnFinDeVie.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserEnFinDeVie.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserEnFinDeVie.setObjectName("textBrowserEnFinDeVie")
        self.verticalLayout_3.addWidget(self.textBrowserEnFinDeVie)
        self.textBrowserDesuet = QtWidgets.QTextBrowser(Statistique)
        self.textBrowserDesuet.setMaximumSize(QtCore.QSize(100, 50))
        self.textBrowserDesuet.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserDesuet.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserDesuet.setObjectName("textBrowserDesuet")
        self.verticalLayout_3.addWidget(self.textBrowserDesuet)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.gridLayout.addLayout(self.verticalLayout_8, 3, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.LabelCentreDeService = QtWidgets.QLabel(Statistique)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelCentreDeService.setFont(font)
        self.LabelCentreDeService.setObjectName("LabelCentreDeService")
        self.horizontalLayout_10.addWidget(self.LabelCentreDeService)
        self.comboBoxCentreService = QtWidgets.QComboBox(Statistique)
        self.comboBoxCentreService.setObjectName("comboBoxCentreService")
        self.horizontalLayout_10.addWidget(self.comboBoxCentreService)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tableResumeInventaire = QtWidgets.QTableWidget(Statistique)
        self.tableResumeInventaire.setMinimumSize(QtCore.QSize(293, 400))
        self.tableResumeInventaire.setMaximumSize(QtCore.QSize(1000, 500))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.tableResumeInventaire.setFont(font)
        self.tableResumeInventaire.setStyleSheet("padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247, 247, 247)")
        self.tableResumeInventaire.setLineWidth(10)
        self.tableResumeInventaire.setMidLineWidth(9)
        self.tableResumeInventaire.setObjectName("tableResumeInventaire")
        self.tableResumeInventaire.setColumnCount(2)
        self.tableResumeInventaire.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableResumeInventaire.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumeInventaire.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumeInventaire.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumeInventaire.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResumeInventaire.setHorizontalHeaderItem(1, item)
        self.tableResumeInventaire.horizontalHeader().setDefaultSectionSize(134)
        self.tableResumeInventaire.horizontalHeader().setMinimumSectionSize(15)
        self.tableResumeInventaire.verticalHeader().setDefaultSectionSize(30)
        self.tableResumeInventaire.verticalHeader().setMinimumSectionSize(20)
        self.tableResumeInventaire.verticalHeader().setSortIndicatorShown(False)
        self.tableResumeInventaire.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_11.addWidget(self.tableResumeInventaire)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout_5, 4, 0, 1, 2)

        self.retranslateUi(Statistique)
        QtCore.QMetaObject.connectSlotsByName(Statistique)

    def retranslateUi(self, Statistique):
        _translate = QtCore.QCoreApplication.translate
        Statistique.setWindowTitle(_translate("Statistique", "Form"))
        self.Labeltitre.setText(_translate("Statistique", "Statistiques"))
        self.LabelnombreTotalEquipement.setText(_translate("Statistique", "Nombre total d\'équipements"))
        self.textBrowserNombreTotalEquipements.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.nombreEtatdeService.setText(_translate("Statistique", "Équipements par état de service"))
        self.LabelMaintenance.setText(_translate("Statistique", "En maintenance :"))
        self.LabelService.setText(_translate("Statistique", "En service :"))
        self.LabelRebus.setText(_translate("Statistique", "Au rebus :"))
        self.textBrowserEnMaintenance.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.textBrowserEnService.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowserAuRebus.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.LabelnombreProvenance.setText(_translate("Statistique", "Équipements par provenance"))
        self.LabelProvenance.setText(_translate("Statistique", "Provenance choisie :"))
        self.LabelNombreProvenance.setText(_translate("Statistique", "Équipements de cette provenance :"))
        self.label_11.setText(_translate("Statistique", "Équipements par état de conservation"))
        self.LabelQuasiNeuf.setText(_translate("Statistique", "Quasi-neuf :"))
        self.LabelAcceptable.setText(_translate("Statistique", "Acceptable :"))
        self.LabelFinDeVie.setText(_translate("Statistique", "En fin de vie :"))
        self.LabelDesuet.setText(_translate("Statistique", "Désuet :"))
        self.textBrowserQuasiNeuf.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowserAcceptable.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowserEnFinDeVie.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowserDesuet.setHtml(_translate("Statistique", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">400</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.LabelCentreDeService.setText(_translate("Statistique", "Résume de l\'inventaire par centre de service"))
        item = self.tableResumeInventaire.verticalHeaderItem(0)
        item.setText(_translate("Statistique", "1"))
        item = self.tableResumeInventaire.verticalHeaderItem(1)
        item.setText(_translate("Statistique", "2"))
        item = self.tableResumeInventaire.verticalHeaderItem(2)
        item.setText(_translate("Statistique", "3"))
        item = self.tableResumeInventaire.horizontalHeaderItem(0)
        item.setText(_translate("Statistique", "Catégorie d\'équipement"))
        item = self.tableResumeInventaire.horizontalHeaderItem(1)
        item.setText(_translate("Statistique", "Quantité"))

