# -*- coding: utf-8 -*-
import datetime
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtWidgets import QTableWidgetItem,QCalendarWidget

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from BDD.PieceManager import PieceManager
from Interface.FenetresEnPython.BonDeTravailUI import Ui_BonDeTravail
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase
from Interface.FenetresEnPython.Signaux import Communicate

class BonDeTravail(Ui_BonDeTravail):
    '''
        Classe gerant la fenetre permettant l'ajout et la modification des bons de travail
    '''
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
        self.listPieceReparationUtilise = list()
        self.pushButtonValider.setDisabled(True)
        self.chargement = Communicate()
        if(consulterBDT is not None):
            #Cas ou on consulter un bon de travail
            self.lineEditID.setText(str(consulterBDT["ID-EQ"]))
            self.chercherEquipement()
            indice = 0
            while(self.listeBonDeTravail[indice]["ID-BDT"] != str(consulterBDT["ID-BDT"])):
                print("id dans la liste", self.listeBonDeTravail[indice]["ID-BDT"])
                print("id recupere", consulterBDT["ID-BDT"])
                indice += 1
            self.indiceBonDeTravail = indice
            self.chargerBonTravail()
        if(ajouterID is not None):
            #Cas ou on va ajouter un bon de travail pour un equipement
            self.lineEditID.setText(ajouterID)
            self.chercherEquipement()
            self.nouveauBondeTravail()
        self.chargement.rechercheTermine.connect(self.chargerBonTravail)
        self.comboBoxCategoriePiece.currentTextChanged.connect(self.choisirCategoriePiece)
        self.nombreBonAjoute = 0

    def ajoutBonDeTravail(self):

        #Creation des differents elements utiles pour la sauvegarde
        self.equipementManager = EquipementManager(pathEquipementDatabase, pathBonTravailDatabase)
        self.bonDeTravailManager = BonTravailManager(pathBonTravailDatabase, pathEquipementDatabase)
        self.pieceManager = PieceManager()
        self.equipementDictionnaire = None
        self.listeBonDeTravail = list()
        self.indiceBonDeTravail = 0

        self.signalFenetreBonTravail = Communicate()
        self.signalFenetreBonTravail.chargerEquipement.connect(self.chargerEquipement)
        self.signalFenetreBonTravail.aucunEquipement.connect(self.aucunEquipementTrouve)
        self.signalFenetreBonTravail.confirmation.connect(self.confirmation)
        self.signalFenetreBonTravail.consultationBonTravail.connect(self.consulterBonDeTravail)
        self.signalFenetreBonTravail.editionBonTravail.connect(self.editionBonDeTravail)
        self.signalFenetreBonTravail.validerChoixPiece.connect(self.validerChoixPiece)
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
        #self.listeWidget.append(self.comboBoxNomTech)

        self.colonneClique = None
        self.nombreClique = 0


        #Connexion des differents boutons
        self.boutonSauvegarde.clicked.connect(self.sauvegarderBonDeTravailThread)
        self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
        self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
        self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
        self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)
        self.comboBoxOuvertFerme.currentTextChanged.connect(self.signalFenetreBonTravail.editionBonTravail.emit)

        self.boutonActualiser.clicked.connect(self.chercherEquipementThread)
        self.boutonAjoutBDT.clicked.connect(self.nouveauBondeTravail)

        self.boutonConsultation.clicked.connect(self.signalFenetreBonTravail.consultationBonTravail.emit)
        #Connexion de l'appuie de la touche entree
        self.lineEditID.returnPressed.connect(self.chercherEquipementThread)

        self.listeCategoriePiece = None

        # self.listePieceReparation = list()
        self.pushButtonValider.clicked.connect(self.signalFenetreBonTravail.validerChoixPiece.emit)
        #modification calendrierBDT
        calendrierBDT = QCalendarWidget()
        calendrierBDT.setStyleSheet("background :#F5F5F5;\n color: black;")
        calendrierBDT.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.dateEdit.setCalendarWidget(calendrierBDT)
        self.dateEdit.setLocale(QLocale(QLocale.French, QLocale.France))


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
        self.dic_request['ID'] = self.lineEditID.text()
        listeTrouve = self.equipementManager.RechercherEquipement(self.dic_request)
        self.boutonConsultation.hide()
        self.boutonSauvegarde.hide()
        self.boutonAjoutBDT.show()
        self.boutonAjoutBDT.setDisabled(True)
        self.comboBoxOuvertFerme.setDisabled(False)
        self.nombreBonAjoute = 0
        #On efface les bons de travail deja affiche
        self.listeBonDeTravail.clear()
        if(any(listeTrouve)):
            #Si on a trouve un equipement correspondant, on affiche les informations correspondantes
            self.equipementDictionnaire = listeTrouve[0]
            #On fait la recheche des bons de travail
            self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"ID-EQ": self.lineEditID.text()})
            self.indiceBonDeTravail = 0
            self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())

            self.signalFenetreBonTravail.chargerEquipement.emit()
            #self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
            #self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
            #self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
            #self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
            #self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])

            # self.boutonAjoutBDT.setDisabled(False)
            # self.boutonFlecheDoubleDroite.show()
            # self.boutonFlecheDroite.show()
            # self.boutonFlecheGauche.show()
            # self.boutonFlecheDoubleGauche.show()
            # self.pushButtonValider.setDisabled(False)
            # self.listeCategoriePiece.sort()
            # self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)
            self.rechercherBonTravail()
        else:
            #Dans le cas ou on ne trouve pas d'equipement associe a cet ID
            self.equipementDictionnaire = None
            self.signalFenetreBonTravail.aucunEquipement.emit()
        self.chargement.finChargement.emit()

    def aucunEquipementTrouve(self):
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
            self.pieceManager.ChoisirPiece(self.listeAjoutPieceReparation)
            if(any(self.equipementDictionnaire)):
                #On ajoute le bon de travail a un equipement existant
                dicRetour = (self.bonDeTravailManager.AjouterBonTravail(self.equipementDictionnaire["ID"], dictionnaireDonnees))
                print(dicRetour)
                if dicRetour["Reussite"]:
                    print("Reussi")
                    idBDT = str(int(self.listeBonDeTravail[self.indiceBonDeTravail]["ID-BDT"]) + 1 + self.nombreBonAjoute)
                    print("bon de travail d'id :", idBDT)
                    dictionnaireDonnees["ID-BDT"] = idBDT
                    self.listeBonDeTravail.append(dictionnaireDonnees)
            self.signalFenetreBonTravail.confirmation.emit()
            self.chargement.sauvegardeTermine.emit()
            self.nombreBonAjoute += 1

    def rechercherBonTravail(self):
        '''
            Methode permettant le chargement des informations d'un bon de travail
            Mise des informations du bon de travall dans les differents champs
             :param: None
             :return:
         '''
        print("Lancement de la recherche des bons de travail")
        if(any(self.listeBonDeTravail)):
            self.chargement.rechercheTermine.emit()

    def remplirBonDeTravail(self):
        #Methode permettant le remplissage des differents champs
        self.labelCacheNomTech.setText(self.comboBoxNomTech.currentText())
        self.labelCacheDate.setText(str(self.dateEdit.date().toPyDate()))
        self.labelCacheTemps.setText(str(self.timeEditTempsEstime.time().toPyTime()))
        self.labelCacheDescSit.setText(self.textEditDescSituation.toPlainText())
        self.labelCacheDescInt.setText(self.textEditDescIntervention.toPlainText())
        self.labelNomTechnicien.setText(self.comboBoxNomTech.currentText())

    def chargerBonTravail(self):
        #Si un bon de travail a ete trouve, on remplit les differents champs associes
        self.listeAjoutPieceReparation.clear()
        self.dateEdit.setDate(self.listeBonDeTravail[self.indiceBonDeTravail]["Date"])
        self.textEditDescSituation.setPlainText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"])
        self.textEditDescSituation.wordWrapMode()
        self.textEditDescIntervention.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"])
        self.textEditDescIntervention.wordWrapMode()
        self.boutonSauvegarde.setVisible(True)
        #Remplir le temps estime
        self.boutonFlecheDoubleDroite.show()
        self.boutonFlecheDroite.show()
        self.boutonFlecheGauche.show()
        self.boutonFlecheDoubleGauche.show()
        self.pushButtonValider.setDisabled(False)
        self.listeCategoriePiece.sort()
        self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)

        if isinstance(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"], datetime.time):
            self.timeEditTempsEstime.setTime(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"])
        if self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"] != "Ouvert":
            self.comboBoxOuvertFerme.setCurrentText("Fermé")
        idBDT = str(self.equipementDictionnaire["ID"]) + "-" + str(self.listeBonDeTravail[self.indiceBonDeTravail]["ID-BDT"])
        print("idBDT", idBDT)
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
                    self.listPieceReparationUtilise.append((categorie, nomPiece, nombre))

    def bonTravailSuivant(self):
        '''
            Methode permettant d'afficher le bon de travail suivant
             :param: None
             :return:
         '''
        if(self.indiceBonDeTravail < len(self.listeBonDeTravail) - 1):
            self.indiceBonDeTravail += 1
            self.rechercherBonTravail()

    def bonTravailPrecedent(self):
        '''
            Methode permettant d'afficher le bon de travail precedent
             :param: None
             :return:
         '''
        if (self.indiceBonDeTravail > 0):
            self.indiceBonDeTravail -= 1
            self.rechercherBonTravail()

    def bonTravailPremier(self):
        '''
            Methode permettant de retourner au premier bon de travail
             :param: None
             :return:
         '''
        self.indiceBonDeTravail = 0
        self.rechercherBonTravail()

    def bonTravailDernier(self):
        '''
            Methode permettant d'aller au dernier bon de travail
             :param: None
             :return:
         '''
        self.indiceBonDeTravail = len(self.listeBonDeTravail) - 1
        self.rechercherBonTravail()

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
        id = self.equipementDictionnaire["ID"] + "-" + str(self.equipementDictionnaire["NbBonTravail"] + 1 + self.nombreBonAjoute)
        self.labelEcritureBonTravail.setText(str(id))
        for label in self.listeLabelCache:
            label.hide()
        self.listeAjoutPieceReparation.clear()
        self.tableWidgetPiecesAssociees.setRowCount(0)

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
        self.textEditDescIntervention.show()
        self.textEditDescSituation.show()
        self.boutonConsultation.hide()
        self.comboBoxOuvertFerme.setDisabled(False)
        for label in self.listeLabelCache:
            label.hide()

        self.rechercherBonTravail()

    def confirmation(self):
        #Methode affichant le bon de travail une fois enregistre
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

    def chargerEquipement(self):
        #Methode permettant le chargement d'un equipement
        self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
        self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
        self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
        self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
        self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])
        self.lineEditID.setText(self.equipementDictionnaire["ID"])
        self.boutonAjoutBDT.setDisabled(False)
        #A modifier
        # self.rechercherBonTravail()
        # self.nouveauBondeTravail()

    def consulterBonTravailSpecifique(self, dict):
        #Methode permettant le chargement d'un bon de travail precis
        self.lineEditID.setText(dict["ID-EQ"])
        self.chercherEquipement()
        self.indiceBonDeTravail = dict["ID-BDT"] - 1
        self.rechercherBonTravail()
        self.signalFenetreBonTravail.consultationBonTravail.emit()

    def chercherEquipementThread(self):
        thread = BonDeTravailThread(self.chercherEquipement)
        thread.start()

    def choisirCategoriePiece(self):
        self.comboBoxNomPiece.clear()
        listePiece = self.pieceManager.ObtenirListePiece(self.comboBoxCategoriePiece.currentText())
        print(self.comboBoxCategoriePiece.currentText())
        self.comboBoxNomPiece.addItems(listePiece)

    def validerChoixPiece(self):
        #Methode permettant la validation du choix des pieces
        categorie = self.comboBoxCategoriePiece.currentText()
        nomPiece = self.comboBoxNomPiece.currentText()
        nombre = self.spinBoxNombrePiece.text()
        self.tableWidgetPiecesAssociees.setRowCount(self.tableWidgetPiecesAssociees.rowCount() + 1)
        self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 0, QTableWidgetItem(categorie))
        self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 1, QTableWidgetItem(nomPiece))
        self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 2, QTableWidgetItem((nombre)))
        if(int(nombre)>0):
            #On ne comptabilise les pièces que s'il y a un nombre non nul
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

    def sauvegarderBonDeTravailThread(self):
        print("Lancement du Thread de sauvegarde")
        thread = BonDeTravailThread(self.sauvegarderBonDeTravail)
        thread.start()

    def rechercherBonDeTravailThread(self):
        thread = BonDeTravailThread(self.rechercherBonTravail)
        thread.start()

class BonDeTravailThread(Thread):
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


