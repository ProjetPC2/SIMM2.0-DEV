"""
Dans cette exemple vous pourrez voir comment :
-Creer une fenetre avec differents composants
-Utiliser plusieurs classes pour faire une fenetre
-Relier des signaux a des actions
-Mettre a jour une fentre dynamiquement
-exemple d'utilisation des layouts pour gerer le placemenet
"""

import sys
from PyQt5 import QtWidgets

import yaml
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.StatistiqueUI import Ui_Statistique


class Statistique(Ui_Statistique):
    """La classe Statistique est la classe qui est va servir a creer la fenetre principal
    Cette classe va contenir les attributs suivants :
    -Un titre
    -Une statusBar
    -un formulaire
    -un formulaire rempli
    -des options
    -un attribut de stockage
    -une liste temporaire pour le stockage des informations"""
    def __init__(self, widget):
        self.setupUi(widget)

        # # Création des differents éléments
        # self.titre = QLabel("Statistique")
        # self.titre.setFont((QFont('SansSerif', 24)))
        # self.titre.setAlignment(Qt.AlignCenter)
        #
        #    # Création des Boutons
        # self.nombreEquipement = 10
        self.ajoutStatistique()
    def ajoutStatistique(self):
        self.equipementManager = EquipementManager("DataBase_Equipement.json", 'DataBase_BDT.json')

        #Mise en place du layout principal

        self.nombreQuasiNeuf = 0
        self.nombreAcceptable = 0
        self.nombreEnFinVie = 0
        self.nombreDesuet = 0
        self.enService = 0
        self.enMaintenance = 0
        self.auRebus = 0

        self.miseAJourDonnees()
        self.textBrowserNombreTotalEquipements.setText(str(self.nombreEquipement))
        self.textBrowserEnMaintenance.setText(str(self.enMaintenance))
        self.textBrowserEnService.setText(str(self.enService))
        self.textBrowserAuRebus.setText(str(self.auRebus))

        self.textBrowserQuasiNeuf.setText(str(self.nombreQuasiNeuf))
        self.textBrowserAcceptable.setText(str(self.nombreAcceptable))
        self.textBrowserEnFinDeVie.setText(str(self.nombreEnFinVie))
        self.textBrowserDesuet.setText(str(self.nombreDesuet))

        self.nombreEquipementProvenance = 0
        #
        # self.tableResumeInventaire.resizeColumnToContents(0)
        # self.tableResumeInventaire.resizeRowsToContents()

        # On fait en sorte que la table prend la largeur de la fenetre
        # self.table.horizontalHeader().setStretchLastSection(True)


        #Mise en place de la forme de la fenetre
        # self.setGeometry(200, 100, 200, 1000)

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
        self.listeProvenance = list(self._conf['Provenance'])
        # self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        # self.listeEtatService = list(self._conf['EtatService'])
        self.listeCentreService = list(self._conf['CentreService'])
        # self.listeSalle = list(self._conf['Salle'])
        print(self.listeProvenance)
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItem("Tous")
        self.comboBoxProvenance.addItems(self.listeProvenance)
        self.comboBoxCentreService.clear()
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItem("Tous")
        self.comboBoxCentreService.addItems(self.listeCentreService)

        self.tableResumeInventaire.clear()
        self.tableResumeInventaire.setHorizontalHeaderLabels(["Categorie equipement", "Quantite"])
        self.tableResumeInventaire.setWordWrap(True)
        self.tableResumeInventaire.resizeColumnToContents(0)
        self.tableResumeInventaire.resizeRowsToContents()
        self.tableResumeInventaire.horizontalHeader().setStretchLastSection(True)
        self.tableResumeInventaire.setRowCount(0)

        self.statsProvenance = self.equipementManager._statsNbEquipementProvenance()
        self.statsCategorie = self.equipementManager._statsNbEquipementCentreServiceCategorie()
        print(self.statsCategorie)
        self.comboBoxProvenance.currentTextChanged.connect(self.affichageProvenance)
        self.comboBoxCentreService.currentTextChanged.connect(self.affichageCenreService)
        self.tableResumeInventaire.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers);
        self.tableResumeInventaire.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.colonneClique = None
        self.nombreClique = 0
        self.tableResumeInventaire.horizontalHeader().sectionClicked.connect(self.trier)


    def miseAJourDonnees(self):
        self.nombreEquipement = self.equipementManager._statsNbTotalEquipement()
        dictionnaire = dict(self.equipementManager._statsNbEquipementEtatService())
        self.enService = dictionnaire["En service"]
        self.auRebus = dictionnaire["Au rebus"]
        self.enMaintenance = dictionnaire["En maintenance"]
        dictionnaire = dict(self.equipementManager._statsNbEquipementEtatConservation())
        self.nombreQuasiNeuf = dictionnaire["Quasi neuf"]
        self.nombreEnFinVie = dictionnaire["En fin de vie"]
        self.nombreAcceptable = dictionnaire["Acceptable"]
        self.nombreDesuet = dictionnaire["D\xE9suet"]

        print(self.nombreEquipement)

    def trier(self, numeroColonne):
        """Methode permettant le tri des colonnes lors du clique sur l'une d'entre elle
        Un clic fait un tri croisssant
        Un second clic fera un tri decroissant"""
        print(numeroColonne)
        if numeroColonne == self.colonneClique:
            if self.nombreClique % 2 == 0:
                self.tableResumeInventaire.sortByColumn(numeroColonne, Qt.AscendingOrder)
            else:
                self.tableResumeInventaire.sortByColumn(numeroColonne, Qt.DescendingOrder)
            self.nombreClique += 1
        else:
            self.nombreClique = 1
            self.tableResumeInventaire.sortByColumn(numeroColonne, Qt.AscendingOrder)
            self.colonneClique = numeroColonne

    def affichageProvenance(self):
        if(self.comboBoxProvenance.currentText() is not ""):
            if(self.comboBoxProvenance.currentText() == "Tous"):
                total = 0
                for value in self.statsProvenance.values():
                    total += value
                self.nombreEquipementProvenance = total
            else:
                self.nombreEquipementProvenance = self.statsProvenance[self.comboBoxProvenance.currentText()]
        else:
            self.nombreEquipementProvenance = 0
        self.textBrowserEquipementProvenance.setText(str(self.nombreEquipementProvenance))

    def affichageCenreService(self):
        # if(self.comboBoxCentreService.currentText() == ""):
        #     dictionnaireResultat = dict()
        #     for dictionnaire in self.statsCategorie.values():
        #         for cle, valeur in dictionnaire.items():
        #             if cle in dictionnaireResultat:
        #                 dictionnaireResultat[cle] += valeur
        #             else:
        #                 dictionnaireResultat[cle] = valeur
        #     self.table.setRowCount(len(dictionnaireResultat))
        #     ligne = 0
        #     for cle,valeur in dictionnaireResultat.items():
        #         self.table.setItem(ligne, 0, QTableWidgetItem(cle))
        #         self.table.setItem(ligne, 1, QTableWidgetItem(valeur))
        #         ligne += 1
        # else:
        #     ligne = 0
        #     self.table.setRowCount(len(self.statsCategorie[self.comboBoxCentreService.currentText()]))
        #     for cle, valeur in self.statsCategorie[self.comboBoxCentreService.currentText()].items():
        #         self.table.setItem(ligne, 0, QTableWidgetItem(cle))
        #         self.table.setItem(ligne, 1, QTableWidgetItem(valeur))
        #         ligne += 1
        if (self.comboBoxCentreService.currentText() != ""):
            dictionnaireResultat = dict()
            if self.comboBoxCentreService.currentText() == "Tous":
                for dictionnaire in self.statsCategorie.values():
                    for cle, valeur in dictionnaire.items():
                                if cle in dictionnaireResultat:
                                    dictionnaireResultat[cle] += valeur
                                else:
                                    dictionnaireResultat[cle] = valeur
            else:
                if self.comboBoxCentreService.currentText() in self.statsCategorie:
                    dictionnaireResultat = self.statsCategorie[self.comboBoxCentreService.currentText()]

            self.tableResumeInventaire.setRowCount(len(dictionnaireResultat))
            if (any(dictionnaireResultat)):
                ligne = 0
                for cle, valeur in dictionnaireResultat.items():
                    self.tableResumeInventaire.setItem(ligne, 0, QTableWidgetItem(cle))
                    self.tableResumeInventaire.item(ligne, 0).setTextAlignment(QtCore.Qt.AlignHCenter)
                    self.tableResumeInventaire.setItem(ligne, 1, QTableWidgetItem(str(valeur)))
                    self.tableResumeInventaire.item(ligne, 1).setTextAlignment(QtCore.Qt.AlignHCenter)

                    ligne += 1

    def miseAJourStats(self):
        self.statsProvenance = self.equipementManager._statsNbEquipementProvenance()
        self.statsCategorie = self.equipementManager._statsNbEquipementCentreServiceCategorie()
        self.miseAJourDonnees()

if __name__ == "__main__": #Si le fichier est lancé tout seul

    import sys

    app = QtWidgets.QApplication(sys.argv)
    statistique = QtWidgets.QWidget()
    statistiqueUI = Statistique(statistique)
    statistique.show()
    sys.exit(app.exec_())