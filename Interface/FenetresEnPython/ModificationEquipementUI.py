# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificationEquipement.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics

class Ui_ModificationEquipement(object):
    def setupUi(self, ModificationEquipement):
        ModificationEquipement.setObjectName("ModificationEquipement")

        width = GetSystemMetrics(0)
        heigth = GetSystemMetrics(1)
        facteur_grandissement_width = 0.9
        facteur_grandissement_heigth = 0.7
        ModificationEquipement.resize(width * facteur_grandissement_width, heigth * facteur_grandissement_heigth)

        ModificationEquipement.setMinimumSize(QtCore.QSize(0, 800))
        ModificationEquipement.setMaximumSize(QtCore.QSize(11111111, 1111111))
        ModificationEquipement.setStyleSheet("QWidget{\n"
"\n"
"background: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"\n"
"}\n"
"\n"
"QDateEdit {\n"
"max-width: 105px\n"
"}\n"
"\n"
"QPushButton {\n"
"color: black;\n"
"background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-color: grey;\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"padding: 3px;\n"
"font: bold 16px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 130px;\n"
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
"\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}")
        self.formLayout = QtWidgets.QFormLayout(ModificationEquipement)
        self.formLayout.setObjectName("formLayout")
        self.layoutTitre = QtWidgets.QHBoxLayout()
        self.layoutTitre.setObjectName("layoutTitre")
        self.label = QtWidgets.QLabel(ModificationEquipement)
        self.label.setStyleSheet("background: white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/add1.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.layoutTitre.addWidget(self.label)
        self.titreModificationEquipement = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.titreModificationEquipement.setFont(font)
        self.titreModificationEquipement.setStyleSheet("background: white;")
        self.titreModificationEquipement.setObjectName("titreModificationEquipement")
        self.layoutTitre.addWidget(self.titreModificationEquipement)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutTitre.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.layoutTitre)
        self.layoutTitreLables = QtWidgets.QVBoxLayout()
        self.layoutTitreLables.setObjectName("layoutTitreLables")
        self.label_34 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background: white;")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.layoutTitreLables.addWidget(self.label_34)
        self.label_37 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background: white;")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.layoutTitreLables.addWidget(self.label_37)
        self.label_36 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background: white;")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.layoutTitreLables.addWidget(self.label_36)
        self.label_35 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background: white;")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.layoutTitreLables.addWidget(self.label_35)
        self.label_30 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("background: white;")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.layoutTitreLables.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background: white;")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.layoutTitreLables.addWidget(self.label_31)
        self.label_33 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background: white;")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.layoutTitreLables.addWidget(self.label_33)
        self.label_29 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background: white;")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.layoutTitreLables.addWidget(self.label_29)
        self.label_27 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background: white;")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.layoutTitreLables.addWidget(self.label_27)
        self.label_3 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.layoutTitreLables.addWidget(self.label_3)
        self.label_26 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background: white;")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.layoutTitreLables.addWidget(self.label_26)
        self.label_2 = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.layoutTitreLables.addWidget(self.label_2)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.layoutTitreLables)
        self.layoutChamps = QtWidgets.QVBoxLayout()
        self.layoutChamps.setObjectName("layoutChamps")
        self.labelId = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelId.setFont(font)
        self.labelId.setStyleSheet("QLabel\n"
"\n"
"{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:rgb(247,247,247);\n"
"}\n"
"")
        self.labelId.setText("")
        self.labelId.setObjectName("labelId")
        self.layoutChamps.addWidget(self.labelId)
        self.comboBoxCategorie = QtWidgets.QComboBox(ModificationEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxCategorie.setFont(font)
        self.comboBoxCategorie.setMaxCount(2147483645)
        self.comboBoxCategorie.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxCategorie.setObjectName("comboBoxCategorie")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.layoutChamps.addWidget(self.comboBoxCategorie)
        self.lineEditMarque = QtWidgets.QLineEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditMarque.setFont(font)
        self.lineEditMarque.setObjectName("lineEditMarque")
        self.layoutChamps.addWidget(self.lineEditMarque)
        self.lineEditModele = QtWidgets.QLineEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditModele.setFont(font)
        self.lineEditModele.setObjectName("lineEditModele")
        self.layoutChamps.addWidget(self.lineEditModele)
        self.lineEditNoDeSerie = QtWidgets.QLineEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNoDeSerie.setFont(font)
        self.lineEditNoDeSerie.setObjectName("lineEditNoDeSerie")
        self.layoutChamps.addWidget(self.lineEditNoDeSerie)
        self.comboBoxSalle = QtWidgets.QComboBox(ModificationEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxSalle.setFont(font)
        self.comboBoxSalle.setMaxCount(2147483645)
        self.comboBoxSalle.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxSalle.setObjectName("comboBoxSalle")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.layoutChamps.addWidget(self.comboBoxSalle)
        self.comboBoxUnite = QtWidgets.QComboBox(ModificationEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxUnite.setFont(font)
        self.comboBoxUnite.setMaxCount(2147483645)
        self.comboBoxUnite.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxUnite.setObjectName("comboBoxUnite")
        self.comboBoxUnite.addItem("")
        self.comboBoxUnite.addItem("")
        self.comboBoxUnite.addItem("")
        self.layoutChamps.addWidget(self.comboBoxUnite)
        self.dateEditDateDaquisition = QtWidgets.QDateEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEditDateDaquisition.setFont(font)
        self.dateEditDateDaquisition.setCalendarPopup(True)
        self.dateEditDateDaquisition.setObjectName("dateEditDateDaquisition")
        self.layoutChamps.addWidget(self.dateEditDateDaquisition)
        self.dateEditDateDuDernierEntretien = QtWidgets.QDateEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEditDateDuDernierEntretien.setFont(font)
        self.dateEditDateDuDernierEntretien.setCalendarPopup(True)
        self.dateEditDateDuDernierEntretien.setObjectName("dateEditDateDuDernierEntretien")
        self.layoutChamps.addWidget(self.dateEditDateDuDernierEntretien)
        self.lineEditFreqEntretien = QtWidgets.QLineEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditFreqEntretien.setFont(font)
        self.lineEditFreqEntretien.setObjectName("lineEditFreqEntretien")
        self.layoutChamps.addWidget(self.lineEditFreqEntretien)
        self.comboBoxProvenance = QtWidgets.QComboBox(ModificationEquipement)
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.layoutChamps.addWidget(self.comboBoxProvenance)
        self.lineEditVoltage = QtWidgets.QLineEdit(ModificationEquipement)
        self.lineEditVoltage.setObjectName("lineEditVoltage")
        self.layoutChamps.addWidget(self.lineEditVoltage)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.layoutChamps)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(ModificationEquipement)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelTitreEtatDeService = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreEtatDeService.setFont(font)
        self.labelTitreEtatDeService.setStyleSheet("background: white;")
        self.labelTitreEtatDeService.setObjectName("labelTitreEtatDeService")
        self.horizontalLayout_4.addWidget(self.labelTitreEtatDeService)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButtonEnService = QtWidgets.QRadioButton(self.frame)
        self.radioButtonEnService.setObjectName("radioButtonEnService")
        self.verticalLayout_3.addWidget(self.radioButtonEnService)
        self.radioButtonEnMaintenance = QtWidgets.QRadioButton(self.frame)
        self.radioButtonEnMaintenance.setObjectName("radioButtonEnMaintenance")
        self.verticalLayout_3.addWidget(self.radioButtonEnMaintenance)
        self.radioButtonAuRebus = QtWidgets.QRadioButton(self.frame)
        self.radioButtonAuRebus.setObjectName("radioButtonAuRebus")
        self.verticalLayout_3.addWidget(self.radioButtonAuRebus)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(ModificationEquipement)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelTitreEtatDeConservation = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreEtatDeConservation.setFont(font)
        self.labelTitreEtatDeConservation.setStyleSheet("background: white;")
        self.labelTitreEtatDeConservation.setObjectName("labelTitreEtatDeConservation")
        self.horizontalLayout_6.addWidget(self.labelTitreEtatDeConservation)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButtonQuasiNeuf = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonQuasiNeuf.setObjectName("radioButtonQuasiNeuf")
        self.verticalLayout_4.addWidget(self.radioButtonQuasiNeuf)
        self.radioButtonAcceptable = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonAcceptable.setObjectName("radioButtonAcceptable")
        self.verticalLayout_4.addWidget(self.radioButtonAcceptable)
        self.radioButtonEnFinDeVie = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonEnFinDeVie.setObjectName("radioButtonEnFinDeVie")
        self.verticalLayout_4.addWidget(self.radioButtonEnFinDeVie)
        self.radioButtonDesuet = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonDesuet.setObjectName("radioButtonDesuet")
        self.verticalLayout_4.addWidget(self.radioButtonDesuet)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTitreCommentaires = QtWidgets.QLabel(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreCommentaires.setFont(font)
        self.labelTitreCommentaires.setObjectName("labelTitreCommentaires")
        self.horizontalLayout_3.addWidget(self.labelTitreCommentaires)
        self.textEditCommentaires = QtWidgets.QTextEdit(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditCommentaires.setFont(font)
        self.textEditCommentaires.setObjectName("textEditCommentaires")
        self.horizontalLayout_3.addWidget(self.textEditCommentaires)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.BoutonValider = QtWidgets.QPushButton(ModificationEquipement)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BoutonValider.setFont(font)
        self.BoutonValider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/check-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonValider.setIcon(icon)
        self.BoutonValider.setObjectName("BoutonValider")
        self.horizontalLayout_8.addWidget(self.BoutonValider)
        self.BoutonModifier = QtWidgets.QPushButton(ModificationEquipement)
        self.BoutonModifier.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/Modify-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonModifier.setIcon(icon1)
        self.BoutonModifier.setIconSize(QtCore.QSize(32, 32))
        self.BoutonModifier.setObjectName("BoutonModifier")
        self.horizontalLayout_8.addWidget(self.BoutonModifier)
        self.BoutonEnregistrer = QtWidgets.QPushButton(ModificationEquipement)
        self.BoutonEnregistrer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonEnregistrer.setIcon(icon2)
        self.BoutonEnregistrer.setObjectName("BoutonEnregistrer")
        self.horizontalLayout_8.addWidget(self.BoutonEnregistrer)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_8)

        self.retranslateUi(ModificationEquipement)
        QtCore.QMetaObject.connectSlotsByName(ModificationEquipement)

    def retranslateUi(self, ModificationEquipement):
        _translate = QtCore.QCoreApplication.translate
        ModificationEquipement.setWindowTitle(_translate("ModificationEquipement", "Form"))
        self.titreModificationEquipement.setText(_translate("ModificationEquipement", "Modification d\'équipement"))
        self.label_34.setText(_translate("ModificationEquipement", "ID : "))
        self.label_37.setText(_translate("ModificationEquipement", "Catégorie : "))
        self.label_36.setText(_translate("ModificationEquipement", "Marque : "))
        self.label_35.setText(_translate("ModificationEquipement", "Modèle : "))
        self.label_30.setText(_translate("ModificationEquipement", "No. de série : "))
        self.label_31.setText(_translate("ModificationEquipement", "Salle : "))
        self.label_33.setText(_translate("ModificationEquipement", "Unité : "))
        self.label_29.setText(_translate("ModificationEquipement", "Date d\'aquisition : "))
        self.label_27.setText(_translate("ModificationEquipement", "Date du dernier entretien : "))
        self.label_3.setText(_translate("ModificationEquipement", "Fréquence d\'entretien (jours): "))
        self.label_26.setText(_translate("ModificationEquipement", "Provenance : "))
        self.label_2.setText(_translate("ModificationEquipement", "Voltage/Courant :"))
        self.comboBoxCategorie.setItemText(0, _translate("ModificationEquipement", "Catégorie 1"))
        self.comboBoxCategorie.setItemText(1, _translate("ModificationEquipement", "Catégorie 2"))
        self.comboBoxCategorie.setItemText(2, _translate("ModificationEquipement", "Catégorie 3"))
        self.comboBoxSalle.setItemText(0, _translate("ModificationEquipement", "Salle 1"))
        self.comboBoxSalle.setItemText(1, _translate("ModificationEquipement", "Salle 2"))
        self.comboBoxSalle.setItemText(2, _translate("ModificationEquipement", "Salle 3"))
        self.comboBoxUnite.setItemText(0, _translate("ModificationEquipement", "Unite X"))
        self.comboBoxUnite.setItemText(1, _translate("ModificationEquipement", "Unite Y"))
        self.comboBoxUnite.setItemText(2, _translate("ModificationEquipement", "Unite Z"))
        self.dateEditDateDaquisition.setDisplayFormat(_translate("ModificationEquipement", "dd-MM-yyyy"))
        self.dateEditDateDuDernierEntretien.setDisplayFormat(_translate("ModificationEquipement", "dd-MM-yyyy"))
        self.labelTitreEtatDeService.setText(_translate("ModificationEquipement", "État de service : "))
        self.radioButtonEnService.setText(_translate("ModificationEquipement", "En service"))
        self.radioButtonEnMaintenance.setText(_translate("ModificationEquipement", "En maintenance"))
        self.radioButtonAuRebus.setText(_translate("ModificationEquipement", "Au rebus"))
        self.labelTitreEtatDeConservation.setText(_translate("ModificationEquipement", "État de Conservation : "))
        self.radioButtonQuasiNeuf.setText(_translate("ModificationEquipement", "Quasi neuf"))
        self.radioButtonAcceptable.setText(_translate("ModificationEquipement", "Acceptable"))
        self.radioButtonEnFinDeVie.setText(_translate("ModificationEquipement", "En fin de vie"))
        self.radioButtonDesuet.setText(_translate("ModificationEquipement", "Désuet"))
        self.labelTitreCommentaires.setText(_translate("ModificationEquipement", "Commentaires : "))
        self.BoutonValider.setText(_translate("ModificationEquipement", "Valider"))
        self.BoutonModifier.setText(_translate("ModificationEquipement", "Modifier"))
        self.BoutonEnregistrer.setText(_translate("ModificationEquipement", "Enregistrer"))

