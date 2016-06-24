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
        self.LabelCategorie = QtWidgets.QLabel(PC2)
        self.LabelCategorie.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelCategorie.setFont(font)
        self.LabelCategorie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelCategorie.setObjectName("LabelCategorie")
        self.verticalLayout_4.addWidget(self.LabelCategorie)
        self.boutonCategorie = QtWidgets.QComboBox(PC2)
        self.boutonCategorie.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.boutonCategorie.setFont(font)
        self.boutonCategorie.setObjectName("boutonCategorie")
        self.verticalLayout_4.addWidget(self.boutonCategorie)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.LabelAvant = QtWidgets.QLabel(PC2)
        self.LabelAvant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelAvant.setFont(font)
        self.LabelAvant.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LabelAvant.setObjectName("LabelAvant")
        self.verticalLayout_7.addWidget(self.LabelAvant)
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
        self.LabelApres = QtWidgets.QLabel(PC2)
        self.LabelApres.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelApres.setFont(font)
        self.LabelApres.setObjectName("LabelApres")
        self.verticalLayout_5.addWidget(self.LabelApres)
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
        self.boutonAvant = QtWidgets.QComboBox(PC2)
        self.boutonAvant.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.boutonAvant.setFont(font)
        self.boutonAvant.setObjectName("boutonAvant")
        self.verticalLayout_8.addWidget(self.boutonAvant)
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
        self.boutonCdS = QtWidgets.QComboBox(PC2)
        self.boutonCdS.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.boutonCdS.setFont(font)
        self.boutonCdS.setObjectName("boutonCdS")
        self.verticalLayout_2.addWidget(self.boutonCdS)
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
        self.LabelCategorie.setText(_translate("PC2", "Catégorie d\'équipement"))
        self.LabelAvant.setText(_translate("PC2", "Avant le"))
        self.LabelApres.setText(_translate("PC2", "Après le"))
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

        self.ajoutRechercheBonDeTravail()

    def ajoutRechercheBonDeTravail(self):
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

        #Mise a jour des differentes listes deroulantes
        self.boutonCategorie.clear()
        self.boutonCategorie.addItem("")
        self.boutonCategorie.addItems(self.listeCategorieEquipement)
        self.boutonAvant.clear()
        self.boutonAvant.addItem("")
        self.boutonAvant.addItems(self.listeEtatService)
        self.boutonCdS.clear()
        self.boutonCdS.addItem("")
        self.boutonCdS.addItems(self.listeCentreService)


        fichierConf.close()

        #Creation des differents colonnes pour le tableau de resultat
        self.listeCleDonnees = list(["ID", "CategorieEquipement", "Modele", "CentreService", "EtatBDT", "Date", "ID-BDT", "DescriptionSituation"])

        self.tableResultats.setColumnCount(len(self.listeCleDonnees))
        self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.resizeColumnsToContents()

        self.dictionnaireRecherche = dict()
        self.dictionnaireRechercheBDT = dict()

        #Connexion des differentes recherches pour la mise a jour automatique
        self.boutonCategorie.currentTextChanged.connect(self.rechercheCategorieEquipement)
        self.boutonAvant.currentTextChanged.connect(self.rechercheEtatDeService)
        self.boutonCdS.currentTextChanged.connect(self.rechercheCentreService)
        # self.comboBoxSalle.currentTextChanged.connect(self.rechercheSalle)
        # self.comboBoxProvenance.currentTextChanged.connect(self.rechercheProvenance)
        self.calendrierAvant.dateChanged.connect(self.rechercheDateAvant)
        self.lineEdit.returnPressed.connect(self.rechercheDescriptionSituation)
        self.calendrierApres.dateChanged.connect(self.rechercheDateApres)

    def rechercheDateAvant(self):
        '''
            Recuperation des bons de travails qui sont anterieurs a la date indique
            :param: None
            :return:
        '''
        self.dictionnaireRechercheBDT["AvantLe"] = self.calendrierAvant.date().toPyDate()
        self.remplirTableau()

    def rechercheDateApres(self):
        '''
            Recuperation des bons de travails qui sont posterieurs a la date indique
            :param: None
            :return:
        '''
        self.dictionnaireRechercheBDT["ApresLe"] = self.calendrierApres.date().toPyDate()
        self.remplirTableau()

    def rechercheDescriptionSituation(self):
        '''
            Recuperation des bons de travails correspondant a la description
            :param: None
            :return:
        '''
        if (self.lineEdit.text() != ""):
            self.dictionnaireRechercheBDT["DescriptionSituation"] = self.lineEdit.text()
        self.remplirTableau()

    def rechercheCategorieEquipement(self):
        '''
            Recuperation des bons de travails associe a une categorie d'equipement
            :param: None
            :return:
        '''
        if (self.boutonCategorie.currentText() != ""):
            self.dictionnaireRecherche["CategorieEquipement"] = self.boutonCategorie.currentText()

        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.remplirTableau()


    def rechercheEtatDeService(self):
        '''
            Recuperation des bons de travails associe a un etat de service
            :param: None
            :return:
        '''
        if (self.boutonAvant.currentText() != ""):
            self.dictionnaireRecherche["EtatService"] = self.boutonAvant.currentText()

        else:
            self.dictionnaireRecherche.pop("EtatService")
        self.remplirTableau()

    def rechercheCentreService(self):
        '''
            Recuperation des bons de travails associe a un centre de service
            :param: None
            :return:
        '''
        if (self.boutonCdS.currentText() != ""):
            self.dictionnaireRecherche["CentreService"] = self.boutonCdS.currentText()

        else:
            self.dictionnaireRecherche.pop("CentreService")
        self.remplirTableau()

    def remplirTableau(self):
        '''
            Remplissage du tableau de resultat avec les eventuels bons de travail trouves
            :param: None
            :return:
        '''
        if (any(self.dictionnaireRecherche)):
            liste = self.equipementManager.RechercherEquipement(self.dictionnaireRecherche)
            listeBonTravail = list()
            listeDonnees = list()
            for element in liste:
                #Recherche a partir des attributs des equipements
                listeBDT = self.bonDeTravailManager.RechercherBonTravail({"ID-EQ": element["ID"]})
                for bonTravail in listeBDT:
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
            #Recherche parmi les coordonnes
            if (any(self.dictionnaireRechercheBDT)):
                liste = self.bonDeTravailManager.RechercherBonTravail(self.dictionnaireRechercheBDT)
                listeDonnees = list()
                dictionnaireEquipementAssocie = dict()
                indice = 0
                if(len(liste) > 0):
                    for bdt in liste :
                            print(bdt["ID-EQ"])
                            if bdt["ID-EQ"] in dictionnaireEquipementAssocie:
                                equipement = dictionnaireEquipementAssocie["ID-EQ"]
                            else:
                                equipement = self.equipementManager.RechercherEquipement({"ID": bdt["ID-EQ"]})[0]
                                dictionnaireEquipementAssocie["ID-EQ"] = equipement
                            print(equipement)
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
                    print("Aucun resultat")
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