# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rbdt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager


class RechercheBonDeTravailUI(object):
    def setupUi(self, PC2):
        PC2.setObjectName("PC2")
        PC2.resize(1388, 1078)
        PC2.setMaximumSize(QtCore.QSize(2000, 2000))
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PC2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LabelTitre = QtWidgets.QLabel(PC2)
        self.LabelTitre.setMaximumSize(QtCore.QSize(2000, 2000))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTitre.setFont(font)
        self.LabelTitre.setObjectName("LabelTitre")
        self.verticalLayout_3.addWidget(self.LabelTitre)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Labelcategorie = QtWidgets.QLabel(PC2)
        self.Labelcategorie.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labelcategorie.setFont(font)
        self.Labelcategorie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Labelcategorie.setObjectName("Labelcategorie")
        self.verticalLayout_4.addWidget(self.Labelcategorie)
        self.buttonCategorie = QtWidgets.QComboBox(PC2)
        self.buttonCategorie.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonCategorie.setFont(font)
        self.buttonCategorie.setObjectName("buttonCategorie")
        self.verticalLayout_4.addWidget(self.buttonCategorie)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Labelavant = QtWidgets.QLabel(PC2)
        self.Labelavant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labelavant.setFont(font)
        self.Labelavant.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Labelavant.setObjectName("Labelavant")
        self.verticalLayout_7.addWidget(self.Labelavant)
        self.calendrierAvant = QtWidgets.QDateEdit(PC2)
        self.calendrierAvant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendrierAvant.setFont(font)
        self.calendrierAvant.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierAvant.setCalendarPopup(True)
        self.calendrierAvant.setObjectName("calendrierAvant")
        self.verticalLayout_7.addWidget(self.calendrierAvant)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Labelapres = QtWidgets.QLabel(PC2)
        self.Labelapres.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labelapres.setFont(font)
        self.Labelapres.setObjectName("Labelapres")
        self.verticalLayout_5.addWidget(self.Labelapres)
        self.calendrierApres = QtWidgets.QDateEdit(PC2)
        self.calendrierApres.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendrierApres.setFont(font)
        self.calendrierApres.setDate(QtCore.QDate(2016, 1, 1))
        self.calendrierApres.setCalendarPopup(True)
        self.calendrierApres.setObjectName("calendrierApres")
        self.verticalLayout_5.addWidget(self.calendrierApres)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Labeletat = QtWidgets.QLabel(PC2)
        self.Labeletat.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labeletat.setFont(font)
        self.Labeletat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Labeletat.setObjectName("Labeletat")
        self.verticalLayout_8.addWidget(self.Labeletat)
        self.buttonAvant = QtWidgets.QComboBox(PC2)
        self.buttonAvant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonAvant.setFont(font)
        self.buttonAvant.setObjectName("buttonAvant")
        self.verticalLayout_8.addWidget(self.buttonAvant)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LabelCdS = QtWidgets.QLabel(PC2)
        self.LabelCdS.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelCdS.setFont(font)
        self.LabelCdS.setObjectName("LabelCdS")
        self.verticalLayout_2.addWidget(self.LabelCdS)
        self.buttonCdS = QtWidgets.QComboBox(PC2)
        self.buttonCdS.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonCdS.setFont(font)
        self.buttonCdS.setObjectName("buttonCdS")
        self.verticalLayout_2.addWidget(self.buttonCdS)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Labeldescription = QtWidgets.QLabel(PC2)
        self.Labeldescription.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Labeldescription.setFont(font)
        self.Labeldescription.setObjectName("Labeldescription")
        self.verticalLayout.addWidget(self.Labeldescription)
        self.lineEdit = QtWidgets.QLineEdit(PC2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableResultats = QtWidgets.QTableWidget(PC2)
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
        self.verticalLayout_3.addLayout(self.verticalLayout_11)
        self.LabelTitre.raise_()

        self.retranslateUi(PC2)
        QtCore.QMetaObject.connectSlotsByName(PC2)

    def retranslateUi(self, PC2):
        _translate = QtCore.QCoreApplication.translate
        PC2.setWindowTitle(_translate("PC2", "PC2"))
        self.LabelTitre.setText(_translate("PC2", "Assistant de Recherche-Bon de travail"))
        self.Labelcategorie.setText(_translate("PC2", "Catégorie d\'équipement"))
        self.Labelavant.setText(_translate("PC2", "Avant le"))
        self.Labelapres.setText(_translate("PC2", "Après le"))
        self.calendrierApres.setDisplayFormat(_translate("PC2", "dd-MM-yyyy"))
        self.Labeletat.setText(_translate("PC2", "État"))
        self.LabelCdS.setText(_translate("PC2", "Centre de service"))
        self.Labeldescription.setText(_translate("PC2", "Description de la situation"))
        self.tableResultats.setSortingEnabled(False)
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

        # Recuperation des differents attributs
        self.equipementManager = EquipementManager("DataBase_Equipement.json")
        self.bonDeTravailManager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')
        # self.listeCleDonnees = list()
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        # self.listeCleDonnees = list(self._conf['champsAcceptes-Equipement'])
        # print("liste des cles : ", self.listeCleDonnees)

        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeCentreService = list(self._conf['CentreService'])
        self.listeEtatService = list(self._conf['EtatService'])
        # self.listeProvenance = list(self._conf['Provenance'])

        self.buttonCategorie.clear()
        self.buttonCategorie.addItem("")
        self.buttonCategorie.addItems(self.listeCategorieEquipement)
        self.buttonAvant.clear()
        self.buttonAvant.addItem("")
        self.buttonAvant.addItems(self.listeEtatService)
        self.buttonCdS.clear()
        self.buttonCdS.addItem("")
        self.buttonCdS.addItems(self.listeCentreService)


        fichierConf.close()

        self.listeCleDonnees = list(["ID", "CategorieEquipement", "Modele", "CentreService", "EtatBDT", "Date", "ID-BDT", "DescriptionSituation"])

        self.tableResultats.setColumnCount(len(self.listeCleDonnees))
        self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.resizeColumnsToContents()

        self.dictionnaireRecherche = dict()
        self.dictionnaireRechercheBDT = dict()

        self.buttonCategorie.currentTextChanged.connect(self.rechercheCategorieEquipement)
        self.buttonAvant.currentTextChanged.connect(self.rechercheEtatDeService)
        self.buttonCdS.currentTextChanged.connect(self.rechercheCentreService)
        # self.comboBoxSalle.currentTextChanged.connect(self.rechercheSalle)
        # self.comboBoxProvenance.currentTextChanged.connect(self.rechercheProvenance)
        self.calendrierAvant.dateChanged.connect(self.rechercheDateAvant)
        self.lineEdit.returnPressed.connect(self.rechercheDescriptionSituation)


    def rechercheDateAvant(self):
        self.dictionnaireRechercheBDT["AvantLe"] = self.calendrierAvant.date().toPyDate()
        self.remplirTableau()

    def rechercheDateApres(self):
        self.dictionnaireRechercheBDT["ApresLe"] = self.calendrierApres.date().toPyDate()
        self.remplirTableau()

    def rechercheDescriptionSituation(self):
        if (self.lineEdit.text() is not ""):
            print(self.lineEdit.text())
            self.dictionnaireRechercheBDT["DescriptionSituation"] = self.lineEdit.text()


    def rechercheCategorieEquipement(self):
        """Methode permettant la recherche par rapport au champ de recherche
        de categorie d'equipement"""
        if (self.buttonCategorie.currentText() is not ""):
            self.dictionnaireRecherche["CategorieEquipement"] = self.buttonCategorie.currentText()

        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.remplirTableau()


    def rechercheEtatDeService(self):
        if (self.buttonAvant.currentText() is not ""):
            self.dictionnaireRecherche["EtatService"] = self.buttonAvant.currentText()

        else:
            self.dictionnaireRecherche.pop("EtatService")
        self.remplirTableau()

    def rechercheCentreService(self):
        if (self.buttonCdS.currentText() is not ""):
            self.dictionnaireRecherche["CentreService"] = self.buttonCdS.currentText()

        else:
            self.dictionnaireRecherche.pop("CentreService")
        self.remplirTableau()

    def remplirTableau(self):
        if (any(self.dictionnaireRecherche)):
            print(self.equipementManager.RechercherEquipement(self.dictionnaireRecherche))
            liste = self.equipementManager.RechercherEquipement(self.dictionnaireRecherche)
            listeBonTravail = list()
            listeDonnees = list()
            for element in liste:
                for bonTravail in self.bonDeTravailManager.RechercherBonTravail({"ID-EQ": element["ID"]}):
                    #Recuperation des bons de travail associe a un equipement
                    listeBonTravail.append(bonTravail)
                    dictDonnees = dict()
                    dictDonnees["ID"] = element["ID"]
                    dictDonnees["CategorieEquipement"] = element["CategorieEquipement"]
                    dictDonnees["Modele"] = element["Modele"]
                    dictDonnees["CentreService"] = element["CentreService"]
                    dictDonnees["EtatBDT"] = bonTravail["EtatBDT"]
                    dictDonnees["Date"] = bonTravail["Date"]
                    dictDonnees["ID-BDT"] = bonTravail["ID-BDT"]
                    dictDonnees["DescriptionSituation"] = bonTravail["DescriptionSituation"]
                    listeDonnees.append(dictDonnees)
            self.tableResultats.setRowCount(len(listeDonnees))
            for i, dictionnaire in enumerate(listeDonnees):
                # Creation des QTableWidgetItem
                colonne = 0
                for cle in self.listeCleDonnees:
                    self.tableResultats.setItem(i, colonne, QTableWidgetItem(str(dictionnaire[cle])))
                    colonne += 1

        else:
            if (any(self.dictionnaireRechercheBDT)):
                liste = self.bonDeTravailManager.RechercherBonTravail(self.dictionnaireRechercheBDT)
                print(liste)
                listeDonnees = list()
                for bdt in liste :
                        equipement = self.equipementManager.RechercherEquipement({"ID": bdt["ID-EQ"]})[0]
                        dictDonnees = dict()
                        dictDonnees["ID"] = equipement["ID"]
                        dictDonnees["CategorieEquipement"] = equipement["CategorieEquipement"]
                        dictDonnees["Modele"] = equipement["Modele"]
                        dictDonnees["CentreService"] = equipement["CentreService"]
                        dictDonnees["EtatBDT"] = bdt["EtatBDT"]
                        dictDonnees["Date"] = bdt["Date"]
                        dictDonnees["ID-BDT"] = bdt["ID-BDT"]
                        dictDonnees["DescriptionSituation"] = bdt["DescriptionSituation"]
                        listeDonnees.append(dictDonnees)
                self.tableResultats.setRowCount(len(listeDonnees))
                for i, dictionnaire in enumerate(listeDonnees):
                    # Creation des QTableWidgetItem
                    colonne = 0
                    for cle in self.listeCleDonnees:
                        self.tableResultats.setItem(i, colonne, QTableWidgetItem(str(dictionnaire[cle])))
                        colonne += 1
            else:
                print("dictionnaire de recherche vide")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rechercheBonDeTravail = QtWidgets.QWidget()
    rechercheBonDeTravailUI = RechercheBonDeTravailUI()
    rechercheBonDeTravailUI.setupUi(rechercheBonDeTravail)
    rechercheBonDeTravail.show()
    sys.exit(app.exec_())