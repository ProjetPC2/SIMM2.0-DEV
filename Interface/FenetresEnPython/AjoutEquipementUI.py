# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AjoutEquipement.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AjoutEquipement(object):
    def setupUi(self, AjoutEquipement):
        AjoutEquipement.setObjectName("AjoutEquipement")
        AjoutEquipement.resize(964, 711)
        AjoutEquipement.setStyleSheet("background:white;")
        self.gridLayout = QtWidgets.QGridLayout(AjoutEquipement)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(AjoutEquipement)
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
        self.labelTitreEtatDeService.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreEtatDeService.setObjectName("labelTitreEtatDeService")
        self.horizontalLayout_4.addWidget(self.labelTitreEtatDeService)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelEtatDeService = QtWidgets.QLabel(self.frame)
        self.labelEtatDeService.setStyleSheet("background: white;")
        self.labelEtatDeService.setObjectName("labelEtatDeService")
        self.verticalLayout_3.addWidget(self.labelEtatDeService)
        self.radioButtonEnService = QtWidgets.QRadioButton(self.frame)
        self.radioButtonEnService.setStyleSheet("background:white;")
        self.radioButtonEnService.setObjectName("radioButtonEnService")
        self.verticalLayout_3.addWidget(self.radioButtonEnService)
        self.radioButtonEnMaintenance = QtWidgets.QRadioButton(self.frame)
        self.radioButtonEnMaintenance.setStyleSheet("background:white;")
        self.radioButtonEnMaintenance.setObjectName("radioButtonEnMaintenance")
        self.verticalLayout_3.addWidget(self.radioButtonEnMaintenance)
        self.radioButtonAuRebus = QtWidgets.QRadioButton(self.frame)
        self.radioButtonAuRebus.setStyleSheet("background:white;")
        self.radioButtonAuRebus.setObjectName("radioButtonAuRebus")
        self.verticalLayout_3.addWidget(self.radioButtonAuRebus)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(AjoutEquipement)
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
        self.labelTitreEtatDeConservation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitreEtatDeConservation.setObjectName("labelTitreEtatDeConservation")
        self.horizontalLayout_6.addWidget(self.labelTitreEtatDeConservation)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelEtatDeConservation = QtWidgets.QLabel(self.frame_2)
        self.labelEtatDeConservation.setStyleSheet("background: white;")
        self.labelEtatDeConservation.setObjectName("labelEtatDeConservation")
        self.verticalLayout_4.addWidget(self.labelEtatDeConservation)
        self.radioButtonQuasiNeuf = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonQuasiNeuf.setStyleSheet("background:white;")
        self.radioButtonQuasiNeuf.setObjectName("radioButtonQuasiNeuf")
        self.verticalLayout_4.addWidget(self.radioButtonQuasiNeuf)
        self.radioButtonAcceptable = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonAcceptable.setStyleSheet("background:white;")
        self.radioButtonAcceptable.setObjectName("radioButtonAcceptable")
        self.verticalLayout_4.addWidget(self.radioButtonAcceptable)
        self.radioButtonEnFinDeVie = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonEnFinDeVie.setStyleSheet("background:white;")
        self.radioButtonEnFinDeVie.setObjectName("radioButtonEnFinDeVie")
        self.verticalLayout_4.addWidget(self.radioButtonEnFinDeVie)
        self.radioButtonDesuet = QtWidgets.QRadioButton(self.frame_2)
        self.radioButtonDesuet.setStyleSheet("background:white;")
        self.radioButtonDesuet.setObjectName("radioButtonDesuet")
        self.verticalLayout_4.addWidget(self.radioButtonDesuet)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.layoutTitre = QtWidgets.QHBoxLayout()
        self.layoutTitre.setObjectName("layoutTitre")
        self.label = QtWidgets.QLabel(AjoutEquipement)
        self.label.setStyleSheet("background:white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/add1.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.layoutTitre.addWidget(self.label)
        self.titreModificationEquipement = QtWidgets.QLabel(AjoutEquipement)
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
        self.gridLayout.addLayout(self.layoutTitre, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutChampsModifiables = QtWidgets.QVBoxLayout()
        self.layoutChampsModifiables.setObjectName("layoutChampsModifiables")
        self.labelVide = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelVide.setFont(font)
        self.labelVide.setStyleSheet("background: white;")
        self.labelVide.setText("")
        self.labelVide.setObjectName("labelVide")
        self.layoutChampsModifiables.addWidget(self.labelVide)
        self.comboBoxCategorie = QtWidgets.QComboBox(AjoutEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxCategorie.setFont(font)
        self.comboBoxCategorie.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"background:rgb(247, 247, 247);\n"
"}\n"
"    ")
        self.comboBoxCategorie.setMaxCount(2147483645)
        self.comboBoxCategorie.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxCategorie.setObjectName("comboBoxCategorie")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.layoutChampsModifiables.addWidget(self.comboBoxCategorie)
        self.lineEditMarque = QtWidgets.QLineEdit(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditMarque.setFont(font)
        self.lineEditMarque.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:white;\n"
"min-width: 50px;\n"
"max-width: 220px;\n"
"background:rgb(247, 247, 247);\n"
"}")
        self.lineEditMarque.setObjectName("lineEditMarque")
        self.layoutChampsModifiables.addWidget(self.lineEditMarque)
        self.lineEditModele = QtWidgets.QLineEdit(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditModele.setFont(font)
        self.lineEditModele.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:white;\n"
"min-width: 50px;\n"
"max-width: 220px;\n"
"background:rgb(247, 247, 247);\n"
"}")
        self.lineEditModele.setObjectName("lineEditModele")
        self.layoutChampsModifiables.addWidget(self.lineEditModele)
        self.lineEditNoDeSerie = QtWidgets.QLineEdit(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNoDeSerie.setFont(font)
        self.lineEditNoDeSerie.setStyleSheet("QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:white;\n"
"min-width: 50px;\n"
"max-width: 220px;\n"
"background:rgb(247, 247, 247);\n"
"}")
        self.lineEditNoDeSerie.setObjectName("lineEditNoDeSerie")
        self.layoutChampsModifiables.addWidget(self.lineEditNoDeSerie)
        self.comboBoxSalle = QtWidgets.QComboBox(AjoutEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxSalle.setFont(font)
        self.comboBoxSalle.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"background:rgb(247, 247, 247);\n"
"}\n"
"    ")
        self.comboBoxSalle.setMaxCount(2147483645)
        self.comboBoxSalle.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxSalle.setObjectName("comboBoxSalle")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.layoutChampsModifiables.addWidget(self.comboBoxSalle)
        self.comboBoxCentreDeService = QtWidgets.QComboBox(AjoutEquipement)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxCentreDeService.setFont(font)
        self.comboBoxCentreDeService.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"background:rgb(247, 247, 247);\n"
"}\n"
"    ")
        self.comboBoxCentreDeService.setMaxCount(2147483645)
        self.comboBoxCentreDeService.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxCentreDeService.setObjectName("comboBoxCentreDeService")
        self.comboBoxCentreDeService.addItem("")
        self.comboBoxCentreDeService.addItem("")
        self.comboBoxCentreDeService.addItem("")
        self.layoutChampsModifiables.addWidget(self.comboBoxCentreDeService)
        self.dateEditDateDaquisition = QtWidgets.QDateEdit(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEditDateDaquisition.setFont(font)
        self.dateEditDateDaquisition.setStyleSheet("QDateEdit{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background :white;\n"
"max-width:105px;\n"
"background:rgb(247, 247, 247);\n"
"}\n"
"")
        self.dateEditDateDaquisition.setCalendarPopup(True)
        self.dateEditDateDaquisition.setObjectName("dateEditDateDaquisition")
        self.layoutChampsModifiables.addWidget(self.dateEditDateDaquisition)
        self.dateEditDateDuDernierEntretien = QtWidgets.QDateEdit(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEditDateDuDernierEntretien.setFont(font)
        self.dateEditDateDuDernierEntretien.setStyleSheet("QDateEdit{\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background :white;\n"
"max-width:105px;\n"
"background:rgb(247, 247, 247);\n"
"}\n"
"")
        self.dateEditDateDuDernierEntretien.setCalendarPopup(True)
        self.dateEditDateDuDernierEntretien.setObjectName("dateEditDateDuDernierEntretien")
        self.layoutChampsModifiables.addWidget(self.dateEditDateDuDernierEntretien)
        self.comboBoxProvenance = QtWidgets.QComboBox(AjoutEquipement)
        self.comboBoxProvenance.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"background:rgb(247, 247, 247);\n"
"}\n"
"    ")
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.layoutChampsModifiables.addWidget(self.comboBoxProvenance)
        self.lineEditCodeASSET = QtWidgets.QLineEdit(AjoutEquipement)
        self.lineEditCodeASSET.setMinimumSize(QtCore.QSize(127, 0))
        self.lineEditCodeASSET.setMaximumSize(QtCore.QSize(223, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCodeASSET.setFont(font)
        self.lineEditCodeASSET.setStyleSheet("    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"background:rgb(247, 247, 247);")
        self.lineEditCodeASSET.setObjectName("lineEditCodeASSET")
        self.layoutChampsModifiables.addWidget(self.lineEditCodeASSET)
        self.horizontalLayout.addLayout(self.layoutChampsModifiables)
        self.layoutChampsNonModifiables = QtWidgets.QVBoxLayout()
        self.layoutChampsNonModifiables.setObjectName("layoutChampsNonModifiables")
        self.labelID = QtWidgets.QLabel(AjoutEquipement)
        self.labelID.setStyleSheet("background: white;")
        self.labelID.setObjectName("labelID")
        self.layoutChampsNonModifiables.addWidget(self.labelID)
        self.labelCategorie = QtWidgets.QLabel(AjoutEquipement)
        self.labelCategorie.setStyleSheet("background: white;")
        self.labelCategorie.setObjectName("labelCategorie")
        self.layoutChampsNonModifiables.addWidget(self.labelCategorie)
        self.labelMarque = QtWidgets.QLabel(AjoutEquipement)
        self.labelMarque.setStyleSheet("background: white;")
        self.labelMarque.setObjectName("labelMarque")
        self.layoutChampsNonModifiables.addWidget(self.labelMarque)
        self.labelModele = QtWidgets.QLabel(AjoutEquipement)
        self.labelModele.setStyleSheet("background: white;")
        self.labelModele.setObjectName("labelModele")
        self.layoutChampsNonModifiables.addWidget(self.labelModele)
        self.labelNoDeSerie = QtWidgets.QLabel(AjoutEquipement)
        self.labelNoDeSerie.setStyleSheet("background: white;")
        self.labelNoDeSerie.setObjectName("labelNoDeSerie")
        self.layoutChampsNonModifiables.addWidget(self.labelNoDeSerie)
        self.labelSalle = QtWidgets.QLabel(AjoutEquipement)
        self.labelSalle.setStyleSheet("background: white;")
        self.labelSalle.setObjectName("labelSalle")
        self.layoutChampsNonModifiables.addWidget(self.labelSalle)
        self.labelCentreDeService = QtWidgets.QLabel(AjoutEquipement)
        self.labelCentreDeService.setStyleSheet("background: white;")
        self.labelCentreDeService.setObjectName("labelCentreDeService")
        self.layoutChampsNonModifiables.addWidget(self.labelCentreDeService)
        self.labelDateDAquisition = QtWidgets.QLabel(AjoutEquipement)
        self.labelDateDAquisition.setStyleSheet("background: white;")
        self.labelDateDAquisition.setObjectName("labelDateDAquisition")
        self.layoutChampsNonModifiables.addWidget(self.labelDateDAquisition)
        self.labelDateDernierEntretien = QtWidgets.QLabel(AjoutEquipement)
        self.labelDateDernierEntretien.setStyleSheet("background: white;")
        self.labelDateDernierEntretien.setObjectName("labelDateDernierEntretien")
        self.layoutChampsNonModifiables.addWidget(self.labelDateDernierEntretien)
        self.labelProvenance = QtWidgets.QLabel(AjoutEquipement)
        self.labelProvenance.setStyleSheet("background: white;")
        self.labelProvenance.setObjectName("labelProvenance")
        self.layoutChampsNonModifiables.addWidget(self.labelProvenance)
        self.labelCodeASSET = QtWidgets.QLabel(AjoutEquipement)
        self.labelCodeASSET.setObjectName("labelCodeASSET")
        self.layoutChampsNonModifiables.addWidget(self.labelCodeASSET)
        self.horizontalLayout.addLayout(self.layoutChampsNonModifiables)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.layoutTitreLables = QtWidgets.QVBoxLayout()
        self.layoutTitreLables.setObjectName("layoutTitreLables")
        self.label_34 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background: white;")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.layoutTitreLables.addWidget(self.label_34)
        self.label_37 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background: white;")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.layoutTitreLables.addWidget(self.label_37)
        self.label_36 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background: white;")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.layoutTitreLables.addWidget(self.label_36)
        self.label_35 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background: white;")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.layoutTitreLables.addWidget(self.label_35)
        self.label_30 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("background: white;")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.layoutTitreLables.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background: white;")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.layoutTitreLables.addWidget(self.label_31)
        self.label_33 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background: white;")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.layoutTitreLables.addWidget(self.label_33)
        self.label_29 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background: white;")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.layoutTitreLables.addWidget(self.label_29)
        self.label_27 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background: white;")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.layoutTitreLables.addWidget(self.label_27)
        self.label_26 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background: white;")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.layoutTitreLables.addWidget(self.label_26)
        self.label_2 = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.layoutTitreLables.addWidget(self.label_2)
        self.gridLayout.addLayout(self.layoutTitreLables, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTitreCommentaires = QtWidgets.QLabel(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreCommentaires.setFont(font)
        self.labelTitreCommentaires.setStyleSheet("background: white;")
        self.labelTitreCommentaires.setObjectName("labelTitreCommentaires")
        self.horizontalLayout_3.addWidget(self.labelTitreCommentaires)
        self.textEditCommentaires = QtWidgets.QTextEdit(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditCommentaires.setFont(font)
        self.textEditCommentaires.setStyleSheet("QTextEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius: 4px;\n"
"background:white\n"
"}")
        self.textEditCommentaires.setObjectName("textEditCommentaires")
        self.horizontalLayout_3.addWidget(self.textEditCommentaires)
        self.commentaire = QtWidgets.QLabel(AjoutEquipement)
        self.commentaire.setStyleSheet("background: white;")
        self.commentaire.setWordWrap(True)
        self.commentaire.setObjectName("commentaire")
        self.horizontalLayout_3.addWidget(self.commentaire)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.BoutonValider = QtWidgets.QPushButton(AjoutEquipement)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BoutonValider.setFont(font)
        self.BoutonValider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonValider.setStyleSheet("QPushButton {\n"
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
"max-width:220px;\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/check-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonValider.setIcon(icon)
        self.BoutonValider.setObjectName("BoutonValider")
        self.horizontalLayout_8.addWidget(self.BoutonValider)
        self.BoutonModifier = QtWidgets.QPushButton(AjoutEquipement)
        self.BoutonModifier.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonModifier.setStyleSheet("QPushButton {\n"
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
"max-width:220px;\n"
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
        icon1.addPixmap(QtGui.QPixmap("Images/Modify-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonModifier.setIcon(icon1)
        self.BoutonModifier.setIconSize(QtCore.QSize(32, 32))
        self.BoutonModifier.setObjectName("BoutonModifier")
        self.horizontalLayout_8.addWidget(self.BoutonModifier)
        self.BoutonEnregistrer = QtWidgets.QPushButton(AjoutEquipement)
        self.BoutonEnregistrer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonEnregistrer.setStyleSheet("QPushButton {\n"
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
"max-width:220px;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/save (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonEnregistrer.setIcon(icon2)
        self.BoutonEnregistrer.setObjectName("BoutonEnregistrer")
        self.horizontalLayout_8.addWidget(self.BoutonEnregistrer)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 2)

        self.retranslateUi(AjoutEquipement)
        QtCore.QMetaObject.connectSlotsByName(AjoutEquipement)

    def retranslateUi(self, AjoutEquipement):
        _translate = QtCore.QCoreApplication.translate
        AjoutEquipement.setWindowTitle(_translate("AjoutEquipement", "Form"))
        self.labelTitreEtatDeService.setText(_translate("AjoutEquipement", "État de service : "))
        self.labelEtatDeService.setText(_translate("AjoutEquipement", "Ici État de Service"))
        self.radioButtonEnService.setText(_translate("AjoutEquipement", "En service"))
        self.radioButtonEnMaintenance.setText(_translate("AjoutEquipement", "En maintenance"))
        self.radioButtonAuRebus.setText(_translate("AjoutEquipement", "Au rebus"))
        self.labelTitreEtatDeConservation.setText(_translate("AjoutEquipement", "État de Conservation : "))
        self.labelEtatDeConservation.setText(_translate("AjoutEquipement", "Ici État de Conservation"))
        self.radioButtonQuasiNeuf.setText(_translate("AjoutEquipement", "Quasi neuf"))
        self.radioButtonAcceptable.setText(_translate("AjoutEquipement", "Acceptable"))
        self.radioButtonEnFinDeVie.setText(_translate("AjoutEquipement", "En fin de vie"))
        self.radioButtonDesuet.setText(_translate("AjoutEquipement", "Désuet"))
        self.titreModificationEquipement.setText(_translate("AjoutEquipement", "Ajout d\'équipement"))
        self.comboBoxCategorie.setItemText(0, _translate("AjoutEquipement", "Catégorie 1"))
        self.comboBoxCategorie.setItemText(1, _translate("AjoutEquipement", "Catégorie 2"))
        self.comboBoxCategorie.setItemText(2, _translate("AjoutEquipement", "Catégorie 3"))
        self.comboBoxSalle.setItemText(0, _translate("AjoutEquipement", "Salle 1"))
        self.comboBoxSalle.setItemText(1, _translate("AjoutEquipement", "Salle 2"))
        self.comboBoxSalle.setItemText(2, _translate("AjoutEquipement", "Salle 3"))
        self.comboBoxCentreDeService.setItemText(0, _translate("AjoutEquipement", "Centre de service X"))
        self.comboBoxCentreDeService.setItemText(1, _translate("AjoutEquipement", "Centre de service Y"))
        self.comboBoxCentreDeService.setItemText(2, _translate("AjoutEquipement", "Centre de service Z"))
        self.dateEditDateDaquisition.setDisplayFormat(_translate("AjoutEquipement", "dd-MM-yyyy"))
        self.dateEditDateDuDernierEntretien.setDisplayFormat(_translate("AjoutEquipement", "dd-MM-yyyy"))
        self.labelID.setText(_translate("AjoutEquipement", "Ici ID"))
        self.labelCategorie.setText(_translate("AjoutEquipement", "Ici Catégorie"))
        self.labelMarque.setText(_translate("AjoutEquipement", "Ici Marque"))
        self.labelModele.setText(_translate("AjoutEquipement", "Ici Modèle"))
        self.labelNoDeSerie.setText(_translate("AjoutEquipement", "Ici No. de serie"))
        self.labelSalle.setText(_translate("AjoutEquipement", "Ici Salle"))
        self.labelCentreDeService.setText(_translate("AjoutEquipement", "Ici Centre de service"))
        self.labelDateDAquisition.setText(_translate("AjoutEquipement", "Ici Date d\'aquisition"))
        self.labelDateDernierEntretien.setText(_translate("AjoutEquipement", "Ici Date du dernier entretien"))
        self.labelProvenance.setText(_translate("AjoutEquipement", "Ici Provenance"))
        self.labelCodeASSET.setText(_translate("AjoutEquipement", "Ici Code ASSET"))
        self.label_34.setText(_translate("AjoutEquipement", "ID : "))
        self.label_37.setText(_translate("AjoutEquipement", "Catégorie : "))
        self.label_36.setText(_translate("AjoutEquipement", "Marque : "))
        self.label_35.setText(_translate("AjoutEquipement", "Modèle : "))
        self.label_30.setText(_translate("AjoutEquipement", "No. de série : "))
        self.label_31.setText(_translate("AjoutEquipement", "Salle : "))
        self.label_33.setText(_translate("AjoutEquipement", "Centre de service : "))
        self.label_29.setText(_translate("AjoutEquipement", "Date d\'aquisition : "))
        self.label_27.setText(_translate("AjoutEquipement", "Date du dernier entretien : "))
        self.label_26.setText(_translate("AjoutEquipement", "Provenance : "))
        self.label_2.setText(_translate("AjoutEquipement", "Code ASSET :"))
        self.labelTitreCommentaires.setText(_translate("AjoutEquipement", "Commentaires : "))
        self.commentaire.setText(_translate("AjoutEquipement", "commentaires"))
        self.BoutonValider.setText(_translate("AjoutEquipement", "Valider"))
        self.BoutonModifier.setText(_translate("AjoutEquipement", "Modifier"))
        self.BoutonEnregistrer.setText(_translate("AjoutEquipement", "Enregistrer"))

