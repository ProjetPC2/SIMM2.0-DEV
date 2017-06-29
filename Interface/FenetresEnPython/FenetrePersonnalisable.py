
from PyQt5 import QtWidgets

from Interface.FenetresEnPython.FenetrePersonnalisableUI import Ui_FenetrePersonnalisable
import yaml

'''
Cette class doit vérifier quelles fenetres ont été cochées une fois le bouton enregistrer cliqué.
Les préférences sont inscrites (overwrite) dans le fichier fichier_fenetre_personnalisable.yaml
Ensuite, dans Accueil.py, elle masque les fenetres qui ne sont pas incrites dans le fichier
'''

class FenetrePersonnalisable(Ui_FenetrePersonnalisable):

    def __init__(self, widget):
        self.setupUi(widget)
        self.boutonEnregistrer.clicked.connect(self.verifierChecked)
        self.conf_file = 'fichier_fentre_personnalisable.yaml'


    def verifierChecked(self):
    #Méthode qui permet de voir quelle box sont checked

        if (self.checkBoxAjoutEquipement.isChecked()):
            newData={'Ajout Equipement': True}
        else:
            newData = {'Ajout Equipement': False}

        if (self.checkBoxAjoutBonTravail.isChecked()):
            newData['Ajout Bon de travail'] = True
        else:
            newData['Ajout Bon de travail'] = False

        if (self.checkBoxAjoutPiece.isChecked()):
            newData['Ajout Piece'] = True
        else:
            newData['Ajout Piece'] = False

        if (self.checkBoxImprimer.isChecked()):
            newData['Imprimer'] = True
        else:
            newData['Imprimer'] = False

        if (self.checkBoxModificationEquipement.isChecked()):
            newData['Modification Equipement'] = True
        else:
            newData['Modification Equipement'] = False

        if (self.checkBoxRechercheBonTravail.isChecked()):
            newData['Recherche bon travail'] = True
        else:
            newData['Recherche bon travail'] = False

        if (self.checkBoxRechercheEquipement.isChecked()):
            newData['Recherche equipement'] = True
        else:
            newData['Recherche equipement'] = False

        if (self.checkBoxStastistiques.isChecked()):
            newData['Statistique'] = True
        else:
            newData['Statistique'] = False

        if (self.checkBoxSupportTechnique.isChecked()):
            newData['Support technique'] = True
        else:
            newData['Support technique'] = False

        with open(self.conf_file, 'w') as yaml_file:
            yaml.dump(newData, yaml_file, default_flow_style=False)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = FenetrePersonnalisable(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
