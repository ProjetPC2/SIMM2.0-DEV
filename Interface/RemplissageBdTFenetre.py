import sys
import random


from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import*

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt


from qtconsole.qt import QtCore
from qtpy import QtGui

class RemplissageBdT(QWidget):
    """Classe représentant les informations sur l'equipement"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        #attributs qui contiendra les diffenrts widgets
        self.widgetList = list()

        #Layout formulaire contenant les differents elements
        formulaireConteneur = QFormLayout();
        #creation de la ligne pour l'id
        BondeTravail = QLabel("Ici Id", self)


        #creation de la partie pour le choix de l'etat de service
        etatServiceConteneur = QHBoxLayout()
        etatServiceLabel = QLabel("Ici Etat de service ")

        #insertion des differents elements dans le formulaireLayout
        formulaireConteneur.insertRow(1, "<b>Id :</b>", BondeTravail)


        self.widgetList.append(BondeTravail)

        #on wrap le contenur du texte dans commentaire pour que la fenetre ne s'etire pas trop en largeur
        #commentaire.wordWrap()

        # Layouts
        vbox = QVBoxLayout()
        vbox.addLayout(formulaireConteneur)

        # Création des variables
        self.permanent = False
        self.restart_now = False

        # Affichage de l'interface
        self.setLayout(vbox)

    def setPermanent(self, state):
        if state == Qt.Checked:
            self.permanent = True
        else:
            self.permanent = False

    def setRestart(self, state):
        self.restart_now = state

    def getPermanent(self):
        """Renvoie l'état du """
        return self.permanent

    def getRestart(self):
        return self.restart_now

if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = RemplissageBdT()
    win.setWindowTitle("Options")
    win.show()

    sys.exit(app.exec_())
