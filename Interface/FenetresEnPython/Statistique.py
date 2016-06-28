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

        self.nombreQuasiNeuf = 3
        self.nombreAcceptable = 2
        self.nombreEnFinVie = 2
        self.nombreDesuet = 3
        self.enService = 7
        self.enMaintenance = 2
        self.auRebus = 1

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
        #TODO : a reconnecter une fois que les fichiers de l'ancienne bdd aura ete reparse
        self.comboBoxProvenance.currentTextChanged.connect(self.affichageProvenance)
        self.comboBoxCentreService.currentTextChanged.connect(self.affichageCenreService)

    def center(self):
        """Methode permettant de centrer la fenetre"""
        # Nous recuperons la geometrie de la fenetre principale
        qr = self.frameGeometry()
        # Nous recuperons la definition de l'ecran et nous recuperons le point central
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())
        # self.move(qr.center)

    def closeEvent(self, event):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        #Selon le choix on fait une action precise
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def quitter(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Etes-vous sur de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # self.hide()
            # self.close()
            self.destroy()

    def afficheMessage(self, event):
        """Methode affichant une fenetre de confirmation pour l'ajout d'un equipement
        Cette fenetre va nous faire passer dans le mode consultable
        Les champs ne seront plus modifiables"""
        message = QMessageBox()
        #On met le texte en gras avec les bases <b> </b>
        message.setText("<b>Sauvegarde de l'equipement</b>")
        message.setInformativeText("Vous allez sauvegarder un nouvel equipement")
        message.setWindowTitle("Confirmation")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.buttonClicked.connect(self.confirmation)
        message.exec()

    def confirmation(self,i):
        #Methode qui va faire appel a la methode valider
        #Cette methode est appelee une fois que l'ajout d'un element a ete confirme
        if i.text() == "OK":
            self.valider()

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
        self.nombreDesuet = dictionnaire["Desuet"]

        print(self.nombreEquipement)

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


if __name__ == "__main__": #Si le fichier est lancé tout seul

    import sys

    app = QtWidgets.QApplication(sys.argv)
    statistique = QtWidgets.QWidget()
    statistiqueUI = Statistique(statistique)
    statistique.show()
    sys.exit(app.exec_())