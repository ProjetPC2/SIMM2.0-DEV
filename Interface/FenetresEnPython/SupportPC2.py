from PyQt5 import QtWidgets

from BDD.EquipementManager import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase, pathBonTravailDatabase
from Interface.FenetresEnPython.SupportPC2UI import Ui_SupportPC2


class SupportPC2(Ui_SupportPC2):
    #Classe permettant la gestion de la fenetre support
    def __init__(self, widget):
        self.setupUi(widget)
        self.ajoutSupport()

    def ajoutSupport(self):
        self.boutonRinitialiserStatistiques.clicked.connect(self.recalculerStatistique)

    def recalculerStatistique(self):
        self.equipementManager = EquipementManager(pathEquipementDatabase, pathBonTravailDatabase)
        self.equipementManager._recalculStats()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = SupportPC2(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
