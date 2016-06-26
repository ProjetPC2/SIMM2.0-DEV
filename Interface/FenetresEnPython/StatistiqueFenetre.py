"""
Dans cette exemple vous pourrez voir comment :
-Creer une fenetre avec differents composants
-Utiliser plusieurs classes pour faire une fenetre
-Relier des signaux a des actions
-Mettre a jour une fentre dynamiquement
-exemple d'utilisation des layouts pour gerer le placemenet
"""

import sys

import yaml
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *

from BDD.EquipementManager import EquipementManager


class Statistique(QWidget):
    """La classe Statistique est la classe qui est va servir a creer la fenetre principal
    Cette classe va contenir les attributs suivants :
    -Un titre
    -Une statusBar
    -un formulaire
    -un formulaire rempli
    -des options
    -un attribut de stockage
    -une liste temporaire pour le stockage des informations"""
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Création des differents éléments
        self.titre = QLabel("Statistique")
        self.titre.setFont((QFont('SansSerif', 24)))
        self.titre.setAlignment(Qt.AlignCenter)

           # Création des Boutons
        self.nombreEquipement = 10

        self.equipementManager = EquipementManager("DataBase_Equipement.json")



        #Mise en place du layout principal
        horizontalLayout = QHBoxLayout()
        etatDeConservationLayout = QVBoxLayout()
        nombreEquipementEtatConservationLabel = QLabel("<b>Nombre d'equipement par etat de conservation</b>")

        self.nombreQuasiNeuf = 3
        self.nombreAcceptable = 2
        self.nombreEnFinVie = 2
        self.desuet = 3
        self.enService = 7
        self.enMaintenance = 2
        self.auRebus = 1

        self.miseAJourDonnees()
        self.labelNombreEquipement = QLabel(("Il y a <b>%d</b> equipement") %self.nombreEquipement)
        self.quasiNeufLabel = QLabel("Quasi Neuf : %d" %self.nombreQuasiNeuf)
        self.acceptableLabel = QLabel("Acceptable : %d" %self.nombreAcceptable)
        self.enFinVieLabel = QLabel("En fin de vie : %d" %self.nombreEnFinVie)
        self.desuetLabel = QLabel("Desuet : %d" %self.desuet)


        etatDeConservationLayout.addWidget(nombreEquipementEtatConservationLabel)
        etatDeConservationLayout.addWidget(self.quasiNeufLabel)
        etatDeConservationLayout.addWidget(self.acceptableLabel)
        etatDeConservationLayout.addWidget(self.enFinVieLabel)
        etatDeConservationLayout.addWidget(self.desuetLabel)


        etatDeServiceLayout = QVBoxLayout()

        nombreEquipementEtatServiceLabel = QLabel("<b>Nombre d'equipement par etat de service</b>")
        self.enServiceLabel = QLabel("Quasi Neuf : %d" % self.enService)
        self.enMaintenanceLabel = QLabel("Acceptable : %d" % self.enMaintenance)
        self.auRebusLabel = QLabel("En fin de vie : %d" % self.auRebus)
        etatDeServiceLayout.addWidget(nombreEquipementEtatServiceLabel)
        etatDeServiceLayout.addWidget(self.enServiceLabel)
        etatDeServiceLayout.addWidget(self.enMaintenanceLabel)
        etatDeServiceLayout.addWidget(self.auRebusLabel)


        horizontalLayout.addLayout(etatDeConservationLayout)
        horizontalLayout.addLayout(etatDeServiceLayout)

        nombreEquipementProvenanceLabel = QLabel("<b>Nombre d'equipement par Provenance</b>")
        provenance = QHBoxLayout()
        provenanceLabel = QLabel("Provenance choix ")
        self.listeComboProvenance = QComboBox()
        # self.listeComboProvenance.addItem("provenance1")
        # self.listeComboProvenance.addItem("provenance2")
        # self.listeComboProvenance.addItem("provenance3")

        provenance.addWidget(provenanceLabel)
        provenance.addWidget(self.listeComboProvenance)

        self.nombreEquipementProvenance = 0
        self.nombreEquipementProvenanceChoisi = QLabel("Nombre d'equipement de cette provenance : %d" %self.nombreEquipementProvenance)

        resume = QHBoxLayout()
        resumeLabel = QLabel("<b>Resume d'inventaire par centre de Service</b>")
        self.listeComboService = QComboBox()
        self.listeComboService.addItem("service1")
        self.listeComboService.addItem("service2")
        self.listeComboService.addItem("service3")
        resume.addWidget(resumeLabel)
        resume.addWidget(self.listeComboService)

        # donnees tests sous forme d'une liste de tuple
        tableData = [
            ("Service", '21'),
            ("Chaise", '12'),
            ("Lit", '33')
        ]

        # creation d'une table widget de taille 3x2
        self.table = QTableWidget(0,2)
        # on met les titres des colonnes
        self.table.setMinimumHeight(500)
        # remplissage du tableau
        # for i, (name, color) in enumerate(tableData):
        #     # Creation des QTableWidgetItem
        #     nameItem = QTableWidgetItem(name)
        #     colorItem = QTableWidgetItem(color)
        #     # Insertion des elements
        #     self.table.setItem(i, 0, nameItem)
        #     self.table.setItem(i, 1, colorItem)
        self.table.resizeColumnToContents(0)
        self.table.resizeRowsToContents()

        # On fait en sorte que la table prend la largeur de la fenetre
        # self.table.horizontalHeader().setStretchLastSection(True)


        # Window sera le layout vertical principal qui contiendra les autres layout
        window = QVBoxLayout()
        window.addWidget(self.titre)
        window.addWidget(self.labelNombreEquipement)
        window.addLayout(horizontalLayout)
        window.addWidget(nombreEquipementProvenanceLabel)
        window.addLayout(provenance)
        window.addWidget(self.nombreEquipementProvenanceChoisi)
        window.addLayout(resume)
        window.addWidget(self.table)
        # on normalise l'espacement des differents elements de la fenetre
        window.addStretch(1)

        #Mise en place de la forme de la fenetre
        self.setLayout(window)
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

        self.listeComboProvenance.addItem("")
        self.listeComboProvenance.addItem("Tous")
        self.listeComboProvenance.addItems(self.listeProvenance)
        self.listeComboService.clear()
        self.listeComboService.addItem("")
        self.listeComboService.addItems(self.listeCentreService)

        self.table.clear()
        self.table.setHorizontalHeaderLabels(["Categorie equipement", "Quantite"])
        self.table.setWordWrap(True)
        self.table.resizeColumnToContents(0)
        self.table.resizeRowsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

        self.statsProvenance = self.equipementManager._statsNbEquipementProvenance()
        self.statsCategorie = self.equipementManager._statsNbEquipementCentreServiceCategorie()

        #TODO : a reconnecter une fois que les fichiers de l'ancienne bdd aura ete reparse
        # self.listeComboProvenance.currentTextChanged.connect(self.affichageProvenance)
        # self.listeComboService.currentTextChanged.connect(self.affichageCenreService)

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
        self.desuet = dictionnaire["Desuet"]

        print(self.nombreEquipement)

    def affichageProvenance(self):
        if(self.listeComboProvenance.currentText() is not ""):
            if(self.listeComboProvenance.currentText() == "Tous"):
                total = 0
                for value in self.statsProvenance.values():
                    total += value
                self.nombreEquipementProvenance = total
            else:
                self.nombreEquipementProvenance = self.statsProvenance[self.listeComboProvenance.currentText()]
        else:
            self.nombreEquipementProvenance = 0
        self.nombreEquipementProvenanceChoisi.setText((
            "Nombre d'equipement de cette provenance : %d" % self.nombreEquipementProvenance))

    def affichageCenreService(self):
        if(self.listeComboService.currentText() == ""):
            dictionnaireResultat = dict()
            for dictionnaire in self.statsCategorie.values():
                for cle, valeur in dictionnaire.items():
                    if cle in dictionnaireResultat:
                        dictionnaireResultat[cle] += valeur
                    else:
                        dictionnaireResultat[cle] = valeur
            self.table.setRowCount(len(dictionnaireResultat))
            ligne = 0
            for cle,valeur in dictionnaireResultat.items():
                self.table.setItem(ligne, 0, QTableWidgetItem(cle))
                self.table.setItem(ligne, 1, QTableWidgetItem(valeur))
                ligne += 1
        else:
            ligne = 0
            self.table.setRowCount(len(self.statsCategorie[self.listeComboService.currentText()]))
            for cle, valeur in self.statsCategorie[self.listeComboService.currentText()].items():
                self.table.setItem(ligne, 0, QTableWidgetItem(cle))
                self.table.setItem(ligne, 1, QTableWidgetItem(valeur))
                ligne += 1

if __name__ == "__main__": #Si le fichier est lancé tout seul

    app = QApplication(sys.argv)
    window = Statistique()
    # window.center()
    window.show()
    sys.exit(app.exec_())