import os

import sys
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QFileDialog

def backUp():
    """ Methode permettant de copier les fichiers de la base de données
    Cette méthode va copier les fichiers dans un dossier SIMMBackUp
    Par défaut ce dossier se trouvera créer sur le bureau"""
    directory = QFileDialog.getExistingDirectory(None, 'Create Dir', os.path.expanduser("~/Desktop/"),
                                                QFileDialog.ShowDirsOnly)
    print(directory)
    systemOS = sys.platform
    directory = directory + "/SIMMBackUp"
    print(os.path.expanduser(directory))
    if systemOS == "linux":
        os.system("mkdir" + directory)
        os.system("cp DataBase_Equipement.yaml Database_BDT.yaml fichier_conf.yaml fichier_stats.yaml fichier_pieces.yaml" + os.path.expanduser(directory))
    elif systemOS == "win32":
        print("Ordinateur sous Windows")
    else:
        print("Autre OS")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    backUp()
    sys.exit(app.exec_())
   # os.system("pause")