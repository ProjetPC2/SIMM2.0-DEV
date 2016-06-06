"""
Dans ce fichier vous pourrez voir :
-un exemple de creation d'un widget personnalise
-l'utilisation du form layout
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class FormulaireRempli(QWidget):
    """Classe représentant les informations sur l'equipement"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        #attributs qui contiendra les diffenrts widgets
        self.widgetList = list()

        #Layout formulaire contenant les differents elements
        formulaireConteneur = QFormLayout();
        #creation de la ligne pour l'id
        idLabel = QLabel("Ici Id", self)
        #creation de la ligne pour la categorie d'equipement
        categorieEquipementLabel = QLabel("Ici Categorie Equipement  ", self)

        # creation de la ligne pour la marque de l'equipement
        marqueLabel = QLabel("Ici marque", self)

        # creation de la ligne pour le modele de l'equipement
        modeleLabel = QLabel("Ici Modele ", self)

        # creation de la ligne pour le numero de serie de l'equipement
        numSerieLabel = QLabel("Ici No. de serie ", self)

        # creation de la ligne pour la categorie d'equipement
        salleLabel = QLabel("Ici Label ", self)

        # creation de la ligne pour la categorie d'equipement
        centreServiceLabel = QLabel("Ici Centre de service ", self)

        # creation de la partie pour la date d'acquisition
        dateAcquisitionLabel = QLabel("Ici Date d'acquisition ")

        # creation de la partie pour la date du dernier entretien
        dateEntretienLabel = QLabel("Ici Date du dernier entretien")

        #creation de la partie pour la provenance
        provenanceLabel = QLabel()

        #creation de la partie pour le choix de l'etat de service
        etatServiceConteneur = QHBoxLayout()
        etatServiceLabel = QLabel("Ici Etat de service ")

        #creation de la partie pour le choix de l'etat de conservation
        etatConservationConteneur = QHBoxLayout()
        etatConservationLabel = QLabel("Ici Etat de conservation ")
        commentaire = QLabel("Ici commentaires ")
        #insertion des differents elements dans le formulaireLayout
        formulaireConteneur.insertRow(1, "<b>Id :</b>", idLabel)
        formulaireConteneur.insertRow(2, "<b>Categorie Equipement : </b>", categorieEquipementLabel)
        formulaireConteneur.insertRow(3, "<b>Marque : </b>", marqueLabel)
        formulaireConteneur.insertRow(4, "<b>Modele : </b>", modeleLabel)
        formulaireConteneur.insertRow(5, "<b>No. de serie : </b>", numSerieLabel)
        formulaireConteneur.insertRow(6, "<b>Salle : </b>", salleLabel)
        formulaireConteneur.insertRow(7, "<b>Centre de service : </b>", centreServiceLabel)
        formulaireConteneur.insertRow(8, "<b>Date d'acquisition : </b>", dateAcquisitionLabel)
        formulaireConteneur.insertRow(9, "<b>Date du dernier entretien : </b>", dateEntretienLabel)
        formulaireConteneur.insertRow(10, "<b>Provenance : </b>", provenanceLabel)
        formulaireConteneur.insertRow(10, "<b>Etat Service : </b>", etatServiceLabel)
        formulaireConteneur.insertRow(11, "<b>Etat Conservation :</b>", etatConservationLabel)
        formulaireConteneur.insertRow(12, "<b>Commentaires : </b>", commentaire)

        self.widgetList.append(idLabel)
        self.widgetList.append(categorieEquipementLabel)
        self.widgetList.append(marqueLabel)
        self.widgetList.append(modeleLabel)
        self.widgetList.append(numSerieLabel)
        self.widgetList.append(salleLabel)
        self.widgetList.append(centreServiceLabel)
        self.widgetList.append(dateAcquisitionLabel)
        self.widgetList.append(dateEntretienLabel)
        self.widgetList.append(provenanceLabel)
        self.widgetList.append(etatServiceLabel)
        self.widgetList.append(etatConservationLabel)
        self.widgetList.append(commentaire)
        #on wrap le contenur du texte dans commentaire pour que la fenetre ne s'etire pas trop en largeur
        commentaire.wordWrap()

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

    win = FormulaireRempli()
    win.setWindowTitle("Options")
    win.show()

    sys.exit(app.exec_())