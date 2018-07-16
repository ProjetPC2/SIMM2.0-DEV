import os
import sqlite3
import csv
import sys
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QFileDialog

from Interface.FenetresEnPython.Fichiers import pathFichierConf, pathEquipementDatabase


def backUp():
    """ Methode permettant de copier les fichiers de la base de données
    Cette méthode va copier les fichiers dans un dossier SIMMBackUp
    Par défaut ce dossier se trouvera créer sur le bureau"""
    directory = QFileDialog.getExistingDirectory(None, 'Create Dir', os.path.expanduser("~/Desktop/"),
                                                QFileDialog.ShowDirsOnly)

    print(directory)
    directory = directory + "/SIMMBackUp"
    systemOS = sys.platform
    print(os.path.expanduser(directory))

    conn = sqlite3.connect("Equipement.db")
    c = conn.cursor()

    data = c.execute("SELECT * FROM Equipement")

    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        #writer.writerows(["ID", "CategorieEquipement", "Marque", "Modele", "NumeroSerie", "Salle", "Unite", "DateAcquisition", "DateDernierEntretien", "FreqEntretien", "Provenance", "Voltage", "EtatService", "EtatConservation", "Commentaires"])
        writer.writerows(data)


    if systemOS == "linux":
        os.system("mkdir " + directory)
        os.system("cp " + pathFichierConf + " " + pathEquipementDatabase + os.path.expanduser(directory))
    elif systemOS == "win32":
        print("Ordinateur sous Windows")
        print(os.path.expanduser(directory))
        path = "\"" + os.path.expanduser(directory) + "\""
        #path = os.path.expanduser(directory)
        os.system("mkdir " + path)
        os.system("robocopy " + "./ " + path + " " + pathFichierConf + " " + pathEquipementDatabase)

    else:
        print("Autre OS")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    backUp()
    sys.exit(app.exec_())
   # os.system("pause")