# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BdT3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtWidgets

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
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

        #Connexion des differents boutons
        self.boutonSauvegarde.clicked.connect(self.sauvegarderBonDeTravail)
        self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
        self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
        self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
        self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)
        self.comboBoxOuvertFerme.currentTextChanged.connect(self.editionBonDeTravail)

        self.boutonActualiser.clicked.connect(self.chercherEquipement)
        #TODO : Connexion du bouton AjoutBDT avec une methode a creer nouveauBDT
        self.boutonAjoutBDT.clicked.connect(self.nouveauBondeTravail)
        #TODO : Faire appel a la methode qui sera implementee plus bas pour masquer les differents labels et afficher les champs de saisie

        self.boutonConsultation.clicked.connect(self.consulterBonDeTravail)
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

    #TODO: Creer une methode nouveauBDT, avec comme seul argument : self
    #Cette methode fera appel a la methode pour masquer les labels et afficher les champs de saisie ainsi que l'affichage des boutons  appropries
    # Cette methode aura pour but de de vider les champs du BDT ( Description Situation, Description intervention
    # Temps estime et ID bon de travail

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


    #TODO : Creer une methode qui affiche les differents labels et qui masque les champs de saisie correspondant

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
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = BonDeTravail(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())


