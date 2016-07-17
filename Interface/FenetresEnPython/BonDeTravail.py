# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BdT3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from BDD.PieceManager import PieceManager
from Interface.FenetresEnPython.BonDeTravailUI import Ui_BonDeTravail


class BonDeTravail(Ui_BonDeTravail):
    def __init__(self, widget, consulterBDT = None, ajouterID = None):
        self.setupUi(widget)
        self.ajoutBonDeTravail()
        self.boutonConsultation.hide()
        self.boutonAjoutBDT.setDisabled(True)
        self.boutonSauvegarde.hide()
        self.boutonFlecheDoubleDroite.hide()
        self.boutonFlecheDroite.hide()
        self.boutonFlecheGauche.hide()
        self.boutonFlecheDoubleGauche.hide()
        self.dic_request = dict()
        self.listeAjoutPieceReparation = list()
        self.pushButtonValider.setDisabled(True)

        if(consulterBDT is not None):
            self.lineEditID.setText(str(consulterBDT["ID-EQ"]))
            self.chercherEquipement()
            self.indiceBonDeTravail = int(consulterBDT["ID-BDT"]) - 1
            self.chargerBonTravail()
            self.ajoutBonDeTravail()
        if(ajouterID is not None):
            self.lineEditID.setText(ajouterID)
            self.chercherEquipement()
            self.nouveauBondeTravail()


    def ajoutBonDeTravail(self):

        self.labelEcritureBonTravail.setText("")
        #Connexion de l'appuie de la touche entree
        self.lineEditID.returnPressed.connect(self.chercherEquipement)

        #Creation des differents elements utiles pour la sauvegarde
        self.equipementManager = EquipementManager('DataBase_Equipement.json', 'DataBase_BDT.json')
        self.bonDeTravailManager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')
        self.pieceManager = PieceManager()
        self.equipementDictionnaire = None
        self.listeBonDeTravail = list()
        self.indiceBonDeTravail = 0

        self.listeLabelCache = list()
        self.listeLabelCache.append(self.labelCacheNomTech)
        self.listeLabelCache.append(self.labelCacheDate)
        self.listeLabelCache.append(self.labelCacheTemps)
        self.listeLabelCache.append(self.labelCacheDescSit)
        self.listeLabelCache.append(self.labelCacheDescInt)

        for label in self.listeLabelCache:
            label.hide()

        self.listeWidget = list()
        self.listeWidget.append(self.textEditDescIntervention)
        self.listeWidget.append(self.textEditDescSituation)
        self.listeWidget.append(self.timeEditTempsEstime)
        self.listeWidget.append(self.labelEcritureBonTravail)
        self.listeWidget.append(self.dateEdit)
        # self.listeWidget.append(self.comboBoxNomTech)

        self.colonneClique = None
        self.nombreClique = 0


        #Connexion des differents boutons
        self.boutonSauvegarde.clicked.connect(self.sauvegarderBonDeTravail)
        self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
        self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
        self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
        self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)
        self.comboBoxOuvertFerme.currentTextChanged.connect(self.editionBonDeTravail)

        self.boutonActualiser.clicked.connect(self.chercherEquipement)
        self.boutonAjoutBDT.clicked.connect(self.nouveauBondeTravail)

        self.boutonConsultation.clicked.connect(self.consulterBonDeTravail)
        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)
        self.comboBoxCategoriePiece.currentTextChanged.connect(self.choisirCategoriePiece)
        # self.listePieceReparation = list()
        self.pushButtonValider.clicked.connect(self.validerChoixPiece)
        self.listeCleDonnees = list(["Categorie","Nom Piece", "Nombre"])
        self.tableWidgetPiecesAssociees.setColumnCount(len(self.listeCleDonnees))
        self.tableWidgetPiecesAssociees.setHorizontalHeaderLabels(self.listeCleDonnees)
        self.tableWidgetPiecesAssociees.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetPiecesAssociees.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetPiecesAssociees.horizontalHeader().sectionClicked.connect(self.trier)

    def chercherEquipement(self):
        '''
            Recuperation de l'equipement associe a l'ID dans le cas ou il existe
            Affichage des informations de l'equipement dans les champs existants
            Recuperation des bons de travail associes a cet equipement
            :param: None
            :return:
        '''
        #On fait la requete a la BDD
        self.boutonConsultation.hide()
        self.boutonSauvegarde.hide()
        self.boutonAjoutBDT.show()
        self.boutonAjoutBDT.setDisabled(True)
        self.comboBoxOuvertFerme.setDisabled(False)
        print("recherche equipement")
        self.dic_request['ID'] = self.lineEditID.text()
        listeTrouve = self.equipementManager.RechercherEquipement(self.dic_request)
        #On efface les bons de travail deja affiche
        self.listeBonDeTravail.clear()
        if(any(listeTrouve)):
            #Si on a trouve un equipement correspondant, on affiche les informations correspondantes
            self.equipementDictionnaire = listeTrouve[0]
            self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
            self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
            self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
            self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
            self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])
            #On fait la recheche des bons de travail
            self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"ID-EQ": self.lineEditID.text()})
            self.indiceBonDeTravail = 0
            self.chargerBonTravail()
            self.boutonAjoutBDT.setDisabled(False)
            self.boutonFlecheDoubleDroite.show()
            self.boutonFlecheDroite.show()
            self.boutonFlecheGauche.show()
            self.boutonFlecheDoubleGauche.show()
            self.pushButtonValider.setDisabled(False)
        else:
            #Dans le cas ou on ne trouve pas d'equipement associe a cet ID
            self.equipementDictionnaire = None
            self.labelEcritureCatEquip.clear()
            self.labelEcritureCentreService.clear()
            self.labelEcritureMarque.clear()
            self.labelEcritureSalle.clear()
            self.labelEcritureModele.clear()
            self.labelEcritureBonTravail.clear()
            self.dateEdit.clear()
            self.timeEditTempsEstime.clear()
            self.textEditDescSituation.clear()
            self.textEditDescIntervention.clear()
            self.boutonAjoutBDT.setDisabled(True)
            self.comboBoxOuvertFerme.setDisabled(True)
            self.boutonFlecheDoubleDroite.hide()
            self.boutonFlecheDroite.hide()
            self.boutonFlecheGauche.hide()
            self.boutonFlecheDoubleGauche.hide()
            self.pushButtonValider.setDisabled(True)

    def sauvegarderBonDeTravail(self):
        '''
           Methode permettant la sauvegarde du bon de travail
           Recuperation des informations des differents champs
           Puis sauvegarde dans la BDD
            :param: None
            :return:
        '''
        #Recuperation des differentes informations dans les champs de BDT
        if(self.equipementDictionnaire is not None):
            dictionnaireDonnees = dict()
            dictionnaireDonnees["Date"] = self.dateEdit.date().toPyDate()
            dictionnaireDonnees["TempsEstime"] = (self.timeEditTempsEstime.time().toPyTime())
            dictionnaireDonnees["DescriptionSituation"] = self.textEditDescSituation.toPlainText()
            dictionnaireDonnees["DescriptionIntervention"] = self.textEditDescIntervention.toPlainText()
            dictionnaireDonnees["NomTechnicien"] = self.comboBoxNomTech.currentText()
            if(self.comboBoxOuvertFerme.currentText() != "Ouvert"):
                dictionnaireDonnees["EtatBDT"] = "Ferme"
            else:
                dictionnaireDonnees["EtatBDT"] = self.comboBoxOuvertFerme.currentText()
            dictionnaireDonnees["Pieces"] = self.listeAjoutPieceReparation
            #Decrementation des pieces dans le stock
            self.pieceManager.choisirPiece(self.listeAjoutPieceReparation)
            if(any(self.equipementDictionnaire)):
                #On ajoute le bon de travail a un equipement existant
                dicRetour = (self.bonDeTravailManager.AjouterBonTravail(self.equipementDictionnaire["ID"], dictionnaireDonnees))
                print(dicRetour)
                if dicRetour["Reussite"]:
                    print("Reussi")
                    idBDT = self.bonDeTravailManager._ObtenirProchainIDdeBDT(self.dic_request["ID"])
                    dictionnaireDonnees["ID-BDT"] = idBDT
                    self.listeBonDeTravail.append(dictionnaireDonnees)


            self.confirmation()

    def chargerBonTravail(self):
        '''
            Methode permettant le chargement des informations d'un bon de travail
            Mise des informations du bon de travall dans les differents champs
             :param: None
             :return:
         '''
        if(any(self.listeBonDeTravail)):
            #Si un bon de travail a ete trouve, on remplit les differents champs associes
            self.listeAjoutPieceReparation.clear()
            self.dateEdit.setDate(self.listeBonDeTravail[self.indiceBonDeTravail]["Date"])
            self.textEditDescSituation.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"])
            self.textEditDescSituation.wordWrapMode()
            self.textEditDescIntervention.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"])
            self.textEditDescIntervention.wordWrapMode()
            #Remplir le temps estime
            #TODO: Remplir le temps estime associe a un BDT
            if isinstance(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"], datetime.time):
                self.timeEditTempsEstime.setTime(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"])
            if self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"] != "Ouvert":
                self.comboBoxOuvertFerme.setCurrentText("Fermé")
            idBDT = str(self.equipementDictionnaire["ID"]) + "-" + str(self.indiceBonDeTravail + 1)
            self.labelEcritureBonTravail.setText(idBDT)
            self.tableWidgetPiecesAssociees.setRowCount(0)
            if "Pieces" in self.listeBonDeTravail[self.indiceBonDeTravail]:
                if self.listeBonDeTravail[self.indiceBonDeTravail]["Pieces"] is not None:
                    print(len(self.listeBonDeTravail[self.indiceBonDeTravail]["Pieces"]))
                    self.tableWidgetPiecesAssociees.setRowCount(len(self.listeBonDeTravail[self.indiceBonDeTravail]["Pieces"]))
                    ligne = 0
                    for tuple in self.listeBonDeTravail[self.indiceBonDeTravail]["Pieces"]:
                        print(tuple)
                        categorie, nomPiece, nombre = tuple
                        self.tableWidgetPiecesAssociees.setItem(ligne, 0,
                                                         QTableWidgetItem(categorie))
                        self.tableWidgetPiecesAssociees.setItem(ligne, 1, QTableWidgetItem(nomPiece))
                        self.tableWidgetPiecesAssociees.setItem(ligne, 2, QTableWidgetItem(str(nombre)))
                        ligne += 1
                    self.listeAjoutPieceReparation.append((categorie, nomPiece, nombre))
            #inutile
            # self.labelCacheDate.setText(str(self.listeBonDeTravail[self.indiceBonDeTravail]["Date"]))
            # self.labelCacheDescInt.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"])
            # self.labelCacheDescInt.wordWrap()
            # self.labelCacheDescSit.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"])
            # self.labelCacheDescSit.wordWrap()
            # self.labelCacheTemps.setText(str(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"]))
            # self.labelCacheNomTech.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["NomTechnicien"])

    #TODO : creer une methode similaire a chargerBonDeTravail qui va s'occuper de mettre les bonnes informations dans les labels "Ce que j'ai ecrit"
    def remplirBonDeTravail(self):

        self.labelCacheNomTech.setText(self.comboBoxNomTech.currentText())
        self.labelCacheDate.setText(str(self.dateEdit.date().toPyDate()))
        self.labelCacheTemps.setText(str(self.timeEditTempsEstime.time().toPyTime()))
        self.labelCacheDescSit.setText(self.textEditDescSituation.toPlainText())
        self.labelCacheDescInt.setText(self.textEditDescIntervention.toPlainText())


    def bonTravailSuivant(self):
        '''
            Methode permettant d'afficher le bon de travail suivant
             :param: None
             :return:
         '''
        if(self.indiceBonDeTravail < len(self.listeBonDeTravail) - 1):
            self.indiceBonDeTravail += 1
            self.chargerBonTravail()

    def bonTravailPrecedent(self):
        '''
            Methode permettant d'afficher le bon de travail precedent
             :param: None
             :return:
         '''
        if (self.indiceBonDeTravail > 0):
            self.indiceBonDeTravail -= 1
            self.chargerBonTravail()

    def bonTravailPremier(self):
        '''
            Methode permettant de retourner au premier bon de travail
             :param: None
             :return:
         '''
        self.indiceBonDeTravail = 0
        self.chargerBonTravail()

    def bonTravailDernier(self):
        '''
            Methode permettant d'aller au dernier bon de travail
             :param: None
             :return:
         '''
        self.indiceBonDeTravail = len(self.listeBonDeTravail) - 1
        self.chargerBonTravail()

    def editionBonDeTravail(self):
        print("edition")
        if(self.comboBoxOuvertFerme.currentText() == "Ouvert"):
            self.dateEdit.setDisabled(False)
            self.timeEditTempsEstime.setDisabled(False)
            self.textEditDescSituation.setDisabled(False)
            self.textEditDescIntervention.setDisabled(False)
        else:
            self.dateEdit.setDisabled(True)
            self.timeEditTempsEstime.setDisabled(True)
            self.textEditDescSituation.setDisabled(True)
            self.textEditDescIntervention.setDisabled(True)

    def nouveauBondeTravail(self):
        # self.textEditDescIntervention.clear()
        # self.textEditDescIntervention.show()
        # self.textEditDescSituation.clear()
        # self.timeEditTempsEstime.clear()
        # self.labelEcritureBonTravail.clear()
        # self.dateEdit.clear()
        # self.comboBoxNomTech.setCurrentText()
        for widget in self.listeWidget:
            widget.show()
            widget.clear()
        self.comboBoxOuvertFerme.setDisabled(False)
        self.comboBoxOuvertFerme.setCurrentIndex(0)
        self.comboBoxNomTech.show()
        self.boutonAjoutBDT.hide()
        self.boutonFlecheDoubleDroite.hide()
        self.boutonFlecheDroite.hide()
        self.boutonFlecheGauche.hide()
        self.boutonFlecheDoubleGauche.hide()
        self.boutonConsultation.show()
        if(any(self.listeBonDeTravail)):
            self.boutonSauvegarde.show()

        for label in self.listeLabelCache:
            label.hide()
        self.listeAjoutPieceReparation.clear()

    def consulterBonDeTravail(self):
        self.comboBoxNomTech.show()
        self.boutonAjoutBDT.hide()
        self.boutonFlecheDoubleDroite.show()
        self.boutonFlecheDroite.show()
        self.boutonFlecheGauche.show()
        self.boutonFlecheDoubleGauche.show()
        self.boutonConsultation.show()
        self.boutonSauvegarde.show()
        self.boutonAjoutBDT.show()
        self.boutonConsultation.hide()
        self.comboBoxOuvertFerme.setDisabled(False)
        for label in self.listeLabelCache:
            label.hide()

        self.chargerBonTravail()

    def confirmation(self):
        self.boutonConsultation.hide()
        self.textEditDescIntervention.hide()
        self.textEditDescSituation.hide()
        self.timeEditTempsEstime.hide()
        self.labelCacheDescInt.hide()
        self.dateEdit.hide()
        self.comboBoxNomTech.hide()

        self.boutonSauvegarde.hide()
        self.boutonAjoutBDT.hide()
        self.boutonFlecheDoubleDroite.hide()
        self.boutonFlecheDroite.hide()
        self.boutonFlecheGauche.hide()
        self.boutonFlecheDoubleGauche.hide()
        self.comboBoxOuvertFerme.setDisabled(True)
        for label in self.listeLabelCache:
            label.show()
        self.remplirBonDeTravail()
        if(any(self.listeBonDeTravail)):
            self.boutonConsultation.show()
        self.boutonAjoutBDT.show()
        self.listeAjoutPieceReparation.clear()


    def afficheSaisi(self):

        self.dateEdit.hide()
        self.comboBoxNomTech.hide()
        self.timeEditTempsEstime.hide()
        self.textEditDescIntervention.hide()
        self.textEditDescSituation.hide()

    def chargerEquipement(self):
        self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
        self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
        self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
        self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
        self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])
        self.lineEditID.setText(self.equipementDictionnaire["ID"])
        self.chargerBonTravail()
        self.nouveauBondeTravail()

    def consulterBonTravailSpecifique(self, dict):
        self.lineEditID.setText(dict["ID-EQ"])
        self.chercherEquipement()
        self.indiceBonDeTravail = dict["ID-BDT"] - 1
        self.chargerBonTravail()
        self.consulterBonDeTravail()

    def chercherEquipementThread(self):
        thread = RechercherBonDeTravail(self.chercherEquipement)
        thread.start()

    def choisirCategoriePiece(self):
        self.comboBoxNomPiece.clear()
        listePiece = self.pieceManager.ObtenirListePiece(self.comboBoxCategoriePiece.currentText())
        self.comboBoxNomPiece.addItems(listePiece)

    def validerChoixPiece(self):
        categorie = self.comboBoxCategoriePiece.currentText()
        nomPiece = self.comboBoxNomPiece.currentText()
        nombre = self.spinBoxNombrePiece.text()
        self.tableWidgetPiecesAssociees.setRowCount(self.tableWidgetPiecesAssociees.rowCount() + 1)

        self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 0, QTableWidgetItem(categorie))
        self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 1, QTableWidgetItem(nomPiece))
        self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 2, QTableWidgetItem((nombre)))

        self.listeAjoutPieceReparation.append((categorie, nomPiece, int(nombre)))
        print(self.listeAjoutPieceReparation)

    def trier(self, numeroColonne):
        """Methode permettant le tri des colonnes lors du clique sur l'une d'entre elle
        Un clic fait un tri croisssant
        Un second clic fera un tri decroissant"""
        print(numeroColonne)
        if numeroColonne == self.colonneClique:
            if self.nombreClique % 2 == 0:
                self.tableWidgetPiecesAssociees.sortByColumn(numeroColonne, Qt.AscendingOrder)
            else:
                self.tableWidgetPiecesAssociees.sortByColumn(numeroColonne, Qt.DescendingOrder)
            self.nombreClique += 1
        else:
            self.nombreClique = 1
            self.tableWidgetPiecesAssociees.sortByColumn(numeroColonne, Qt.AscendingOrder)
            self.colonneClique = numeroColonne

class RechercherBonDeTravail (Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction


    def run(self):
        self.fonction()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = BonDeTravail(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())


