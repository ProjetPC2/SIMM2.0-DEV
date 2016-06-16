# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Statistique.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(851, 555)
        Form.setStyleSheet("QPushButton {\n"
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
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Labeltitre = QtWidgets.QLabel(Form)
        self.Labeltitre.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Labeltitre.setFont(font)
        self.Labeltitre.setObjectName("Labeltitre")
        self.horizontalLayout.addWidget(self.Labeltitre)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LabelnombreTotalEquipement = QtWidgets.QLabel(Form)
        self.LabelnombreTotalEquipement.setMaximumSize(QtCore.QSize(241, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelnombreTotalEquipement.setFont(font)
        self.LabelnombreTotalEquipement.setObjectName("LabelnombreTotalEquipement")
        self.horizontalLayout_2.addWidget(self.LabelnombreTotalEquipement)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LabelCentreDeService = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LabelCentreDeService.setFont(font)
        self.LabelCentreDeService.setObjectName("LabelCentreDeService")
        self.verticalLayout_5.addWidget(self.LabelCentreDeService)
        self.tableResultats = QtWidgets.QTableWidget(Form)
        self.tableResultats.setMinimumSize(QtCore.QSize(293, 186))
        self.tableResultats.setMaximumSize(QtCore.QSize(120, 200))
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
        self.tableResultats.setColumnCount(2)
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
        self.tableResultats.horizontalHeader().setDefaultSectionSize(134)
        self.tableResultats.horizontalHeader().setMinimumSectionSize(15)
        self.tableResultats.verticalHeader().setDefaultSectionSize(30)
        self.tableResultats.verticalHeader().setMinimumSectionSize(20)
        self.tableResultats.verticalHeader().setSortIndicatorShown(False)
        self.tableResultats.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.tableResultats)
        self.gridLayout.addLayout(self.verticalLayout_5, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.nombreEtatdeService = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nombreEtatdeService.setFont(font)
        self.nombreEtatdeService.setObjectName("nombreEtatdeService")
        self.horizontalLayout_13.addWidget(self.nombreEtatdeService)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.LabelService = QtWidgets.QLabel(Form)
        self.LabelService.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelService.setFont(font)
        self.LabelService.setObjectName("LabelService")
        self.horizontalLayout_6.addWidget(self.LabelService)
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_6.addWidget(self.textBrowser_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.LabelMaintenance = QtWidgets.QLabel(Form)
        self.LabelMaintenance.setMaximumSize(QtCore.QSize(103, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelMaintenance.setFont(font)
        self.LabelMaintenance.setObjectName("LabelMaintenance")
        self.horizontalLayout_7.addWidget(self.LabelMaintenance)
        self.textBrowser_6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_7.addWidget(self.textBrowser_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.LabelRebus = QtWidgets.QLabel(Form)
        self.LabelRebus.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelRebus.setFont(font)
        self.LabelRebus.setObjectName("LabelRebus")
        self.horizontalLayout_14.addWidget(self.LabelRebus)
        self.textBrowser_10 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_10.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.horizontalLayout_14.addWidget(self.textBrowser_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LabelQuasiNeuf = QtWidgets.QLabel(Form)
        self.LabelQuasiNeuf.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelQuasiNeuf.setFont(font)
        self.LabelQuasiNeuf.setObjectName("LabelQuasiNeuf")
        self.horizontalLayout_5.addWidget(self.LabelQuasiNeuf)
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_5.addWidget(self.textBrowser_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LabelAcceptable = QtWidgets.QLabel(Form)
        self.LabelAcceptable.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelAcceptable.setFont(font)
        self.LabelAcceptable.setObjectName("LabelAcceptable")
        self.horizontalLayout_3.addWidget(self.LabelAcceptable)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.LabelFinDeVie = QtWidgets.QLabel(Form)
        self.LabelFinDeVie.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelFinDeVie.setFont(font)
        self.LabelFinDeVie.setObjectName("LabelFinDeVie")
        self.horizontalLayout_10.addWidget(self.LabelFinDeVie)
        self.textBrowser_9 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_9.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.horizontalLayout_10.addWidget(self.textBrowser_9)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LabelDesuet = QtWidgets.QLabel(Form)
        self.LabelDesuet.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelDesuet.setFont(font)
        self.LabelDesuet.setObjectName("LabelDesuet")
        self.horizontalLayout_4.addWidget(self.LabelDesuet)
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_4.addWidget(self.textBrowser_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_16.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LabelnombreProvenance = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LabelnombreProvenance.setFont(font)
        self.LabelnombreProvenance.setObjectName("LabelnombreProvenance")
        self.verticalLayout_4.addWidget(self.LabelnombreProvenance)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.LabelProvenance = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelProvenance.setFont(font)
        self.LabelProvenance.setObjectName("LabelProvenance")
        self.horizontalLayout_8.addWidget(self.LabelProvenance)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.LabelNombreProvenance = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelNombreProvenance.setFont(font)
        self.LabelNombreProvenance.setObjectName("LabelNombreProvenance")
        self.horizontalLayout_15.addWidget(self.LabelNombreProvenance)
        self.textBrowser_7 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(50, 26))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout_15.addWidget(self.textBrowser_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_16.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_16, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Labeltitre.setText(_translate("Form", "Statistiques"))
        self.LabelnombreTotalEquipement.setText(_translate("Form", "Nombre total d\'équipement"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelCentreDeService.setText(_translate("Form", "Résume d\'inventaire par centre de service"))
        item = self.tableResultats.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableResultats.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableResultats.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableResultats.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Catégorie d\'équipement"))
        item = self.tableResultats.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Quantité"))
        self.nombreEtatdeService.setText(_translate("Form", "Nombre d\'équipement par état de service"))
        self.LabelService.setText(_translate("Form", "En service"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelMaintenance.setText(_translate("Form", "En maintenance"))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelRebus.setText(_translate("Form", "Au rebus"))
        self.textBrowser_10.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("Form", "Nombre d\'équipement par état de conservation"))
        self.LabelQuasiNeuf.setText(_translate("Form", "Quasi-neuf"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelAcceptable.setText(_translate("Form", "Acceptable"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelFinDeVie.setText(_translate("Form", "En fin de vie"))
        self.textBrowser_9.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelDesuet.setText(_translate("Form", "Désuet"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelnombreProvenance.setText(_translate("Form", "Nombre d\'équipement par provenance"))
        self.LabelProvenance.setText(_translate("Form", "Provenance choisie:"))
        self.LabelNombreProvenance.setText(_translate("Form", "Équipement de cette provenance:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

