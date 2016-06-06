"""
Dans cette exemple vous pourrez voir comment :
-Creer une fenetre avec differents composants
-Utiliser plusieurs classes pour faire une fenetre
-Relier des signaux a des actions
-Mettre a jour une fentre dynamiquement
-exemple d'utilisation des layouts pour gerer le placemenet
"""

import sys

from PyQt5.QtCore import QDate
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Formulaire
import FormulaireRempli
import Stockage
from AbstractWindow import AbstractWindow
from BDD import EquipementManager
from BDD.EquipementManager import *

class AjouterEquipementFenetre(QMainWindow, AbstractWindow):
    """La classe AjouterEquipementFenetre est la classe qui est va servir a creer la fenetre principal
    Cette classe va contenir les attributs suivants :
    -Un titre
    -Une statusBar
    -un formulaire
    -un formulaire rempli
    -des options
    -un attribut de stockage
    -une liste temporaire pour le stockage des informations"""
    ...

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # Création des differents éléments
        self.titre = QLabel("Formulaire - Ajout d'un equipement")
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap('Images\PdC-Bouton_Ajouter.png'))
        self.titre.setFont((QFont('SansSerif', 24)))
        self.statusBar().showMessage("Ajout d'un equipement")
        #Creation des differents composants de la fenetre
        self.formulaire = Formulaire.Formulaire(self)
        self.formulaireRempli = FormulaireRempli.FormulaireRempli(self)
        self.formulaire.widgetList[0].textEdited.connect(self.miseAJourStatutBar)
        self.stockage = Stockage.Stockage()
        self.listeTemp = list()
        self.equipementManager = EquipementManager("BDD\DataBase_Equipement.json")
        # creation du menu
        menubar = self.menuBar()
        # Créations de l'action quitter dans le menu
        exit = QAction("Quitter", self)
        #Assignation d'un raccourci de sortie
        exit.setShortcut('Ctrl+Q')
        exit.triggered.connect(qApp.quit)
        #Ajout de l'element Fichier dans le menu
        fileMenu = menubar.addMenu("Fichier")
        #Ajout de l'option quitter dans la partie fichier
        fileMenu.addAction(exit)

        # Création des Boutons
        self.validerBouton = QPushButton("Valider")
        self.modifierBouton = QPushButton("Modifier")
        self.quitterBouton = QPushButton("Quitter")

        # Création du layout contenant les boutons
        buttons = QHBoxLayout()
        buttons.addWidget(self.validerBouton)
        buttons.addWidget(self.modifierBouton)
        #Masquage du bouton inutilse
        self.modifierBouton.hide()
        buttons.addWidget(self.quitterBouton)

        # bottom va etre le layout qui sera la partie basse de la fenetre
        bottom = QVBoxLayout()
        # le layout bottom va contenir les boutons de validation, modification et pour quitter
        bottom.addLayout(buttons)

        # form layout sera le layout qui va contenir les differents formulaires d'affichage
        form = QVBoxLayout()
        form.addWidget(self.formulaire)
        form.addWidget(self.formulaireRempli)
        # on masque pour l'instant le formulaire de consultation
        self.formulaireRempli.hide()

        # Window sera le layout vertical principal qui contiendra les autres layout
        window = QVBoxLayout()
        partieTitre = QHBoxLayout()
        partieTitre.addWidget(self.titre)
        partieTitre.addWidget(self.logo)
        window.addLayout(partieTitre)
        window.addLayout(form)
        window.addLayout(bottom)
        #on normalise l'espacement des differents elements de la fenetre
        window.addStretch(1)
        #Mise en place du layout principal
        centWidget = QWidget()
        centWidget.setLayout(window)

        #Connection des differents actions au click d'un bouton
        self.quitterBouton.clicked.connect(self.quitter)
        self.validerBouton.clicked.connect(self.afficheMessage)
        self.modifierBouton.clicked.connect(self.modifier)

        #Mise en place de la forme de la fenetre
        self.setCentralWidget(centWidget)
        self.setGeometry(200, 200, 300, 300)
        self.resize(1000,1000)
        self.setWindowTitle("SIMM 2.0")
        self.setWindowIcon(QIcon('Images\PC2.png'))


    def valider(self):
        """Methode valider qui va changer le contenu de la fenetre une fois l'equipement valider
        Cette methode va tout d'abord declancher une fenetre de confirmation
        Puis si la confirmation est valide, elle va mettre les informations sous forme de Qlabel
        Les informations ne seront donc plus modifiables, on passe en mode consultatble"""
        self.formulaire.hide()
        self.validerBouton.hide()
        self.formulaireRempli.show()
        self.modifierBouton.show()
        self.statusBar().showMessage("Modification d'un equipement")
        self.donnees()
        self.remplissageFormulaire()
        self.listeTemp.clear()
        self.resize(1000,1000)

    def modifier(self):
        """Methode modifier permet de passer du mode consultable au mode modifiable
        Cette methode donne la possibilite a l'utilisateur de changer les differents champs
        On retourne dans le meme version que l'ajout d'un equipement"""
        self.formulaireRempli.hide()
        self.modifierBouton.hide()
        self.formulaire.show()
        self.validerBouton.show()
        self.statusBar().showMessage("Ajout d'un equipement")

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

    def miseAJourStatutBar(self, text):
        #methode mettant a jour le texte dans la status bar
        self.statusBar().showMessage(text)

    def confirmation(self,i):
        #Methode qui va faire appel a la methode valider
        #Cette methode est appelee une fois que l'ajout d'un element a ete confirme
        if i.text() == "OK":
            self.valider()

    def donnees(self):
        """Methode permettant la recuperation des donnees dans les differents widgets
        On parcours la liste des widgets et on recupere les differentes informations utiles
        Les informations sont recuperees de facon specifique selon le type du widget"""
        numeroGroupBox = 0
        for widget in self.formulaire.widgetList:
            # self.stockage.dictionnaire
            if type(widget) is QLineEdit:
                self.listeTemp.append(widget.text())
            elif type(widget) is QDateEdit:
                self.listeTemp.append(str(widget.date().toPyDate()))
                print(widget.date().toPyDate())
                print(QDate.currentDate())
            elif type(widget) is QComboBox:
                self.listeTemp.append(widget.currentText())
                print(widget.currentText())
            elif type(widget) is QGroupBox:
                if numeroGroupBox == 0 :
                    self.listeTemp.append(self.formulaire.etatService)
                    numeroGroupBox += 1
                else:
                    self.listeTemp.append(self.formulaire.etatConservation)

            else:
                self.listeTemp.append(widget.toPlainText())
                print(widget.toPlainText())

    def remplissageFormulaire(self):
        """Methode permettant de remplir le formulaire dans le mode consultable"""

        # self.formulaireRempli.widgetList[0].setText(self.equipementManager._ObtenirProchainID())
        # i = 1
        i=0
        for text in self.listeTemp:
            self.formulaireRempli.widgetList[i].setText(text)
            i += 1


if __name__ == "__main__": #Si le fichier est lancé tout seul

    app = QApplication(sys.argv)
    window = AjouterEquipementFenetre()
    # window.center()
    window.show()
    sys.exit(app.exec_())