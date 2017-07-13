import datetime
import os
from threading import Thread

import yaml
from PyQt5 import QtWidgets
from PyQt5.QtCore import QLocale, QDate
from PyQt5.QtWidgets import *
from shutil import copyfile

from BDD.EquipementManagerSQLite import EquipementManager
from Interface.FenetresEnPython.AjoutEquipementUI import Ui_AjoutEquipement
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase, pathFichierConf
from Interface.FenetresEnPython.Signaux import Communicate
from Interface.Stockage import Equipement


class ModificationEquipement(Ui_AjoutEquipement):
    #Classe gerant la fenetre permettant la modification d'un equipement
    def __init__(self, widget, equipement):
        self.setupUi(widget)
        self.equipementRecherche = equipement
        self.BoutonEnregistrer.hide()
        self.BoutonModifier.hide()
        self.sauvegarde = Communicate()
        self.signalFenetre = Communicate()
        self.signalFenetre.signalNouvelEquipement.connect(self.nouvelEquipement)
        self.signalFenetre.signalVerificationEquipement.connect(self.verificationEquipement)
        self.signalFenetre.signalModifierEquipement.connect(self.modifierEquipement)
        self.ajout()


    def ajout(self):

        self.titreModificationEquipement.setText("Modification d\'équipement")

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
        self.equipementManager = EquipementManager(pathEquipementDatabase)
        self.listeDonnees = list()
        try:
            fichierConf = open(pathFichierConf, 'r')  # try: ouvrir le fichier et le lire
            with fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", pathFichierConf)  # définir ce qu'il faut faire pour corriger
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


        # Creation du liste pour manipuler plus facilement ces differents labels
        # --ATTETION-- L'ordre est donc important
        self.listeLabel = list()
        # self.listeLabel.append(self.labelID)
        self.listeLabel.append(self.labelCategorie)
        self.listeLabel.append(self.labelMarque)
        self.listeLabel.append(self.labelModele)
        self.listeLabel.append(self.labelNoDeSerie)
        self.listeLabel.append(self.labelSalle)
        self.listeLabel.append(self.labelCentreDeService)
        self.listeLabel.append(self.labelDateDAquisition)
        self.listeLabel.append(self.labelDateDernierEntretien)
        self.listeLabel.append(self.labelProvenance)
        self.listeLabel.append(self.labelCodeASSET)
        self.listeLabel.append(self.labelEtatDeService)
        self.listeLabel.append(self.labelEtatDeConservation)

        # Masquage des differents labels
        for label in self.listeLabel:
            label.hide()
        self.labelID.hide()

        # Traitement de la partie commentaires
        self.listeLabel.append(self.commentaire)
        self.horizontalLayout_3.addWidget(self.commentaire)
        self.commentaire.hide()

        # Redefinition de la taille des champs d'entree de date
        self.dateEditDateDaquisition.setMinimumWidth(200)
        self.dateEditDateDuDernierEntretien.setMinimumWidth(200)

         # Connexion du bouton valider
        self.BoutonValider.clicked.connect(self.signalFenetre.signalVerificationEquipement.emit)
        self.BoutonEnregistrer.clicked.connect(self.sauvegarderEquipementThread)
        self.BoutonModifier.clicked.connect(self.signalFenetre.signalModifierEquipement.emit)
        # self.BoutonEnregistrer.clicked.connect(self.nouvelEquipement)

        # Selection des choix par defaut pour les radio boutons
        self.radioButtonEnService.setChecked(True)
        self.radioButtonQuasiNeuf.setChecked(True)
        # Mise en place de la modification des champs deroulants
        self.comboBoxSalle.setEditable(True)
        self.comboBoxProvenance.setEditable(True)
        self.comboBoxCentreDeService.setEditable(True)

        self.BoutonPDF.clicked.connect(self.ouvrirPDF)
        self.fileToSave = ""
        self.filePath = ""

        if self.equipementRecherche is not None:
            self.remplirEquipement()
            # connexion du bouton de sauvegarde du pdf


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
        i = 0
        for donnees in self.listeDonnees:
            self.equipement.listeMethodes[i](donnees)
            i += 1
        self.equipement.dictionnaire["PdfPath"] = self.filePath
        self.equipementManager.ModifierEquipement(self. equipementRecherche["Id"], self.equipement.dictionnaire)
        self.sauvegarde.sauvegardeTermine.emit()

    def verificationEquipement(self):
        """Methode affichant le recapitulatif de l'equipement"""
        if (self.verificationChamps()):
            self.labelID.show()
            self.labelVide.hide()
            self.donnees()
            indice = 0
            for text in self.listeDonnees:
                if type(self.listeWidgets[indice]) is QButtonGroup:
                    for radioBouton in self.listeWidgets[indice].buttons():
                            radioBouton.hide()
                    self.listeLabel[indice].setText(str(text))
                    self.listeLabel[indice].show()
                else:
                    self.listeLabel[indice].setText(str(text))
                    self.listeLabel[indice].show()
                    self.listeWidgets[indice].hide()
                indice += 1
            self.labelID.setText(str(self.equipementRecherche["Id"]))
            self.BoutonEnregistrer.show()
            self.BoutonModifier.show()
            self.BoutonValider.hide()
            self.BoutonPDF.hide()
        else:
            print("Champs obligatoire(s) manquant(s)")

    def modifierEquipement(self):
        """Action lors de l'appuie sur le bouton modifier
        On repasse sur l'ajout d'un equipement avec les champs modifiables"""
        indice = 0
        self.labelEtatDeService.hide()
        self.labelEtatDeConservation.hide()
        self.labelVide.show()
        for text in self.listeDonnees:
            if type(self.listeWidgets[indice]) is QButtonGroup:
                for radioBouton in self.listeWidgets[indice].buttons():
                    radioBouton.show()
            else:
                self.listeLabel[indice].hide()
                self.listeWidgets[indice].show()
            indice += 1
        self.labelID.hide()
        self.BoutonEnregistrer.hide()
        self.BoutonValider.show()
        self.BoutonModifier.hide()
        self.BoutonPDF.show()


    def remplirEquipement(self):
        """Methode permettant le remplissage des differents labels
         Utilisation des donnees entrees par l'utilisateur pour les labels
         """
        equipement = self.equipementRecherche
        self.labelVide.setText(str(equipement["Id"]))
        indice = 0
        for widget in self.listeWidgets:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                widget.setText(str(equipement[self.listeCleDonnees[indice]]))
            elif type(widget) is QDateEdit:
                widget.setDate(datetime.datetime.strptime(equipement[self.listeCleDonnees[indice]] ,"%Y-%m-%d"))
            elif type(widget) is QComboBox:
                widget.setCurrentText(equipement[self.listeCleDonnees[indice]])
            elif type(widget) is QButtonGroup:
                for radioBouton in widget.buttons():
                    if radioBouton.text() == equipement[self.listeCleDonnees[indice]]:
                        radioBouton.setChecked(True)
            else:
                widget.setText(equipement[self.listeCleDonnees[indice]])
            indice += 1
        self.parsingPath(equipement["PdfPath"])



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

    def sauvegarderEquipementThread(self):
        thread = SauvergarderEquipement(self.sauvegarderEquipement)
        thread.start()

    def ouvrirPDF(self):
        filter = "PDF (*.pdf)"
        fileName = QFileDialog.getOpenFileName(None, "Open File",
                                                  os.path.expanduser("~/Desktop"),
                                                filter);
        print(fileName[0])
        self.parsingPath(fileName[0])

    def parsingPath(self, fileName):
        self.filePath = fileName
        splitFileName = self.filePath.split("/")
        self.fileToSave = splitFileName[len(splitFileName) - 1]
        print(self.fileToSave)
        self.labelPDF.setText(self.fileToSave)
        print("Sauvegarde terminee")

    def savePDF(self):
        print(self.fileToSave)
        if(self.fileToSave != ""):
            print("Saving file")
            #ATTENTION : Il faut mettre un double /
            path = "PDF//"
            path += self.fileToSave
            copyfile(self.filePath, path)
            print("Finish Saving")
        else:
            print("No selected file")

class SauvergarderEquipement(Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction = fonction


    def run(self):
        self.fonction()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modificationEquipement = QtWidgets.QWidget()
    equipement = dict({"Id":"9",
                       "CategorieEquipement":"test",
                       "Marque":"Apple",
                       "Modele":"modele",
                       "NumeroSerie":"3",
                       "Salle":"",
                       "CentreService":"5",
                       "DateAcquisition":QDate.currentDate (),
                       "DateDernierEntretien":QDate.currentDate (),
                       "Provenance":"6",
                       "CodeAsset":"6",
                       "EtatService":"ok",
                       "EtatConservation":"ok",
                       "Commentaires":"Bonjour",})
    modificationEquipementUI = ModificationEquipement(modificationEquipement, equipement)
    modificationEquipement.show()
    sys.exit(app.exec_())