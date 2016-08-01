import datetime

import yaml
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import *

from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase
from Interface.FenetresEnPython.ModificationEquipementUI import Ui_ModificationEquipement
from Interface.Stockage import Equipement

class ModificationEquipement(Ui_ModificationEquipement):
    def __init__(self, widget, equipement):
        self.setupUi(widget)
        self.equipementRecherche = equipement
        self.ajout()
        self.BoutonEnregistrer.hide()
        self.BoutonModifier.hide()

    def ajout(self):

        # Creation du groupe contenant le choix pour l'etat de service
        self.groupeBoutonEtatService = QButtonGroup()
        self.groupeBoutonEtatService.addButton(self.radioButtonEnService)
        self.groupeBoutonEtatService.addButton(self.radioButtonEnMaintenance)
        self.groupeBoutonEtatService.addButton(self.radioButtonAuRebus)

        # Creation du groupe contenant le choix pour l'etat de conservation
        self.groupeBoutonEtatConservation = QButtonGroup()
        self.groupeBoutonEtatConservation.addButton(self.radioButtonQuasiNeuf)
        self.groupeBoutonEtatConservation.addButton(self.radioButtonAcceptable)
        self.groupeBoutonEtatConservation.addButton(self.radioButtonEnFinDeVie)
        self.groupeBoutonEtatConservation.addButton(self.radioButtonDesuet)

        # Recuperation des differents elements utiles de la fenetre dans une liste
        self.listeWidgets = list()
        self.listeWidgets.append(self.comboBoxCategorie)
        self.listeWidgets.append(self.lineEditMarque)
        self.listeWidgets.append(self.lineEditModele)
        self.listeWidgets.append(self.lineEditNoDeSerie)
        self.listeWidgets.append(self.comboBoxSalle)
        self.listeWidgets.append(self.comboBoxCentreDeService)
        self.listeWidgets.append(self.dateEditDateDaquisition)
        self.listeWidgets.append(self.dateEditDateDuDernierEntretien)
        self.listeWidgets.append(self.comboBoxProvenance)
        self.listeWidgets.append(self.lineEditCodeASSET)
        self.listeWidgets.append(self.groupeBoutonEtatService)
        self.listeWidgets.append(self.groupeBoutonEtatConservation)
        self.listeWidgets.append(self.textEditCommentaires)


        #modification des calendriers
        calendrier = QCalendarWidget()
        calendrier.setStyleSheet("background :#F5F5F5;\n color: black;")
        calendrier.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.dateEditDateDaquisition.setCalendarWidget(calendrier)
        self.dateEditDateDaquisition.setLocale(QLocale(QLocale.French, QLocale.France))
        calendrierEntretien = QCalendarWidget()
        calendrierEntretien.setStyleSheet("background :#F5F5F5;\n color: black;")
        calendrierEntretien.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.dateEditDateDuDernierEntretien.setCalendarWidget(calendrierEntretien)
        self.dateEditDateDuDernierEntretien.setLocale(QLocale(QLocale.French, QLocale.France))

        # Creation de la variable equipement qui servira a l'enregistrement dans la BDD
        self.equipement = Equipement()
        self.equipement.ajoutListeMethodes()

        # Recuperation des differents attributs d''un equipement
        self.equipementManager = EquipementManager(pathEquipementDatabase, pathBonTravailDatabase)
        self.listeDonnees = list()
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger
        # récupère la liste des 'accepted keys' dans le fichier de configuration
        self.listeCleDonnees = list(self._conf['champsAcceptes-Equipement'])

        # Recuperation des differents elements des listes deroulantes
        self.listeCategorieEquipement = list(self._conf['CategorieEquipement'])
        self.listeEtatService = list(self._conf['EtatService'])
        self.listeCentreService = list(self._conf['CentreService'])
        self.listeSalle = list(self._conf['Salle'])
        self.listeProvenance = list(self._conf['Provenance'])

        self.listeCategorieEquipement.sort()
        self.listeEtatService.sort()
        self.listeCentreService.sort()
        self.listeSalle.sort()
        self.listeProvenance.sort()

        # Chargement des differentes listes deroulantes
        self.comboBoxCategorie.clear()
        self.comboBoxCategorie.addItems(self.listeCategorieEquipement)
        self.comboBoxSalle.clear()
        self.comboBoxSalle.addItems(self.listeSalle)
        self.comboBoxCentreDeService.clear()
        self.comboBoxCentreDeService.addItems(self.listeCentreService)
        self.comboBoxProvenance.clear()
        self.comboBoxProvenance.addItems(self.listeProvenance)

        # Connexion du bouton valider
        self.BoutonValider.clicked.connect(self.verificationEquipement)

        # Creation des differents labels pour la verification
        self.categorieEquipementLabel = QLabel("Ici Categorie Equipement  ")
        self.marqueLabel = QLabel("Ici marque")
        self.modeleLabel = QLabel("Ici Modele ")
        self.numSerieLabel = QLabel("Ici No. de serie ")
        self.salleLabel = QLabel("Ici Label ")
        self.centreServiceLabel = QLabel("Ici Centre de service ")
        self.dateAcquisitionLabel = QLabel("Ici Date d'acquisition ")
        self.dateEntretienLabel = QLabel("Ici Date du dernier entretien")
        self.provenanceLabel = QLabel()
        self.codeASSETLabel = QLabel()
        self.etatServiceLabel = QLabel("Ici Etat de service ")
        self.etatConservationLabel = QLabel("Ici Etat de conservation ")
        self.commentaire = QLabel("Ici commentaires ")


        # Creation du liste pour manipuler plus facilement ces differents labels
        # --ATTETION-- L'ordre est donc important
        self.listeLabel = list()
        self.listeLabel.append(self.categorieEquipementLabel)
        self.listeLabel.append(self.marqueLabel)
        self.listeLabel.append(self.modeleLabel)
        self.listeLabel.append(self.numSerieLabel)
        self.listeLabel.append(self.salleLabel)
        self.listeLabel.append(self.centreServiceLabel)
        self.listeLabel.append(self.dateAcquisitionLabel)
        self.listeLabel.append(self.dateEntretienLabel)
        self.listeLabel.append(self.provenanceLabel)
        self.listeLabel.append(self.codeASSETLabel)
        self.listeLabel.append(self.etatServiceLabel)
        self.listeLabel.append(self.etatConservationLabel)

        # Masquage des differents labels
        for label in self.listeLabel:
            self.layoutChamps.addWidget(label)
            label.hide()

        # Traitement de la partie commentaires
        self.listeLabel.append(self.commentaire)
        self.horizontalLayout_3.addWidget(self.commentaire)
        self.commentaire.hide()

        # Redefinition de la taille des champs d'entree de date
        self.dateEditDateDaquisition.setMinimumWidth(200)
        self.dateEditDateDuDernierEntretien.setMinimumWidth(200)

        self.BoutonEnregistrer.clicked.connect(self.sauvegarderEquipement)
        self.BoutonModifier.clicked.connect(self.modifierEquipement)
        # self.BoutonEnregistrer.clicked.connect(self.nouvelEquipement)

        # Selection des choix par defaut pour les radio boutons
        self.radioButtonEnService.setChecked(True)
        self.radioButtonQuasiNeuf.setChecked(True)
        # Mise en place de la modification des champs deroulants
        self.comboBoxSalle.setEditable(True)
        self.comboBoxProvenance.setEditable(True)
        self.comboBoxCentreDeService.setEditable(True)

        if self.equipementRecherche is not None:
            self.remplirEquipement()

    def obtenirEtatDeService(self, groupeBoutton):
        """Methode permettant d'obtenir le choix selectionne parmi le groupe
        de radio bouton"""
        bouton = self.groupeBoutonEtatService.checkedButton()
        self.etatDeService = bouton.text()

    def donnees(self):
        """Methode permettant la recuperation des donnees dans les differents widgets
        On parcours la liste des widgets et on recupere les differentes informations utiles
        Les informations sont recuperees de facon specifique selon le type du widget"""
        self.listeDonnees.clear()
        for widget in self.listeWidgets:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                self.listeDonnees.append(widget.text())
            elif type(widget) is QDateEdit:
                self.listeDonnees.append(widget.date().toPyDate())
                if isinstance(widget.date().toPyDate(), datetime.date):
                    print("format date correct")
                else:
                    print("probleme avec format date")
            elif type(widget) is QComboBox:
                self.listeDonnees.append(widget.currentText())
            elif type(widget) is QButtonGroup:
                bouton = widget.checkedButton()
                etatDeService = bouton.text()
                self.listeDonnees.append(etatDeService)
            else:
                self.listeDonnees.append(widget.toPlainText())

    def sauvegarderEquipement(self):
        """Methode permettant l'enregristrement de l'equipement dans la BDD"""

        # self.donnees()
        i = 0
        for donnees in self.listeDonnees:
            self.equipement.listeMethodes[i](donnees)
            i += 1
        # self.equipementManager = EquipementManager('DataBase_Equipement.json', 'DataBase_BDT.json')
        self.equipementManager.ModifierEquipement(self. equipementRecherche["ID"], self.equipement.dictionnaire)

    def verificationEquipement(self):
        """Methode affichant le recapitulatif de l'equipement"""
        if (self.verificationChamps()):
            self.donnees()
            indice = 0
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            for text in self.listeDonnees:
                if type(self.listeWidgets[indice]) is QButtonGroup:
                    for radioBouton in self.listeWidgets[indice].buttons():
                        if not radioBouton.isChecked():
                            radioBouton.hide()
                else:
                    self.listeLabel[indice].setFont(font)
                    self.listeLabel[indice].setText(str(text))
                    self.listeLabel[indice].show()
                    self.listeWidgets[indice].hide()
                indice += 1
            # self.labelId.setText(str(self.equipementManager._ObtenirProchainID()))
            self.BoutonEnregistrer.show()
            self.BoutonModifier.show()
            self.BoutonValider.hide()
        else:
            print("Champs obligatoire(s) manquant(s)")

    def modifierEquipement(self):
        """Action lors de l'appuie sur le bouton modifier
        On repasse sur l'ajout d'un equipement avec les champs modifiables"""
        indice = 0
        for text in self.listeDonnees:
            if type(self.listeWidgets[indice]) is QButtonGroup:
                for radioBouton in self.listeWidgets[indice].buttons():
                    radioBouton.show()
            else:
                self.listeLabel[indice].hide()
                self.listeWidgets[indice].show()
            indice += 1
        self.labelId.setText("")
        self.BoutonEnregistrer.hide()
        self.BoutonValider.show()
        self.BoutonModifier.hide()

    def remplirEquipement(self):
        """Methode permettant le remplissage des differents labels
         Utilisation des donnees entrees par l'utilisateur pour les labels
         """
        equipement = self.equipementRecherche
        self.labelId.setText(equipement["ID"])
        indice = 0
        for widget in self.listeWidgets:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                widget.setText(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QDateEdit:
                widget.setDate(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QComboBox:
                widget.setCurrentText(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QButtonGroup:
                for radioBouton in widget.buttons():
                    if radioBouton.text() == equipement[self.listeCleDonnees[indice]]:
                        radioBouton.setChecked(True)
            else:
                widget.setText(equipement[self.listeCleDonnees[indice]])
            indice += 1

    def verificationChamps(self):
        if (self.comboBoxCategorie.currentText() == ""):
            return False
        else:
            return True

    def nouvelEquipement(self):
        """Remet en place un formulaire vide pour l'ajout d'un equipement
            """
        indice = 0
        for text in self.listeDonnees:
            if type(self.listeWidgets[indice]) is QButtonGroup:
                for radioBouton in self.listeWidgets[indice].buttons():
                    radioBouton.show()
            else:
                self.listeLabel[indice].hide()
                self.listeWidgets[indice].show()
                if (isinstance(self.listeWidgets[indice], QLineEdit) or isinstance(self.listeWidgets[indice],
                                                                                   QTextEdit)):
                    self.listeWidgets[indice].clear()
            indice += 1
        self.labelID.setText("")
        self.BoutonEnregistrer.hide()
        self.BoutonValider.show()
        self.BoutonModifier.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modificationEquipement = QtWidgets.QWidget()
    modificationEquipementUI = ModificationEquipement(modificationEquipement, None)
    modificationEquipement.show()
    sys.exit(app.exec_())