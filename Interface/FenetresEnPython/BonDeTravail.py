# -*- coding: utf-8 -*-
import datetime
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from BDD.BonTravailManagerSQLite import BonTravailManager
from BDD.EquipementManagerSQLite import EquipementManager
from BDD.PieceManagerSQLite import PieceManager
from Interface.FenetresEnPython.BonDeTravailUI6 import Ui_BonDeTravail
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase, pathPieceDatabase
from Interface.FenetresEnPython.Signaux import Communicate

class BonDeTravail(Ui_BonDeTravail):
    '''
        Classe gerant la fenetre permettant l'ajout et la modification des bons de travail
    '''
    def __init__(self, widget, consulterBDT = None, ajouterID = None, equipement = None, listeBonTravail = None, bonSpecifique = False):
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
        self.consulterBDT = consulterBDT
        self.ajouterID = ajouterID
        self.modificationBon = True
        self.chargement.rechercheTermine.connect(self.chargerBonTravail)
        self.comboBoxCategoriePiece.currentTextChanged.connect(self.choisirCategoriePiece)
        if(self.consulterBDT is not None):
            #Cas ou on consulter un bon de travail
            # self.chercherEquipementThread()
            self.listeBonDeTravail = listeBonTravail
            if(len(listeBonTravail)):
                self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"IdEquipement":listeBonTravail[0]["IdEquipement"], "NumeroBonTravail":listeBonTravail[0]["NumeroBonTravail"]})

            if(self.equipementDictionnaire is not None):
                self.equipementDictionnaire = equipement
                if (any(self.listeBonDeTravail)):
                    self.boutonConsultation.show()

            else:
                #id_equipement = str(self.listeBonDeTravail[self.indiceBonDeTravail]["IdEquipement"])
                #self.equipementDictionnaire = self.equipementManager.RechercherEquipement((self.listeBonDeTravail[0]["IdEquipement"]))[0]
                if(equipement is None):
                    self.equipementDictionnaire = self.equipementManager.RechercherEquipement({"Id":str(self.listeBonDeTravail[0]["IdEquipement"])})[0]
                else:
                    self.equipementDictionnaire = equipement
            self.lineEditID.setText(str(self.equipementDictionnaire["Id"]))
            self.signalFenetreBonTravail.chargerEquipementAPartirBon.emit()
            self.consulterBonTravailSpecifique()
            self.boutonActualiser.setDisabled(True)
            self.lineEditID.setDisabled(True)
            self.boutonAjoutBDT.hide()
            self.boutonAjoutBDT.setDisabled(True)
            self.modificationBon = True
            if(bonSpecifique):
                self.boutonFlecheDoubleDroite.hide()
                self.boutonFlecheDroite.hide()
                self.boutonFlecheGauche.hide()
                self.boutonFlecheDoubleGauche.hide()
        if(ajouterID is not None):
            #Cas ou on va ajouter un bon de travail pour un equipement
            self.lineEditID.setText(str(equipement["Id"]))
            self.lineEditID.setDisabled(True)
            self.boutonActualiser.setDisabled(True)
            self.boutonConsultation.setDisabled(True)
            self.equipementDictionnaire = equipement
            self.signalFenetreBonTravail.chargerEquipement.emit()
            self.listeBonDeTravail = listeBonTravail
            self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
            self.listeCategoriePiece.sort()
            self.comboBoxCategoriePiece.clear()
            self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)
            self.signalFenetreBonTravail.nouveauBonTravail.emit()

    def ajoutBonDeTravail(self):

        #Creation des differents elements utiles pour la sauvegarde
        self.equipementManager = EquipementManager(pathEquipementDatabase)
        self.bonDeTravailManager = BonTravailManager(pathBonTravailDatabase)
        self.pieceManager = PieceManager(pathPieceDatabase)
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
        self.signalFenetreBonTravail.nouveauBonTravail.connect(self.nouveauBondeTravail)
        self.signalFenetreBonTravail.chargerBonTravail.connect(self.chargerBonTravail)
        self.signalFenetreBonTravail.chargerEquipementAPartirBon.connect(self.chargerEquipementAPartirBon)
        self.signalFenetreBonTravail.aucunBon.connect(self.aucunBonDeTravail)
        self.listeLabelCache = list()
        self.listeLabelCache.append(self.labelCacheNomTech)
        self.listeLabelCache.append(self.labelCacheDate)
        self.listeLabelCache.append(self.labelCacheTemps)
        self.listeLabelCache.append(self.labelCacheDescSit)
        self.listeLabelCache.append(self.labelCacheDescInt)
        self.listeLabelCache.append(self.labelAssistanceCache)

        self.groupeBoutonAssistance = QButtonGroup()
        self.groupeBoutonAssistance.addButton(self.checkBoxOutil)
        self.groupeBoutonAssistance.addButton(self.checkBoxPiece)
        self.groupeBoutonAssistance.addButton(self.checkBoxFormation)
        self.groupeBoutonAssistance.addButton(self.checkBoxManuel)
        self.groupeBoutonAssistance.setExclusive(False)

        for label in self.listeLabelCache:
            label.hide()

        self.listeWidget = list()
        self.listeWidget.append(self.textEditDescIntervention)
        self.listeWidget.append(self.textEditDescSituation)
        self.listeWidget.append(self.timeEditTempsEstime)
        self.listeWidget.append(self.labelEcritureBonTravail)
        self.listeWidget.append(self.dateEdit)
        #self.listeWidget.append(self.groupeBoutonAssistance)

        #self.listeWidget.append(self.comboBoxNomTech)

        self.colonneClique = None
        self.nombreClique = 0
        self.nombreBonAjoute = 0


        #Connexion des differents boutons
        self.boutonSauvegarde.clicked.connect(self.sauvegarderBonDeTravailThread)
        self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
        self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
        self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
        self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)
        self.comboBoxOuvertFerme.currentTextChanged.connect(self.signalFenetreBonTravail.editionBonTravail.emit)

        self.boutonActualiser.clicked.connect(self.chercherEquipementThread)
        self.boutonAjoutBDT.clicked.connect(self.signalFenetreBonTravail.nouveauBonTravail.emit)

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
        calendrierBDT.setGridVisible(True)
        self.dateEdit.setCalendarWidget(calendrierBDT)
        self.dateEdit.setLocale(QLocale(QLocale.French, QLocale.France))
        self.dateEdit.setDate(QDate.currentDate())

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
        self.dic_request['Id'] = self.lineEditID.text()
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
            self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"IdEquipement": self.lineEditID.text()})
            self.indiceBonDeTravail = 0
            self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
            self.listeCategoriePiece.sort()
            self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)
            self.signalFenetreBonTravail.chargerEquipement.emit()
            self.rechercherBonTravail()
        else:
            #Dans le cas ou on ne trouve pas d'equipement associe a cet ID
            self.equipementDictionnaire = None
            self.listeBonDeTravail.clear()
            self.signalFenetreBonTravail.aucunEquipement.emit()
        self.chargement.finChargement.emit()

    def aucunEquipementTrouve(self):
        self.labelEcritureCatEquip.clear()
        self.labelEcritureCentreService.clear()
        self.labelEcritureMarque.clear()
        self.labelEcritureSalle.clear()
        self.labelEcritureModele.clear()
        self.labelEcritureBonTravail.clear()
        # self.dateEdit.clear()
        # self.timeEditTempsEstime.clear()
        # self.textEditDescSituation.clear()
        # self.textEditDescIntervention.clear()
        # self.boutonAjoutBDT.setDisabled(True)
        # self.comboBoxOuvertFerme.setDisabled(True)
        # self.boutonFlecheDoubleDroite.hide()
        # self.boutonFlecheDroite.hide()
        # self.boutonFlecheGauche.hide()
        # self.boutonFlecheDoubleGauche.hide()
        # self.pushButtonValider.setDisabled(True)
        self.boutonAjoutBDT.setDisabled(True)
        self.signalFenetreBonTravail.aucunBon.emit()


    def aucunBonDeTravail(self):
        self.listeAjoutPieceReparation.clear()
        self.tableWidgetPiecesAssociees.setRowCount(0)
        self.dateEdit.clear()
        self.timeEditTempsEstime.clear()
        self.textEditDescSituation.clear()
        self.textEditDescIntervention.clear()
        self.labelEcritureBonTravail.clear()
        self.comboBoxOuvertFerme.setDisabled(True)
        self.boutonSauvegarde.setVisible(False)
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
        #if(self.equipementDictionnaire is not None):
        dictionnaireDonnees = dict()
        dictionnaireDonnees["Date"] = self.dateEdit.date().toPyDate()
        dictionnaireDonnees["TempsEstime"] = (self.timeEditTempsEstime.time().toPyTime())
        dictionnaireDonnees["DescriptionSituation"] = self.textEditDescSituation.toPlainText()
        dictionnaireDonnees["DescriptionIntervention"] = self.textEditDescIntervention.toPlainText()
        dictionnaireDonnees["NomTechnicien"] = self.comboBoxNomTech.currentText()
        if(self.comboBoxOuvertFerme.currentText() != "Non"):
            dictionnaireDonnees["EtatBDT"] = "Ferme"
        else:
            dictionnaireDonnees["EtatBDT"] = "Ouvert"
        #dictionnaireDonnees["Pieces"] = self.listeAjoutPieceReparation
        #dictionnaireDonnees["Assistance"]  = "A"


        if(self.checkBoxOutil.isChecked()):
            dictionnaireDonnees["Outils"] = 1
        else:
            dictionnaireDonnees["Outils"] = 0
        if (self.checkBoxPiece.isChecked()):
            dictionnaireDonnees["Pieces"] = 1
        else:
            dictionnaireDonnees["Pieces"] = 0
        if (self.checkBoxManuel.isChecked()):
            dictionnaireDonnees["Manuel"] = 1
        else:
            dictionnaireDonnees["Manuel"] = 0
        if (self.checkBoxFormation.isChecked()):
            dictionnaireDonnees["Formation"] = 1
        else:
            dictionnaireDonnees["Formation"] = 0
        self.obtenirChoixAssistance()


        if (len(self.listeBonDeTravail) > 0):
            idBDT = str(int(self.listeBonDeTravail[len(self.listeBonDeTravail) - 1][
                                "NumeroBonTravail"]) + 1)  # + self.nombreBonAjoute)
        else:
            idBDT = 1
        print("ID BON TRAVAIL ", idBDT)
        #Decrementation des pieces dans le stock
        if(any(self.equipementDictionnaire)):
            #On ajoute le bon de travail a un equipement existant
            if not self.modificationBon:
                dicRetour = (self.bonDeTravailManager.AjouterBonTravail(self.equipementDictionnaire["Id"], dictionnaireDonnees))
                print(dicRetour)
                if dicRetour["Reussite"]:
                    print("Reussi")
                    print("bon de travail d'id :", idBDT)
                    #dictionnaireDonnees["NumeroBonTravail"] = idBDT
                    self.listeBonDeTravail.append(dictionnaireDonnees)
                    self.nombreBonAjoute += 1
                    self.pieceManager.ChoisirPiece(self.listeAjoutPieceReparation, self.equipementDictionnaire["Id"], idBDT)
                    dictionnaireDonnees["NumeroBonTravail"] = idBDT
                    self.signalFenetreBonTravail.confirmation.emit()
            else:
                dicRetour = (self.bonDeTravailManager.ModifierBonTravail(self.equipementDictionnaire["Id"], self.listeBonDeTravail[self.indiceBonDeTravail]["NumeroBonTravail"], dictionnaireDonnees))
                if dicRetour["Reussite"]:
                    self.pieceManager.ChoisirPiece(self.listeAjoutPieceReparation, self.equipementDictionnaire["Id"] , self.listeBonDeTravail[self.indiceBonDeTravail]["NumeroBonTravail"], True)
                    print("Modification Réussie")
                    '''self.listeBonDeTravail[self.indiceBonDeTravail]["Date"] = str(dictionnaireDonnees["Date"])
                    self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"] = str(dictionnaireDonnees["TempsEstime"])
                    self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"] = dictionnaireDonnees["DescriptionSituation"]
                    self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"] = dictionnaireDonnees["DescriptionIntervention"]
                    self.listeBonDeTravail[self.indiceBonDeTravail]["NomTechnicien"] = dictionnaireDonnees["NomTechnicien"]
                    self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"] = dictionnaireDonnees["EtatBDT"]'''
                    self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"IdEquipement": self.lineEditID.text()})
        self.chargement.sauvegardeTermine.emit()

    def rechercherBonTravail(self):
        '''
            Methode permettant le chargement des informations d'un bon de travail
            Mise des informations du bon de travall dans les differents champs
             :param: None
             :return:
         '''
        print("Lancement de la recherche des bons de travail")
        self.listeBonDeTravail = self.bonDeTravailManager.RechercherBonTravail({"IdEquipement": self.lineEditID.text()})
        if(any(self.listeBonDeTravail)):
            self.chargement.rechercheTermine.emit()
        else:
            print("Aucun bon de travail")
            self.signalFenetreBonTravail.aucunBon.emit()

    def remplirBonDeTravail(self):
        #Methode permettant le remplissage des differents champs
        self.labelCacheNomTech.setText(self.comboBoxNomTech.currentText())
        self.labelCacheDate.setText(str(self.dateEdit.date().toPyDate()))
        self.labelCacheTemps.setText(str(self.timeEditTempsEstime.time().toPyTime()))
        self.labelCacheDescSit.setText(self.textEditDescSituation.toPlainText())
        self.labelCacheDescInt.setText(self.textEditDescIntervention.toPlainText())
        self.labelCacheNomTech.setText(self.comboBoxNomTech.currentText())
        self.labelAssistanceCache.setVisible(False)
        self.checkBoxManuel.setEnabled(False)
        self.checkBoxOutil.setEnabled(False)
        self.checkBoxFormation.setEnabled(False)
        self.checkBoxPiece.setEnabled(False)


    def chargerBonTravail(self):
        #Si un bon de travail a ete trouve, on remplit les differents champs associes
        self.listeAjoutPieceReparation.clear()
        self.tableWidgetPiecesAssociees.setRowCount(0)

        if(len(self.listeBonDeTravail)>0):
            self.dateEdit.setDate(datetime.datetime.strptime(self.listeBonDeTravail[self.indiceBonDeTravail]["Date"], "%Y-%m-%d"))
            self.textEditDescSituation.setPlainText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionSituation"])
            self.textEditDescSituation.wordWrapMode()
            self.textEditDescIntervention.setText(self.listeBonDeTravail[self.indiceBonDeTravail]["DescriptionIntervention"])
            self.textEditDescIntervention.wordWrapMode()
            self.boutonSauvegarde.setVisible(True)
            if(len(self.listeBonDeTravail)>1):
                self.boutonFlecheDoubleDroite.show()
                self.boutonFlecheDroite.show()
                self.boutonFlecheGauche.show()
                self.boutonFlecheDoubleGauche.show()
            self.pushButtonValider.setDisabled(False)
            if isinstance(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"], datetime.time):
                self.timeEditTempsEstime.setTime(datetime.datetime.strptime(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"], "%H-%m"))
            if self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"] == "Ouvert":
                print("ETAT BDT:", self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"])
                self.comboBoxOuvertFerme.setCurrentText("Non")
            else:
                self.comboBoxOuvertFerme.setCurrentText("Oui")
            idBDT = str(self.equipementDictionnaire["Id"]) + "-" + str(self.listeBonDeTravail[self.indiceBonDeTravail]["NumeroBonTravail"])
            print("idBDT", idBDT)
            self.labelEcritureBonTravail.setText(idBDT)
            if (self.listeBonDeTravail[self.indiceBonDeTravail]["Outils"] == 1):
                self.checkBoxOutil.setChecked(True)
            else:
                self.checkBoxOutil.setChecked(False)
            if (self.listeBonDeTravail[self.indiceBonDeTravail]["Pieces"] == 1):
                self.checkBoxPiece.setChecked(True)
            else:
                self.checkBoxPiece.setChecked(False)
            if (self.listeBonDeTravail[self.indiceBonDeTravail]["Manuel"] == 1):
                self.checkBoxManuel.setChecked(True)
            else:
                self.checkBoxManuel.setChecked(False)
            if (self.listeBonDeTravail[self.indiceBonDeTravail]["Formation"] == 1):
                self.checkBoxFormation.setChecked(True)
            else:
                self.checkBoxFormation.setChecked(False)

            idEq = str(self.equipementDictionnaire["Id"])
            idb = str(self.listeBonDeTravail[self.indiceBonDeTravail]["NumeroBonTravail"])
            self.listeAjoutPieceReparation = self.pieceManager.obtenirPieceAssocieBonTravail(idEq, idb)

            if len(self.listeAjoutPieceReparation)>0:
                self.tableWidgetPiecesAssociees.setRowCount(len(self.listeAjoutPieceReparation))
                ligne = 0
                for tuple in self.listeAjoutPieceReparation:
                    print(tuple)
                    categorie, nomPiece, nombre = tuple
                    self.tableWidgetPiecesAssociees.setItem(ligne, 0,
                                                         QTableWidgetItem(categorie))
                    self.tableWidgetPiecesAssociees.setItem(ligne, 1, QTableWidgetItem(nomPiece))
                    self.tableWidgetPiecesAssociees.setItem(ligne, 2, QTableWidgetItem(str(nombre)))
                    ligne += 1
                    self.listPieceReparationUtilise.append((categorie, nomPiece, nombre))
        else:
            self.signalFenetreBonTravail.aucunBon.emit()

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
        if(self.comboBoxOuvertFerme.currentText() == "Non"):
            self.dateEdit.setDisabled(False)
            self.timeEditTempsEstime.setDisabled(False)
            self.textEditDescSituation.setDisabled(False)
            self.textEditDescIntervention.setDisabled(False)
            self.checkBoxManuel.setEnabled(True)
            self.checkBoxOutil.setEnabled(True)
            self.checkBoxFormation.setEnabled(True)
            self.checkBoxPiece.setEnabled(True)
            self.comboBoxNomTech.setDisabled(False)
        else:
            self.dateEdit.setDisabled(True)
            self.timeEditTempsEstime.setDisabled(True)
            self.textEditDescSituation.setDisabled(True)
            self.textEditDescIntervention.setDisabled(True)
            self.checkBoxManuel.setEnabled(False)
            self.checkBoxOutil.setEnabled(False)
            self.checkBoxFormation.setEnabled(False)
            self.checkBoxPiece.setEnabled(False)
            self.comboBoxNomTech.setDisabled(True)

    def nouveauBondeTravail(self):
        for widget in self.listeWidget:
            widget.show()
            widget.clear()
        self.comboBoxOuvertFerme.setDisabled(False)
        self.comboBoxOuvertFerme.setCurrentIndex(0)
        self.lineEditID.setDisabled(False)
        self.boutonActualiser.setDisabled(True)
        self.modificationBon = False
        self.comboBoxNomTech.show()
        self.boutonAjoutBDT.hide()
        self.boutonFlecheDoubleDroite.hide()
        self.boutonFlecheDroite.hide()
        self.boutonFlecheGauche.hide()
        self.boutonFlecheDoubleGauche.hide()
        self.boutonConsultation.show()
        self.pushButtonValider.setDisabled(False)
        self.boutonSauvegarde.setVisible(True)
        print(self.equipementDictionnaire["Id"])
        self.equipementManager._AfficherBD()
        self.bonDeTravailManager._AfficherBD()
        id_bdt = (self.bonDeTravailManager._ObtenirProchainIDdeBDT(self.equipementDictionnaire["Id"]))
        print(id_bdt)
        id = str(self.equipementDictionnaire["Id"]) + "-" + str(id_bdt)
        self.labelEcritureBonTravail.setText(str(id))
        for label in self.listeLabelCache:
            label.hide()
        self.listeAjoutPieceReparation.clear()
        self.tableWidgetPiecesAssociees.setRowCount(0)
        self.checkBoxManuel.setEnabled(True)
        self.checkBoxOutil.setEnabled(True)
        self.checkBoxFormation.setEnabled(True)
        self.checkBoxPiece.setEnabled(True)
        self.checkBoxFormation.setChecked(False)
        self.checkBoxPiece.setChecked(False)
        self.checkBoxOutil.setChecked(False)
        self.checkBoxManuel.setChecked(False)
        self.timeEditTempsEstime.setDisabled(False)

        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.sort()
        self.comboBoxCategoriePiece.clear()
        self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)

    def consulterBonDeTravail(self):
        self.comboBoxNomTech.show()
        self.dateEdit.show()
        self.timeEditTempsEstime.show()
        self.boutonFlecheDoubleDroite.show()
        self.boutonFlecheDroite.show()
        self.boutonFlecheGauche.show()
        self.boutonFlecheDoubleGauche.show()
        self.boutonConsultation.show()
        self.boutonSauvegarde.show()
        self.modificationBon = True
        self.boutonAjoutBDT.show()
        self.textEditDescIntervention.show()
        self.textEditDescSituation.show()
        self.boutonConsultation.hide()
        self.comboBoxOuvertFerme.setDisabled(False)
        self.lineEditID.setDisabled(False)
        self.boutonActualiser.setDisabled(False)
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
        print(self.equipementDictionnaire["Id"])
        self.lineEditID.setText(str(self.equipementDictionnaire["Id"]))
        self.boutonAjoutBDT.setDisabled(False)
        #A modifier
        # self.rechercherBonTravail()
        # self.nouveauBondeTravail()

    def chargerEquipementAPartirBon(self):
        #Methode permettant le chargement d'un equipement
        self.labelEcritureCatEquip.setText(self.equipementDictionnaire["CategorieEquipement"])
        self.labelEcritureCentreService.setText(self.equipementDictionnaire["CentreService"])
        self.labelEcritureMarque.setText(self.equipementDictionnaire["Marque"])
        self.labelEcritureSalle.setText(self.equipementDictionnaire["Salle"])
        self.labelEcritureModele.setText(self.equipementDictionnaire["Modele"])
        self.lineEditID.setText(str(self.equipementDictionnaire["Id"]))

        self.boutonAjoutBDT.setDisabled(False)
        #A modifier
        # self.rechercherBonTravail()
        # self.nouveauBondeTravail()

    def consulterBonTravailSpecifique(self):
        self.listeCategoriePiece = list(self.pieceManager.ObtenirListeCategorie())
        self.listeCategoriePiece.sort()
        self.comboBoxCategoriePiece.clear()
        self.comboBoxCategoriePiece.addItems(self.listeCategoriePiece)
        indice = 0
        while str(self.listeBonDeTravail[indice]["NumeroBonTravail"]) != str(self.consulterBDT["NumeroBonTravail"]):
            print("id dans la liste", self.listeBonDeTravail[indice]["NumeroBonTravail"])
            print("id recupere", self.consulterBDT["NumeroBonTravail"])
            indice += 1
        self.indiceBonDeTravail = indice
        self.signalFenetreBonTravail.chargerBonTravail.emit()

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
        if (int(nombre) > 0):
            nombreSuffisant = self.pieceManager.AssezDePiece([(categorie, nomPiece, int(nombre))])
            print("NOMBRE SUFFISANT", nombreSuffisant)
            if (nombreSuffisant):
                #On ne comptabilise les pièces que s'il y a un nombre non nul
                self.tableWidgetPiecesAssociees.setRowCount(self.tableWidgetPiecesAssociees.rowCount() + 1)
                self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 0, QTableWidgetItem(categorie))
                self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 1, QTableWidgetItem(nomPiece))
                self.tableWidgetPiecesAssociees.setItem(self.tableWidgetPiecesAssociees.rowCount() - 1, 2, QTableWidgetItem((nombre)))
                self.listeAjoutPieceReparation.append((categorie, nomPiece, int(nombre)))
            else:
                #On affiche un message pour indiquer qu'il n'y a pas assez de piece
                self.signalFenetreBonTravail.pieceInsuffisant.emit()
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

    def obtenirChoixAssistance(self):
        "Methode permettan d'obtenir le(s) choix selectionne(s) parmi le groupe de check box"
        boutons = list()
        if(self.checkBoxOutil.isChecked()):
            boutons.append(self.checkBoxOutil.text())
        if (self.checkBoxPiece.isChecked()):
            boutons.append(self.checkBoxPiece.text())
        if (self.checkBoxManuel.isChecked()):
            boutons.append(self.checkBoxManuel.text())
        if (self.checkBoxFormation.isChecked()):
            boutons.append(self.checkBoxFormation.text())
        print(boutons)
        self.assistances = boutons
        return boutons


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


