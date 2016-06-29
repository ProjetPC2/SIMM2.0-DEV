# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rbdt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.RechercheBonDeTravailUI import Ui_RechercheBonDeTravail


class RechercheBonDeTravail(Ui_RechercheBonDeTravail):
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutRechercheBonDeTravail()

    def ajoutRechercheBonDeTravail(self):
        # Recuperation des differents attributs
        self.equipementManager = EquipementManager("DataBase_Equipement.json", 'DataBase_BDT.json')
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
        self.comboBoxCategorieEquipement.clear()
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItems(self.listeCategorieEquipement)
        self.comboBoxEtat.clear()
        self.comboBoxEtat.addItem("")
        self.comboBoxEtat.addItems(self.listeEtatService)
        self.comboBoxCentreService.clear()
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItems(self.listeCentreService)


        fichierConf.close()

        #Creation des differents colonnes pour le tableau de resultat
        self.listeCleDonnees = list(["ID-EQ", "ID-BDT", "CategorieEquipement", "Modele", "CentreService", "EtatBDT", "Date", "DescriptionSituation"])

        self.tableResultats.setColumnCount(len(self.listeCleDonnees))
        self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.resizeColumnsToContents()
        self.tableResultats.setRowCount(0)
        # self.tableResultats.setColumnCount(0)

        self.dictionnaireRecherche = dict()
        self.dictionnaireRechercheBDT = dict()

        #Connexion des differentes recherches pour la mise a jour automatique
        self.comboBoxCategorieEquipement.currentTextChanged.connect(self.rechercheCategorieEquipement)
        self.comboBoxEtat.currentTextChanged.connect(self.rechercheEtatDeService)
        self.comboBoxCentreService.currentTextChanged.connect(self.rechercheCentreService)
        # self.comboBoxSalle.currentTextChanged.connect(self.rechercheSalle)
        # self.comboBoxProvenance.currentTextChanged.connect(self.rechercheProvenance)
        self.calendrierAvant.dateChanged.connect(self.rechercheDateAvant)
        self.lineEditDescriptionSituation.returnPressed.connect(self.rechercheDescriptionSituation)
        self.calendrierApres.dateChanged.connect(self.rechercheDateApres)

        self.tableResultats.horizontalHeader().sectionClicked.connect(self.trier)
        self.colonneClique = None
        self.nombreClique = 0
        # Empeche la modification de la table
        self.tableResultats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers);
        self.tableResultats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableResultats.cellDoubleClicked.connect(self.choisirBonDeTravail)
        self.listeResultat = list()
        self.modificationEquipement = None
        self.bonDeTravailSelectionne = None

    def choisirBonDeTravail(self, ligne, colonne):
        #TODO A remanier
        print("ligne", ligne)
        print("colonne", colonne)
        print(self.tableResultats.item(ligne, 0).data(0))
        self.bonDeTravailSelectionne = dict()
        indice = 0
        for cle in self.listeCleDonnees:
            if (cle == "ID-EQ" or cle == "ID-BDT"):
                self.bonDeTravailSelectionne[cle] = int(self.tableResultats.item(ligne, indice).data(0))
            elif cle == "Date" :
                self.bonDeTravailSelectionne[cle] = datetime.datetime.strptime(
                    self.tableResultats.item(ligne, indice).data(0), '%Y-%m-%d')
            elif cle == "TempsEstime":
                self.bonDeTravailSelectionne[cle] = datetime.time.strptime(
                    self.tableResultats.item(ligne, indice).data(0), '%H:%M')
            else:
                self.bonDeTravailSelectionne[cle] = self.tableResultats.item(ligne, indice).data(0)
            indice += 1
        # self.modificationEquipement = QtWidgets.QWidget()
        # self.modificationEquipementUI = ModificationEquipementUI()
        # self.modificationEquipementUI.setupUi(self.modificationEquipement, equipement)
        # # self.modificationEquipement.setStyleSheet("background: white;")
        print(self.bonDeTravailSelectionne)
        # self.hide()

    def trier(self, numeroColonne):
        """Methode permettant le tri des colonnes lors du clique sur l'une d'entre elle
        Un clic fait un tri croisssant
        Un second clic fera un tri decroissant"""
        print(numeroColonne)
        if numeroColonne == self.colonneClique:
            if self.nombreClique % 2 == 0:
                self.tableResultats.sortByColumn(numeroColonne, Qt.AscendingOrder)
            else:
                self.tableResultats.sortByColumn(numeroColonne, Qt.DescendingOrder)
            self.nombreClique += 1
        else:
            self.nombreClique = 1
            self.tableResultats.sortByColumn(numeroColonne, Qt.AscendingOrder)
            self.colonneClique = numeroColonne

    def rechercheCategorieEquipement(self):
        """Methode permettant la recherche par rapport au champ de recherche
        de categorie d'equipement"""
        if (self.comboBoxCategorieEquipement.currentText() != ""):
            self.dictionnaireRecherche["CategorieEquipement"] = self.comboBoxCategorieEquipement.currentText()

        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.remplirTableau()

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
        if (self.lineEditDescriptionSituation.text() != ""):
            self.dictionnaireRechercheBDT["DescriptionSituation"] = self.lineEditDescriptionSituation.text()
        self.remplirTableau()

    def rechercheCategorieEquipement(self):
        '''
            Recuperation des bons de travails associe a une categorie d'equipement
            :param: None
            :return:
        '''
        if (self.comboBoxCategorieEquipement.currentText() != ""):
            self.dictionnaireRecherche["CategorieEquipement"] = self.comboBoxCategorieEquipement.currentText()

        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.remplirTableau()


    def rechercheEtatDeService(self):
        '''
            Recuperation des bons de travails associe a un etat de service
            :param: None
            :return:
        '''
        if (self.comboBoxEtat.currentText() != ""):
            self.dictionnaireRecherche["EtatService"] = self.comboBoxEtat.currentText()

        else:
            self.dictionnaireRecherche.pop("EtatService")
        self.remplirTableau()

    def rechercheCentreService(self):
        '''
            Recuperation des bons de travails associe a un centre de service
            :param: None
            :return:
        '''
        if (self.comboBoxCentreService.currentText() != ""):
            self.dictionnaireRecherche["CentreService"] = self.comboBoxCentreService.currentText()

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
                    dictDonnees["ID-EQ"] = element["ID"]
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
                print(liste)
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
                            dictDonnees["ID-EQ"] = equipement["ID"]
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
    rechercheBonDeTravailUI = RechercheBonDeTravail(rechercheBonDeTravail)
    rechercheBonDeTravail.show()
    sys.exit(app.exec_())