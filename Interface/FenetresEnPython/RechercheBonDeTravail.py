import datetime
import re
from threading import Thread

import yaml
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QLocale, QDate
from PyQt5.QtWidgets import QTableWidgetItem, QCalendarWidget

from BDD.BonTravailManagerSQLite import BonTravailManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase, pathFichierConf
from Interface.FenetresEnPython.RechercheBonDeTravailUI import Ui_RechercheBonDeTravail
from Interface.FenetresEnPython.Signaux import Communicate


class RechercheBonDeTravail(Ui_RechercheBonDeTravail):
    #Classe permettant la gestion de la recherche d'un bon de travail
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutRechercheBonDeTravail()
        self.chargement = Communicate()


    def ajoutRechercheBonDeTravail(self):
        # Recuperation des differents attributs
        self.bonDeTravailManager = BonTravailManager(pathBonTravailDatabase)
        try:
            fichierConf = open(pathFichierConf, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", pathFichierConf)  # définir ce qu'il faut faire pour corriger

        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeCategorieEquipement.sort()
        self.listeCentreService = list(self._conf['CentreService'])
        self.listeCentreService.sort()
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeEtatService.sort()

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

        self.signalRechercheBon = Communicate()
        self.signalRechercheBon.aucunResultat.connect(self.aucunResultat)
        self.signalRechercheBon.remplirTableau.connect(self.remplirTableau)
        self.signalRechercheBon.nouvelleRecherche.connect(self.nouvelleRecherche)
        #modification calendrier
        calendrierApres = QCalendarWidget()
        calendrierApres.setStyleSheet("background :#F5F5F5;\n color: black;")
        calendrierApres.setGridVisible(True)
        self.calendrierApres.setCalendarWidget(calendrierApres)
        calendrierApres.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendrierApres.setLocale(QLocale(QLocale.French, QLocale.France))
        calendrierAvant = QCalendarWidget()
        calendrierAvant.setStyleSheet("background :#F5F5F5;\n color: black;")
        calendrierAvant.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        calendrierAvant.setGridVisible(True)
        self.calendrierAvant.setCalendarWidget(calendrierAvant)
        self.calendrierAvant.setLocale(QLocale(QLocale.French, QLocale.France))

        self.calendrierAvant.setDate(QDate.currentDate())
        self.calendrierApres.setDate(QDate.currentDate())

        #Creation des differents colonnes pour le tableau de resultat
        # self.listeCleDonnees = list(["IdEquipement", "NumeroBonTravail", "CategorieEquipement", "Modele", "CentreService", "EtatBDT", "Date", "DescriptionSituation"])
        self.listeCleDonnees = list(["IdEquipement", "NumeroBonTravail", "CategorieEquipement", "Modele", "CentreService", "EtatBDT", "Date", "DescriptionSituation"])


        #liste contenant les bons résultant de la recherche
        self.listeResultat = list()
        #liste contenant les informations des bons a afficher
        self.listeDonnees = list()


        self.tableResultats.setColumnCount(len(self.listeCleDonnees))
        self.tableResultats.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableResultats.resizeColumnsToContents()
        self.tableResultats.setRowCount(0)

        self.dictionnaireRecherche = dict()

        #Connexion des differentes recherches pour la mise a jour automatique
        self.comboBoxCategorieEquipement.currentTextChanged.connect(self.rechercheCategorieEquipement)
        self.comboBoxEtat.currentTextChanged.connect(self.rechercheEtatDeService)
        self.comboBoxCentreService.currentTextChanged.connect(self.rechercheCentreService)
        self.calendrierAvant.dateChanged.connect(self.rechercheDateAvant)
        self.lineEditDescriptionSituation.returnPressed.connect(self.rechercheDescriptionSituation)
        self.calendrierApres.dateChanged.connect(self.rechercheDateApres)
        self.boutonNouvelleRecherche.clicked.connect(self.signalRechercheBon.nouvelleRecherche.emit)
        self.tableResultats.horizontalHeader().sectionClicked.connect(self.trier)
        self.boutonActualiser.clicked.connect(self.rechercherBonTravailThread)
        self.colonneClique = None
        self.nombreClique = 0
        # Empeche la modification de la table
        self.tableResultats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers);
        self.tableResultats.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableResultats.cellDoubleClicked.connect(self.choisirBonDeTravail)
        self.bonDeTravailSelectionne = None

    def choisirBonDeTravail(self, ligne, colonne):
        print("ligne", ligne)
        print("colonne", colonne)
        print(self.tableResultats.item(ligne, 0).data(0))
        self.bonDeTravailSelectionne = dict()
        print(self.listeResultat)
        for bon in self.listeResultat:
            print((self.tableResultats.item(ligne,0).data(0)))
            print((self.tableResultats.item(ligne,1).data(0)))
            if(bon["IdEquipement"] == str(self.tableResultats.item(ligne,0).data(0)) and bon["NumeroBonTravail"] == str(self.tableResultats.item(ligne, 1).data(0))):
                self.bonDeTravailSelectionne = bon
        print(self.bonDeTravailSelectionne)

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
            recherche = verificationTexte(self.comboBoxCategorieEquipement.currentText())
            print("recherche", recherche)
            self.dictionnaireRecherche["CategorieEquipement"] = recherche
        else:
            self.dictionnaireRecherche.pop("CategorieEquipement")
        self.rechercherBonTravailThread()




    def rechercheDateAvant(self):
        '''
            Recuperation des bons de travails qui sont anterieurs a la date indique
            :param: None
            :return:
        '''
        self.dictionnaireRecherche["AvantLe"] = self.calendrierAvant.date().toPyDate()
        self.rechercherBonTravailThread()


    def rechercheDateApres(self):
        '''
            Recuperation des bons de travails qui sont posterieurs a la date indique
            :param: None
            :return:
        '''
        self.dictionnaireRecherche["ApresLe"] = self.calendrierApres.date().toPyDate()
        self.rechercherBonTravailThread()


    def rechercheDescriptionSituation(self):
        '''
            Recuperation des bons de travails correspondant a la description
            :param: None
            :return:
        '''
        if (self.lineEditDescriptionSituation.text() != ""):
            self.dictionnaireRecherche["DescriptionSituation"] = self.lineEditDescriptionSituation.text()
        self.rechercherBonTravailThread()



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
        self.rechercherBonTravailThread()


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
        self.rechercherBonTravailThread()


    def rechercherBonTravail(self):
            '''
                Remplissage du tableau de resultat avec les eventuels bons de travail trouves
                :param: None
                :return:
            '''
            #Recherche parmi les coordonnes
            self.listeResultat.clear()
            if (any(self.dictionnaireRecherche)):
                print("Affichage dictionnaire de recherche :", self.dictionnaireRecherche)
                self.listeResultat = self.bonDeTravailManager.RechercherBonTravaiGenerique(self.dictionnaireRecherche)
                print(self.listeResultat)
                self.listeDonnees.clear()
                indice = 0
                if(len(self.listeResultat) > 0):
                    for bdt in self.listeResultat :
                            print(bdt["IdEquipement"])
                            dictDonnees = dict()
                            dictDonnees["IdEquipement"] = bdt["IdEquipement"]
                            dictDonnees["CategorieEquipement"] = bdt["CategorieEquipement"]
                            dictDonnees["Modele"] = bdt["Modele"]
                            dictDonnees["CentreService"] = bdt["CentreService"]
                            dictDonnees["EtatBDT"] = bdt["EtatBDT"]
                            dictDonnees["Date"] = bdt["Date"]
                            dictDonnees["NumeroBonTravail"] = bdt["NumeroBonTravail"]
                            dictDonnees["DescriptionSituation"] = bdt["DescriptionSituation"]
                            self.listeDonnees.append(dictDonnees)
                    self.signalRechercheBon.remplirTableau.emit()
                else:
                    print("Aucun resultat")
                    self.signalRechercheBon.aucunResultat.emit()
                    self.chargement.aucunResultat.emit()
            else:
                print("dictionnaire de recherche vide")
                self.signalRechercheBon.aucunResultat.emit()
            self.chargement.finChargement.emit()

    def remplirTableau(self):
        self.tableResultats.setRowCount(len(self.listeDonnees))
        for i, dictionnaire in enumerate(self.listeDonnees):
            # Creation des QTableWidgetItem
            colonne = 0
            for cle in self.listeCleDonnees:
                if(isinstance(dictionnaire[cle], datetime.date)):
                    self.tableResultats.setItem(i, colonne, QTableWidgetItem((str(dictionnaire[cle]))))
                elif (cle == "IdEquipement" or cle == "NumeroBonTravail"):
                    item = QTableWidgetItem()
                    item.setData(Qt.EditRole, int(dictionnaire[cle]))
                    self.tableResultats.setItem(i, colonne, item)
                else:
                    self.tableResultats.setItem(i, colonne, QTableWidgetItem((dictionnaire[cle])))
                colonne += 1
            self.tableResultats.resizeColumnsToContents()

    def aucunResultat(self):
        self.tableResultats.clearContents()
        self.tableResultats.setRowCount(0)


    def nouvelleRecherche(self):
        self.comboBoxCategorieEquipement.setCurrentText("")
        self.comboBoxCentreService.setCurrentText("")
        self.comboBoxEtat.setCurrentText("")
        self.lineEditDescriptionSituation.setText("")
        self.tableResultats.setRowCount(0)
        self.dictionnaireRecherche.clear()


    def rechercherBonTravailThread(self):
        thread = RechercherBonDeTravail(self.rechercherBonTravail)
        thread.start()


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


class RechercherBonDeTravail (Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction


    def run(self):
        self.fonction()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rechercheBonDeTravail = QtWidgets.QWidget()
    rechercheBonDeTravailUI = RechercheBonDeTravail(rechercheBonDeTravail)
    rechercheBonDeTravail.show()
    sys.exit(app.exec_())