import datetime
import re
from threading import Thread

import yaml
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.EquipementManagerSQLite import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase, pathFichierConf
from Interface.FenetresEnPython.RechercheEquipementUI import Ui_RechercheEquipement
from Interface.FenetresEnPython.Signaux import Communicate


class RechercheEquipement(Ui_RechercheEquipement):
    #Classe permettant la gestion de la fenetre de recherche d'equipement
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutRechercheEquipement()
        self.chargement = Communicate()

    def ajoutRechercheEquipement(self):
        #Recuperation des differents attributs d'un equipement
        self.equipementManager = EquipementManager(pathEquipementDatabase)
        self.listeCleDonnees = list()
        self.listeHeaders= ['Id', "Catégorie d'équipement", 'Marque', 'Modèle', 'Numéro de Série', 'Salle', 'Unité', "Date d'aquisition",
        'Date du dernier Entretien', "Fréquence d'entretien", 'Provenance', 'Voltage', 'État de service', 'État de conservation', 'Commentaires', 
        'Chemin PDF']

        try:
            fichierConf = open(pathFichierConf, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", pathFichierConf)  # définir ce qu'il faut faire pour corriger

        # récupère la liste des 'accepted keys' dans le fichier de configuration
        for element in self._conf['champsAcceptes-Equipement']:
            self.listeCleDonnees.append(element)

        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeSalle = list(self._conf['Salle'])
        self.listeUnite = list(self._conf['Unite'])
        self.listeProvenance = list(self._conf['Provenance'])

        #Trie des differentes listes pour les comboBox
        self.listeCategorieEquipement.sort()
        self.listeEtatService.sort()
        self.listeUnite.sort()
        self.listeSalle.sort()
        self.listeProvenance.sort()

        #Mise a jour des listes avec les bons elements
        self.comboBoxCategorieEquipement.clear()
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItems(self.listeCategorieEquipement)
        self.comboBoxEtatService.clear()
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItems(self.listeEtatService)
        self.comboBoxSalle.clear()
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItems(self.listeSalle)
        self.comboBoxUnite.clear()
        self.comboBoxUnite.addItem("")
        self.comboBoxUnite.addItems(self.listeUnite)
        self.comboBoxProvenance.clear()
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItems(self.listeProvenance)

        fichierConf.close()

        #Mise en forme de la page d'accueil
        self.tableResultats.setHorizontalHeaderLabels(self.listeHeaders)
        self.tableResultats.setRowCount(0)

        self.signalRechercheEquipement = Communicate()
        self.signalRechercheEquipement.remplirTableau.connect(self.remplirTableau)
        self.signalRechercheEquipement.nouvelleRecherche.connect(self.nouvelleRecherche)
        self.dictionnaireRecherche = dict()

        #Connexion des differents champs de selections
        self.comboBoxCategorieEquipement.currentTextChanged.connect(self.rechercheCategorieEquipement)
        self.comboBoxEtatService.currentTextChanged.connect(self.rechercheEtatDeService)
        self.comboBoxUnite.currentTextChanged.connect(self.rechercheUnite)
        self.comboBoxSalle.currentTextChanged.connect(self.rechercheSalle)
        self.comboBoxProvenance.currentTextChanged.connect(self.rechercheProvenance)
        self.lineEditNumeroSerie.returnPressed.connect(self.rechercheNumeroSerie)
        self.boutonActualiser.clicked.connect(self.rechercheNumeroSerie)
        self.boutonNouvelleRecherche.clicked.connect(self.signalRechercheEquipement.nouvelleRecherche.emit)
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
        print(self.listeCleDonnees)
        for cle in self.listeCleDonnees:
            if(cle == "Id"):
                print("ligne", ligne)
                print("colonne", colonne)
                print(type(self.tableResultats.item(ligne, indice)))
                self.equipementSelectionne[cle] = self.tableResultats.item(ligne,indice).data(0)
            elif cle == "DateAcquisition" or cle == "DateDernierEntretien":
                self.equipementSelectionne[cle] = self.tableResultats.item(ligne,indice).data(0)
            else:
                self.equipementSelectionne[cle] = self.tableResultats.item(ligne,indice).data(0)
            indice += 1
        print (self.equipementSelectionne)

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
        if(self.comboBoxCategorieEquipement.currentText() != "" and self.comboBoxCategorieEquipement.count() > 0):
            recherche = verificationTexte(self.comboBoxCategorieEquipement.currentText())
            print("recherche", recherche)
            self.dictionnaireRecherche["CategorieEquipement"] = recherche

        else:
            if "CategorieEquipement" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("CategorieEquipement")
        self.rechercherEquipement()

    def rechercheEtatDeService(self):
        """Methode permettant la recherche par rapport au champ de recherche
            d'etat de service d'equipement"""
        if (self.comboBoxEtatService.currentText() != "" and self.comboBoxEtatService.count() >0):
            self.dictionnaireRecherche["EtatService"] = self.comboBoxEtatService.currentText()

        else:
            if "EtatService" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("EtatService")
        self.rechercherEquipement()

    def rechercheUnite(self):
        """Methode permettant la recherche par rapport au champ de recherche
            d'etat de centre de service d'equipement"""
        if (self.comboBoxUnite.currentText() != "" and self.comboBoxUnite.count() >0):
            self.dictionnaireRecherche["Unite"] = self.comboBoxUnite.currentText()

        else:
            if "Unite" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("Unite")
        self.rechercherEquipement()

    def rechercheSalle(self):
        """Methode permettant la recherche par rapport au champ de recherche
            de salle """
        if (self.comboBoxSalle.currentText() != "" and self.comboBoxSalle.count() >0):
            self.dictionnaireRecherche["Salle"] = self.comboBoxSalle.currentText()
        else:
            if "Salle" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("Salle")
        self.rechercherEquipement()

    def rechercheProvenance(self):
        """Methode permettant la recherche par rapport au champ de recherche
           Provenance"""
        if (self.comboBoxProvenance.currentText() != "" and self.comboBoxProvenance.count() >0):
            self.dictionnaireRecherche["Provenance"] = self.comboBoxProvenance.currentText()
        else:
            if "Provenance" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("Provenance")
        self.rechercherEquipement()

    def rechercheNumeroSerie(self):
        """Methode permettant la recherche par rapport au champ de recherche
            Numero de Serie"""
        print("recherche numero de serie")
        if (self.lineEditNumeroSerie.text() != ""):
            self.dictionnaireRecherche["NumeroSerie"] = self.lineEditNumeroSerie.text()
        else:
            if "NumeroSerie" in self.dictionnaireRecherche:
                self.dictionnaireRecherche.pop("NumeroSerie")
        self.rechercherEquipement()

    def rechercherEquipement(self):
        """Methode permettant de remplir la table des resultats
        Le remplissage se fait avec le resultat des donnees"""
        if(any(self.dictionnaireRecherche)):
            self.chargement.chargerEquipement.emit()
            self.listeResultat = self.equipementManager.RechercherEquipement(self.dictionnaireRecherche)
            self.signalRechercheEquipement.remplirTableau.emit()
        else:
            print("dictionnaire de recherche vide")
        self.chargement.finChargement.emit()

    def remplirTableau(self):
        self.tableResultats.setRowCount(len(self.listeResultat))
        if(any(self.listeResultat)):
            for i, dictionnaire in enumerate(self.listeResultat):
                # Creation des QTableWidgetItem
                colonne = 0
                for cle in self.listeCleDonnees:
                    if(cle == "Id"):
                        item = QTableWidgetItem()
                        item.setData(Qt.EditRole, int(dictionnaire[cle]))
                        self.tableResultats.setItem(i, colonne, item)
                    else:
                        self.tableResultats.setItem(i, colonne, QTableWidgetItem(str(dictionnaire[cle])))
                    colonne += 1
                self.tableResultats.resizeColumnsToContents()
        else:
            self.chargement.aucunResultat.emit()

    def nouvelleRecherche(self):
        self.comboBoxProvenance.setCurrentText("")
        self.comboBoxSalle.setCurrentText("")
        self.comboBoxCategorieEquipement.setCurrentText("")
        self.comboBoxUnite.setCurrentText("")
        self.comboBoxEtatService.setCurrentText("")
        self.lineEditNumeroSerie.setText("")
        self.tableResultats.setRowCount(0)
        print(self.dictionnaireRecherche)

    def rechercheCategorieThread(self):
        thread = RechercherEquipement(self.rechercheCategorieEquipement)
        thread.start()

    def rechercheEtatDeServiceThread(self):
        thread = RechercherEquipement(self.rechercheEtatDeService)
        thread.start()

    def rechercheUniteThread(self):
        thread = RechercherEquipement(self.rechercheUnite)
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

    def miseAJourRecherche(self):
        try:
            fichierConf = open(pathFichierConf, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", pathFichierConf)  # définir ce qu'il faut faire pour corriger
        # for element in self._conf['champsAcceptes-Equipement']:
            # self.listeCleDonnees.append(element)
        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeSalle = list(self._conf['Salle'])
        self.listeUnite = list(self._conf['Unite'])
        self.listeProvenance = list(self._conf['Provenance'])

        # Trie des differentes listes pour les comboBox
        self.listeCategorieEquipement.sort()
        self.listeEtatService.sort()
        self.listeUnite.sort()
        self.listeSalle.sort()
        self.listeProvenance.sort()

        # Mise a jour des listes avec les bons elements
        self.comboBoxCategorieEquipement.clear()
        self.comboBoxCategorieEquipement.addItem("")
        self.comboBoxCategorieEquipement.addItems(self.listeCategorieEquipement)
        self.comboBoxEtatService.clear()
        self.comboBoxEtatService.addItem("")
        self.comboBoxEtatService.addItems(self.listeEtatService)
        self.comboBoxUnite.clear()
        self.comboBoxUnite.addItem("")
        self.comboBoxUnite.addItems(self.listeUnite)
        self.comboBoxSalle.clear()
        self.comboBoxSalle.addItem("")
        self.comboBoxSalle.addItems(self.listeSalle)
        self.comboBoxProvenance.clear()
        self.comboBoxProvenance.addItem("")
        self.comboBoxProvenance.addItems(self.listeProvenance)

        fichierConf.close()

def verificationTexte(texte):
    print("Verification en cours")
    print(texte)
    copie = str(texte)
    listeOccurence = []
    for occ in re.finditer('[()]', texte):
        print(occ)
        listeOccurence.append(occ.start())
    print(listeOccurence)
    modification = 0
    for indice in listeOccurence:
        local = copie[:indice + modification] + '\\' + copie[indice + modification:]
        modification += 1
        copie = local
    print("Nouveau texte", copie)
    return copie


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
    rechercheEquipementUI = RechercheEquipement(rechercheEquipement)
    rechercheEquipement.show()
    sys.exit(app.exec_())
