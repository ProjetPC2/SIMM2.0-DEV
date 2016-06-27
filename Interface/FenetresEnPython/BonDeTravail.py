# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BdT3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets

from BDD.BonTravailManager import BonTravailManager
from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.BonDeTravailUI import Ui_BonDeTravail


class BonDeTravail(Ui_BonDeTravail):
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutBonDeTravail()

    def ajoutBonDeTravail(self):

        self.labelEcritureBonTravail.setText("")
        #Connexion de l'appuie de la touche entree
        self.lineEditID.returnPressed.connect(self.chercherEquipement)

        #Creation des differents elements utiles pour la sauvegarde
        self.equipementManager = EquipementManager('DataBase_Equipement.json')
        self.bonDeTravailManager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')
        self.equipementDictionnaire = None
        self.listeBonDeTravail = list()
        self.indiceBonDeTravail = 0

        #Connexion des differents boutons
        self.boutonSauvegarde.clicked.connect(self.sauvegarderBonDeTravail)
        self.boutonFlecheGauche.clicked.connect(self.bonTravailPrecedent)
        self.boutonFlecheDroite.clicked.connect(self.bonTravailSuivant)
        self.boutonFlecheDoubleDroite.clicked.connect(self.bonTravailDernier)
        self.boutonFlecheDoubleGauche.clicked.connect(self.bonTravailPremier)
        self.comboBoxOuvertFerme.currentTextChanged.connect(self.editionBonDeTravail)
        #TODO : Connexion du bouton d'actualisation au clique pour lancer la recherche
        #TODO : Connexion du bouton AjoutBDT avec une methode a creer nouveauBDT

        #TODO : Faire appel a la methode qui sera implementee plus bas pour masquer les differents labels et afficher les champs de saisie

    def chercherEquipement(self):
        '''
            Recuperation de l'equipement associe a l'ID dans le cas ou il existe
            Affichage des informations de l'equipement dans les champs existants
            Recuperation des bons de travail associes a cet equipement
            :param: None
            :return:
        '''
        #On fait la requete a la BDD
        print("recherche equipement")
        dic_request = dict()
        dic_request['ID'] = self.lineEditID.text()
        listeTrouve = self.equipementManager.RechercherEquipement(dic_request)
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
        else:
            #Dans le cas ou on ne trouve pas d'equipement associe a cet ID
            self.equipementDictionnaire = None
            self.labelEcritureCatEquip.setText("")
            self.labelEcritureCentreService.setText("")
            self.labelEcritureMarque.setText("")
            self.labelEcritureSalle.setText("")
            self.labelEcritureModele.setText("")


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
            dictionnaireDonnees["TempsEstime"] = str(self.timeEditTempsEstime.time().toPyTime())
            dictionnaireDonnees["DescriptionSituation"] = self.textEditDescSituation.toPlainText()
            dictionnaireDonnees["DescriptionIntervention"] = self.textEditDescIntervention.toPlainText()
            if(self.comboBoxOuvertFerme.currentText() != "Ouvert"):
                dictionnaireDonnees["EtatBDT"] = "Ferme"
            else:
                self.comboBoxOuvertFerme.currentText()
            if(any(self.equipementDictionnaire)):
                #On ajoute le bon de travail a un equipement existant
                self.bonDeTravailManager.AjouterBonTravail(self.equipementDictionnaire["ID"], dictionnaireDonnees)

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
            # self.timeEditTempsEstime.setTime(self.listeBonDeTravail[self.indiceBonDeTravail]["TempsEstime"])
            if self.listeBonDeTravail[self.indiceBonDeTravail]["EtatBDT"] != "Ouvert":
                self.comboBoxOuvertFerme.setCurrentText("Fermé")
            idBDT = str(self.equipementDictionnaire["ID"]) + "-" + str(self.indiceBonDeTravail + 1)
            self.labelEcritureBonTravail.setText(idBDT)

    #TODO : creer une methode similaire a chargerBonDeTravail qui va s'occuper de mettre les bonnes informations dans les labels "Ce que j'ai ecrit"
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

    #TODO : Creer une methode qui masque les differents labels "Ce que j'ai ecrit", et les cinq boutons(sauf la consultation) et qui affiche les champs de saisie correspondant et le bouton de consultation


    #TODO : Creer une methode qui affiche les differents labels et les cinqs boutons et qui masque les champs de saisie correspondant ainsi que le bouton de consultation
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = BonDeTravail(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())


