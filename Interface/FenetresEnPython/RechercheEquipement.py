import datetime
from threading import Thread

import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.RechercheEquipementUI import Ui_RechercheEquipement

class RechercheEquipement(Ui_RechercheEquipement):
    def __init__(self, widget, finChargement):
        self.setupUi(widget)
        self.ajoutRechercheEquipement()
        self.finChargement = finChargement

    def ajoutRechercheEquipement(self):
        #Recuperation des differents attributs d'un equipement
        self.equipementManager = EquipementManager("DataBase_Equipement.json", 'DataBase_BDT.json')
        self.listeCleDonnees = list()
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        self.listeCleDonnees.append("ID")
        for element in self._conf['champsAcceptes-Equipement']:
            self.listeCleDonnees.append(element)
        # self.listeCleDonnees = ()
        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeCentreService = list(self._conf['CentreService'])
        self.listeSalle = list(self._conf['Salle'])
        self.listeProvenance = list(self._conf['Provenance'])

        #Mise a jour des listes avec les bons elements
        self.comboBoxCategorieEquipement.clear()
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItems(self.listeCategorieEquipement)
        self.comboBoxEtatService.clear()
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItems(self.listeEtatService)
        self.comboBoxCentreService.clear()
        self.comboBoxCentreService.addItem("")
        self.comboBoxCentreService.addItems(self.listeCentreService)
        self.comboBoxSalle.clear()
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItems(self.listeSalle)
        self.comboBoxProvenance.clear()
        self.comboBoxProvenance.addItems(self.listeProvenance)

        fichierConf.close()

        #Mise en forme de la page d'accueil
        self.tableResultats.setColumnCount(len(self.listeCleDonnees))
        # self.tableResultats.setHorizontalHeaderLabels("ID")
        self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.setRowCount(0)


        self.dictionnaireRecherche = dict()

        #Connexion des differents champs de selections
        self.comboBoxCategorieEquipement.currentTextChanged.connect(self.rechercheCategorieThread)
        self.comboBoxEtatService.currentTextChanged.connect(self.rechercheEtatDeServiceThread)
        self.comboBoxCentreService.currentTextChanged.connect(self.rechercheCentreServiceThread)
        self.comboBoxSalle.currentTextChanged.connect(self.rechercheSalleThread)
        self.comboBoxProvenance.currentTextChanged.connect(self.rechercheProvenanceThread)
        self.lineEditNumeroSerie.returnPressed.connect(self.rechercheNumeroSerieThread)
        self.boutonActualiser.clicked.connect(self.rechercheNumeroSerieThread)
        self.boutonNouvelleRecherche.clicked.connect(self.nouvelleRecherche)
        self.tableResultats.horizontalHeader().sectionClicked.connect(self.tableResultats.sortItems)

        self.tableResultats.horizontalHeader().sectionClicked.connect(self.trier)
        self.colonneClique = None
        self.nombreClique = 0
        #Empeche la modification de la table
        self.tableResultats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers );
        self.tableResultats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableResultats.cellDoubleClicked.connect(self.choisirEquipement)
        self.listeResultat = list()
        self.modificationEquipement = None
        self.equipementSelectionne = None

    def choisirEquipement(self, ligne, colonne):
        print("ligne", ligne)
        print("colonne", colonne)
        print(self.tableResultats.item(ligne,0).data(0))
        self.equipementSelectionne = dict()
        indice = 0
        for cle in self.listeCleDonnees:
            if(cle == "ID"):
                self.equipementSelectionne[cle] = int(self.tableResultats.item(ligne,indice).data(0))
            elif cle == "DateAcquisition" or cle == "DateDernierEntretien":
                self.equipementSelectionne[cle] = datetime.datetime.strptime(self.tableResultats.item(ligne,indice).data(0) , '%Y-%m-%d')
            else:
                self.equipementSelectionne[cle] = self.tableResultats.item(ligne,indice).data(0)
            indice += 1
        # self.modificationEquipement = QtWidgets.QWidget()
        # self.modificationEquipementUI = ModificationEquipementUI()
        # self.modificationEquipementUI.setupUi(self.modificationEquipement, equipement)
        # # self.modificationEquipement.setStyleSheet("background: white;")
        print (self.equipementSelectionne)
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
        if(self.comboBoxCategorieEquipement.currentText() != ""):
            self.dictionnaireRecherche["CategorieEquipement"] = self.comboBoxCategorieEquipement.currentText()

        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.remplirTableau()
        self.finChargement.finProcessus.emit()


    def rechercheEtatDeService(self):
        """Methode permettant la recherche par rapport au champ de recherche
            d'etat de service d'equipement"""
        if (self.comboBoxEtatService.currentText() != ""):
            self.dictionnaireRecherche["EtatService"] = self.comboBoxEtatService.currentText()

        else:
            self.dictionnaireRecherche.pop("EtatService")
        self.remplirTableau()

    def rechercheCentreService(self):
        """Methode permettant la recherche par rapport au champ de recherche
            d'etat de centre de service d'equipement"""
        if (self.comboBoxCentreService.currentText() != ""):
            self.dictionnaireRecherche["CentreService"] = self.comboBoxCentreService.currentText()

        else:
            self.dictionnaireRecherche.pop("CentreService")
        self.remplirTableau()

    def rechercheSalle(self):
        """Methode permettant la recherche par rapport au champ de recherche
            de salle """
        if (self.comboBoxSalle.currentText() != ""):
            self.dictionnaireRecherche["Salle"] = self.comboBoxSalle.currentText()

        else:
            self.dictionnaireRecherche.pop("Salle")
        self.remplirTableau()

    def rechercheProvenance(self):
        """Methode permettant la recherche par rapport au champ de recherche
           Provenance"""
        if (self.comboBoxProvenance.currentText() != ""):
            self.dictionnaireRecherche["Provenance"] = self.comboBoxProvenance.currentText()
        else:
            self.dictionnaireRecherche.pop("Provenance")
        self.remplirTableau()

    def rechercheNumeroSerie(self):
        """Methode permettant la recherche par rapport au champ de recherche
            Numero de Serie"""
        print("recherche numero de serie")
        if (self.lineEditNumeroSerie.text() != ""):
            self.dictionnaireRecherche["NumeroSerie"] = self.lineEditNumeroSerie.text()

        else:
            if "NumeroSerie" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("NumeroSerie")
        self.remplirTableau()

    def remplirTableau(self):
        """Methode permettant de remplir la table des resultats
        Le remplissage se fait avec le resultat des donnees"""
        if(any(self.dictionnaireRecherche)):
            self.listeResultat = self.equipementManager.RechercherEquipement(self.dictionnaireRecherche)
            self.tableResultats.setRowCount(len(self.listeResultat))
            for i, dictionnaire in enumerate(self.listeResultat):
                # Creation des QTableWidgetItem
                colonne = 0
                # print(dictionnaire)
                # print(self.listeCleDonnees)
                for cle in self.listeCleDonnees:
                    self.tableResultats.setItem(i, colonne, QTableWidgetItem(str(dictionnaire[cle])))
                    colonne += 1
                self.tableResultats.resizeColumnsToContents()

        else:
            print("dictionnaire de recherche vide")

    def nouvelleRecherche(self):
        self.comboBoxProvenance.setCurrentText("")
        self.comboBoxSalle.setCurrentText("")
        self.comboBoxCategorieEquipement.setCurrentText("")
        self.comboBoxCentreService.setCurrentText("")
        self.comboBoxEtatService.setCurrentText("")
        self.lineEditNumeroSerie.setText("")
        # self.tableResultats.clear()
        # self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.setRowCount(0)

    def rechercheCategorieThread(self):
        thread = RechercherEquipement(self.rechercheCategorieEquipement)
        thread.start()

    def rechercheEtatDeServiceThread(self):
        thread = RechercherEquipement(self.rechercheEtatDeService)
        thread.start()

    def rechercheCentreServiceThread(self):
        thread = RechercherEquipement(self.rechercheCentreService)
        thread.start()

    def rechercheSalleThread(self):
        thread = RechercherEquipement(self.rechercheSalle)
        thread.start()

    def rechercheProvenanceThread(self):
        thread = RechercherEquipement(self.rechercheProvenance)
        thread.start()

    def rechercheNumeroSerieThread(self):
        thread = RechercherEquipement(self.rechercheNumeroSerie)
        thread.start()


class RechercherEquipement (Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction


    def run(self):
        self.fonction()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rechercheEquipement = QtWidgets.QWidget()
    rechercheEquipementUI = RechercheEquipement(rechercheEquipement, None)
    rechercheEquipement.show()
    sys.exit(app.exec_())
