# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AjoutEquipementUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime

import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QDate
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from BDD.EquipementManager import EquipementManager
from Interface.Stockage import Equipement


class AjoutEquipementUI(object):
    def setupUi(self, MainFrame):
        MainFrame.setObjectName("MainFrame")
        MainFrame.resize(781, 765)
        MainFrame.setStyleSheet("#MainFrame {\n"
"\n"
"background: white;\n"
"}\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"min-width: 50px;\n"
"max-width: 150px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"max-width: 105px\n"
"}\n"
"\n"
"QPushButton {\n"
"color: black;\n"
"background-color: rgb(240, 240, 240);\n"
"border-width: 2px;\n"
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
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 8em;\n"
"    max-width: 200px;\n"
"    \n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:rgb(241, 241, 241);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"   \n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgrey;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.formLayout = QtWidgets.QFormLayout(MainFrame)
        self.formLayout.setObjectName("formLayout")
        self.layoutTitre = QtWidgets.QHBoxLayout()
        self.layoutTitre.setObjectName("layoutTitre")
        self.titreAjoutEquipementUI = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.titreAjoutEquipementUI.setFont(font)
        self.titreAjoutEquipementUI.setObjectName("titreAjoutEquipementUI")
        self.layoutTitre.addWidget(self.titreAjoutEquipementUI)
        self.label = QtWidgets.QLabel(MainFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../SIMM-2.0/Apprentissage Python/exercices/Hatim/Accueil/plus (2).png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.layoutTitre.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutTitre.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.layoutTitre)
        self.layoutTitreLables = QtWidgets.QVBoxLayout()
        self.layoutTitreLables.setObjectName("layoutTitreLables")
        self.label_34 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.layoutTitreLables.addWidget(self.label_34)
        self.label_37 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.layoutTitreLables.addWidget(self.label_37)
        self.label_36 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.layoutTitreLables.addWidget(self.label_36)
        self.label_35 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.layoutTitreLables.addWidget(self.label_35)
        self.label_30 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.layoutTitreLables.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.layoutTitreLables.addWidget(self.label_31)
        self.label_33 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.layoutTitreLables.addWidget(self.label_33)
        self.label_29 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.layoutTitreLables.addWidget(self.label_29)
        self.label_27 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.layoutTitreLables.addWidget(self.label_27)
        self.label_26 = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.layoutTitreLables.addWidget(self.label_26)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.layoutTitreLables)
        self.layoutChamps = QtWidgets.QVBoxLayout()
        self.layoutChamps.setObjectName("layoutChamps")
        self.labelId = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelId.setFont(font)
        self.labelId.setObjectName("labelId")
        self.layoutChamps.addWidget(self.labelId)
        self.comboBoxCategorie = QtWidgets.QComboBox(MainFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBoxCategorie.setFont(font)
        self.comboBoxCategorie.setMaxCount(2147483645)
        self.comboBoxCategorie.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxCategorie.setObjectName("comboBoxCategorie")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.comboBoxCategorie.addItem("")
        self.layoutChamps.addWidget(self.comboBoxCategorie)
        self.lineEditMarque = QtWidgets.QLineEdit(MainFrame)
        self.lineEditMarque.setObjectName("lineEditMarque")
        self.layoutChamps.addWidget(self.lineEditMarque)
        self.lineEditModele = QtWidgets.QLineEdit(MainFrame)
        self.lineEditModele.setObjectName("lineEditModele")
        self.layoutChamps.addWidget(self.lineEditModele)
        self.lineEditNoDeSerie = QtWidgets.QLineEdit(MainFrame)
        self.lineEditNoDeSerie.setObjectName("lineEditNoDeSerie")
        self.layoutChamps.addWidget(self.lineEditNoDeSerie)
        self.comboBoxSalle = QtWidgets.QComboBox(MainFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBoxSalle.setFont(font)
        self.comboBoxSalle.setMaxCount(2147483645)
        self.comboBoxSalle.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxSalle.setObjectName("comboBoxSalle")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItem("")
        self.layoutChamps.addWidget(self.comboBoxSalle)
        self.comboBoxCentreDeService = QtWidgets.QComboBox(MainFrame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBoxCentreDeService.setFont(font)
        self.comboBoxCentreDeService.setMaxCount(2147483645)
        self.comboBoxCentreDeService.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxCentreDeService.setObjectName("comboBoxCentreDeService")
        self.comboBoxCentreDeService.addItem("")
        self.comboBoxCentreDeService.addItem("")
        self.comboBoxCentreDeService.addItem("")
        self.layoutChamps.addWidget(self.comboBoxCentreDeService)
        self.dateEditDateDaquisition = QtWidgets.QDateEdit(MainFrame)
        self.dateEditDateDaquisition.setObjectName("dateEditDateDaquisition")
        self.layoutChamps.addWidget(self.dateEditDateDaquisition)
        self.dateEditDateDuDernierEntretien = QtWidgets.QDateEdit(MainFrame)
        self.dateEditDateDuDernierEntretien.setObjectName("dateEditDateDuDernierEntretien")
        self.layoutChamps.addWidget(self.dateEditDateDuDernierEntretien)

        self.comboBoxProvenance = QtWidgets.QComboBox(MainFrame)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBoxProvenance.setFont(font)
        self.comboBoxProvenance.setMaxCount(2147483645)
        self.comboBoxProvenance.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxProvenance.setObjectName("comboBoxProvenance")
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("")

        self.layoutChamps.addWidget(self.comboBoxProvenance)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.layoutChamps)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(MainFrame)
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
        self.frame_2 = QtWidgets.QFrame(MainFrame)
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
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.boutonValider = QtWidgets.QPushButton(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonValider.setFont(font)
        self.boutonValider.setObjectName("boutonValider")
        self.horizontalLayout_8.addWidget(self.boutonValider)
        # spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_8.addItem(spacerItem2)

        self.formLayout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_8)


        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTitreCommentaires = QtWidgets.QLabel(MainFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTitreCommentaires.setFont(font)
        self.labelTitreCommentaires.setObjectName("labelTitreCommentaires")
        self.horizontalLayout_3.addWidget(self.labelTitreCommentaires)
        self.textEditCommentaires = QtWidgets.QTextEdit(MainFrame)
        self.textEditCommentaires.setObjectName("textEditCommentaires")
        self.horizontalLayout_3.addWidget(self.textEditCommentaires)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)

        self.retranslateUi(MainFrame)
        self.ajout()
        QtCore.QMetaObject.connectSlotsByName(MainFrame)

    def retranslateUi(self, MainFrame):
        _translate = QtCore.QCoreApplication.translate
        MainFrame.setWindowTitle(_translate("MainFrame", "Form"))
        self.titreAjoutEquipementUI.setText(_translate("MainFrame", "Ajout d\'équipement"))
        self.label_34.setText(_translate("MainFrame", "ID : "))
        self.label_37.setText(_translate("MainFrame", "Catégorie : "))
        self.label_36.setText(_translate("MainFrame", "Marque : "))
        self.label_35.setText(_translate("MainFrame", "Modèle : "))
        self.label_30.setText(_translate("MainFrame", "No. de série : "))
        self.label_31.setText(_translate("MainFrame", "Salle : "))
        self.label_33.setText(_translate("MainFrame", "Centre de service : "))
        self.label_29.setText(_translate("MainFrame", "Date d\'aquisition : "))
        self.label_27.setText(_translate("MainFrame", "Date du dernier entretien : "))
        self.label_26.setText(_translate("MainFrame", "Provenance : "))
        # self.labelId.setText(_translate("MainFrame", "27"))
        self.comboBoxCategorie.setItemText(0, _translate("MainFrame", "Catégorie 1"))
        self.comboBoxCategorie.setItemText(1, _translate("MainFrame", "Catégorie 2"))
        self.comboBoxCategorie.setItemText(2, _translate("MainFrame", "Catégorie 3"))
        self.comboBoxSalle.setItemText(0, _translate("MainFrame", "Salle 1"))
        self.comboBoxSalle.setItemText(1, _translate("MainFrame", "Salle 2"))
        self.comboBoxSalle.setItemText(2, _translate("MainFrame", "Salle 3"))
        self.comboBoxCentreDeService.setItemText(0, _translate("MainFrame", "Centre de service X"))
        self.comboBoxCentreDeService.setItemText(1, _translate("MainFrame", "Centre de service Y"))
        self.comboBoxCentreDeService.setItemText(2, _translate("MainFrame", "Centre de service Z"))
        self.labelTitreEtatDeService.setText(_translate("MainFrame", "État de service : "))
        self.radioButtonEnService.setText(_translate("MainFrame", "En service"))
        self.radioButtonEnMaintenance.setText(_translate("MainFrame", "En maintenance"))
        self.radioButtonAuRebus.setText(_translate("MainFrame", "Au rebus"))
        self.labelTitreEtatDeConservation.setText(_translate("MainFrame", "État de Conservation : "))
        self.radioButtonQuasiNeuf.setText(_translate("MainFrame", "Quasi neuf"))
        self.radioButtonAcceptable.setText(_translate("MainFrame", "Acceptable"))
        self.radioButtonEnFinDeVie.setText(_translate("MainFrame", "En fin de vie"))
        self.radioButtonDesuet.setText(_translate("MainFrame", "Desuet"))
        self.boutonValider.setText(_translate("MainFrame", "Valider"))
        self.labelTitreCommentaires.setText(_translate("MainFrame", "Commentaires : "))

    def ajout(self):

        #Creation du groupe contenant le choix pour l'etat de service
        self.groupeBoutonEtatService = QButtonGroup()
        self.groupeBoutonEtatService.addButton(self.radioButtonEnService)
        self.groupeBoutonEtatService.addButton(self.radioButtonEnMaintenance)
        self.groupeBoutonEtatService.addButton(self.radioButtonAuRebus)

        #Creation du groupe contenant le choix pour l'etat de conservation
        self.groupeBoutonEtatConservation = QButtonGroup()
        self.groupeBoutonEtatConservation.addButton(self.radioButtonQuasiNeuf)
        self.groupeBoutonEtatConservation.addButton(self.radioButtonAcceptable)
        self.groupeBoutonEtatConservation.addButton(self.radioButtonEnFinDeVie)
        self.groupeBoutonEtatConservation.addButton(self.radioButtonDesuet)


        #Recuperation des differents elements utiles de la fenetre dans une liste
        self.listeWidgets = list()
        self.listeWidgets.append(self.comboBoxCategorie)
        self.listeWidgets.append(self.lineEditMarque)
        self.listeWidgets.append(self.lineEditModele)
        self.listeWidgets.append(self.lineEditNoDeSerie)
        self.listeWidgets.append(self.comboBoxSalle)
        self.listeWidgets.append(self.comboBoxCentreDeService)
        self.listeWidgets.append(self.dateEditDateDaquisition)
        self.listeWidgets.append(self.dateEditDateDuDernierEntretien)
        self.listeWidgets.append(self.comboBoxProvenance)
        self.listeWidgets.append(self.groupeBoutonEtatService)
        self.listeWidgets.append(self.groupeBoutonEtatConservation)
        self.listeWidgets.append(self.textEditCommentaires)

        #Creation de la variable equipement qui servira a l'enregistrement dans la BDD
        self.equipement = Equipement()
        self.equipement.ajoutListeMethodes()

        # Recuperation des differents attributs d''un equipement
        self.equipementManager = EquipementManager("DataBase_Equipement.json")
        self.listeDonnees = list()
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        self.listeCleDonnees = list(self._conf['champsAcceptes-Equipement'])

        #Recuperation des differents elements des listes deroulantes
        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeCentreService = list(self._conf['CentreService'])
        self.listeSalle = list(self._conf['Salle'])
        self.listeProvenance = list(self._conf['Provenance'])

        #Chargement des differentes listes deroulantes
        self.comboBoxCategorie.clear()
        self.comboBoxCategorie.addItems(self.listeCategorieEquipement)
        self.comboBoxSalle.clear()
        self.comboBoxSalle.addItems(self.listeSalle)
        self.comboBoxCentreDeService.clear()
        self.comboBoxCentreDeService.addItems(self.listeCentreService)
        self.comboBoxProvenance.clear()
        self.comboBoxProvenance.addItems(self.listeProvenance)

        #Connexion du bouton valider
        self.boutonValider.clicked.connect(self.verificationEquipement)

        #Creation des differents labels pour la verification
        self.categorieEquipementLabel = QLabel("Ici Categorie Equipement  ")
        self.marqueLabel = QLabel("Ici marque")
        self.modeleLabel = QLabel("Ici Modele ")
        self.numSerieLabel = QLabel("Ici No. de serie ")
        self.salleLabel = QLabel("Ici Label ")
        self.centreServiceLabel = QLabel("Ici Centre de service ")
        self.dateAcquisitionLabel = QLabel("Ici Date d'acquisition ")
        self.dateEntretienLabel = QLabel("Ici Date du dernier entretien")
        self.provenanceLabel = QLabel()
        self.etatServiceLabel = QLabel("Ici Etat de service ")
        self.etatConservationLabel = QLabel("Ici Etat de conservation ")
        self.commentaire = QLabel("Ici commentaires ")

        #Creation du liste pour manipuler plus facilement ces differents labels
        #--ATTETION-- L'ordre est donc important
        self.listeLabel = list()
        self.listeLabel.append(self.categorieEquipementLabel)
        self.listeLabel.append(self.marqueLabel)
        self.listeLabel.append(self.modeleLabel)
        self.listeLabel.append(self.numSerieLabel)
        self.listeLabel.append(self.salleLabel)
        self.listeLabel.append(self.centreServiceLabel)
        self.listeLabel.append(self.dateAcquisitionLabel)
        self.listeLabel.append(self.dateEntretienLabel)
        self.listeLabel.append(self.provenanceLabel)
        self.listeLabel.append(self.etatServiceLabel)
        self.listeLabel.append(self.etatConservationLabel)

        #Masquage des differents labels
        for label in self.listeLabel:
            self.layoutChamps.addWidget(label)
            label.hide()

        #Traitement de la partie commentaires
        self.listeLabel.append(self.commentaire)
        self.horizontalLayout_3.addWidget(self.commentaire)
        self.commentaire.hide()

        #Redefinition de la taille des champs d'entree de date
        self.dateEditDateDaquisition.setMinimumWidth(200)
        self.dateEditDateDuDernierEntretien.setMinimumWidth(200)

        #Creation des boutons de modification et d'enregistrement
        self.boutonModifier = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonModifier.setFont(font)
        self.boutonModifier.setObjectName("boutonModifier")
        self.horizontalLayout_8.addWidget(self.boutonModifier)
        self.boutonModifier.setText("Modifier")

        self.boutonEnregister = QtWidgets.QPushButton()
        self.boutonEnregister.setFont(font)
        self.boutonEnregister.setObjectName("boutonEnregister")
        self.horizontalLayout_8.addWidget(self.boutonEnregister)
        self.boutonEnregister.setText("Enregistrer")

        self.boutonEnregister.hide()
        self.boutonModifier.hide()

        self.boutonEnregister.clicked.connect(self.sauvegarderEquipement)
        self.boutonModifier.clicked.connect(self.modifierEquipement)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)

        #Selection des choix par defaut pour les radio boutons
        self.radioButtonEnService.setChecked(True)
        self.radioButtonQuasiNeuf.setChecked(True)
        #Mise en place de la modification des champs deroulants
        self.comboBoxSalle.setEditable(True)
        self.comboBoxProvenance.setEditable(True)
        self.comboBoxCentreDeService.setEditable(True)

    def obtenirEtatDeService(self, groupeBoutton):
        """Methode permettant d'obtenir le choix selectionne parmi le groupe
        de radio bouton"""
        bouton = self.groupeBoutonEtatService.checkedButton()
        self.etatDeService = bouton.text()

    def donnees(self):
        """Methode permettant la recuperation des donnees dans les differents widgets
        On parcours la liste des widgets et on recupere les differentes informations utiles
        Les informations sont recuperees de facon specifique selon le type du widget"""
        self.listeDonnees.clear()
        for widget in self.listeWidgets:
                # self.stockage.dictionnaire
                if type(widget) is QLineEdit:
                        self.listeDonnees.append(widget.text())
                elif type(widget) is QDateEdit:
                        self.listeDonnees.append(widget.date().toPyDate())
                        if isinstance(widget.date().toPyDate(), datetime.date):
                            print("format date correct")
                        else:
                            print("probleme avec format date")
                elif type(widget) is QComboBox:
                        self.listeDonnees.append(widget.currentText())
                elif type(widget) is QButtonGroup:
                        bouton = widget.checkedButton()
                        etatDeService = bouton.text()
                        self.listeDonnees.append(etatDeService)
                else:
                        self.listeDonnees.append(widget.toPlainText())

    def sauvegarderEquipement(self):
        """Methode permettant l'enregristrement de l'equipement dans la BDD"""

        # self.donnees()
        i = 0
        for donnees in self.listeDonnees:
            self.equipement.listeMethodes[i](donnees)
            i += 1
        self.equipementManager = EquipementManager('DataBase_Equipement.json')
        self.equipementManager.AjouterEquipement(self.equipement.dictionnaire)

    def verificationEquipement(self):
        """Methode affichant le recapitulatif de l'equipement"""
        self.donnees()
        indice = 0
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        for text in self.listeDonnees:
            if type(self.listeWidgets[indice]) is QButtonGroup:
                for radioBouton in self.listeWidgets[indice].buttons():
                    if not radioBouton.isChecked():
                        radioBouton.hide()
            else:
                self.listeLabel[indice].setFont(font)
                self.listeLabel[indice].setText(str(text))
                self.listeLabel[indice].show()
                self.listeWidgets[indice].hide()
            indice += 1
        self.labelId.setText(str(self.equipementManager._ObtenirProchainID()))
        self.boutonEnregister.show()
        self.boutonModifier.show()
        self.boutonValider.hide()

    def modifierEquipement(self):
        """Action lors de l'appuie sur le bouton modifier
        On repasse sur l'ajout d'un equipement avec les champs modifiables"""
        indice = 0
        for text in self.listeDonnees:
            if type(self.listeWidgets[indice]) is QButtonGroup:
                for radioBouton in self.listeWidgets[indice].buttons():
                        radioBouton.show()
            else:
                self.listeLabel[indice].hide()
                self.listeWidgets[indice].show()
            indice += 1
        self.labelId.setText("")
        self.boutonEnregister.hide()
        self.boutonValider.show()
        self.boutonModifier.hide()

    def remplirEquipement(self):
        """Methode permettant le remplissage des differents labels
         Utilisation des donnees entrees par l'utilisateur pour les labels
         """
        equipement = self.equipementRecherche
        indice = 0
        for widget in self.listeWidgets:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                widget.setText(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QDateEdit:
                widget.setDate(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QComboBox:
                widget.setCurrentText(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QButtonGroup:
                for radioBouton in widget.buttons():
                    if radioBouton.text() == equipement[self.listeCleDonnees[indice]]:
                        radioBouton.setChecked(True)
            else:
                widget.setText(equipement[self.listeCleDonnees[indice]])
            indice += 1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ajoutEquipement = QtWidgets.QWidget()
    ajoutEquipementUI = AjoutEquipementUI()
    ajoutEquipementUI.setupUi(ajoutEquipement)
    ajoutEquipement.show()
    sys.exit(app.exec_())

