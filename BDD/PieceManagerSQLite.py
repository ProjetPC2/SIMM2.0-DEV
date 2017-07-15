# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE MODIFICATION : 15 juin 2016
#
# DESCRIPTION : CLASSE Piece_MANAGER
# Permet la gestion de bons de travails dans une base de données. Ces bons de travail sont associés à des
# équipements d'une autre base de données (voir la classe EquipementManager).
# Les fonctions possibles sont : AjouterPiece, SupprimerPiece, ModificerPiece,
# RechercherPiece.
# Un fichier de configuration est nécessaire au bon fonctionnement de cette classe (fichier_conf.yaml). *À compléter
############################################################################################################

import yaml
from tinydb import *
from tinydb.operations import increment
from BDD.yamlStorage import YAMLStorage
import datetime
import os
import sqlite3 as lite


# vérifier l'ouverture du fichier de conf, fichier de BDD equipement, fichier BDD BdT avec des exceptions

class PieceManager:
    def __init__(self, pathname):
        self._pathnamePiece = pathname

        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS Piece(Categorie TEXT, NomPiece TEXT, Nombre Integer)")
            con.commit()
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()

    def AjouterPiece(self, listeTuple):
        print(listeTuple)
        dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            for tup in listeTuple:
                commandeSQL = "SELECT Nombre FROM Piece WHERE Categorie='{0}' AND NomPiece='{1}'".format(tup[0],tup[1])
                print(commandeSQL)
                cur.execute(commandeSQL)
                rows = cur.fetchall()
                if len(rows) == 0:
                    commandeSQL= "INSERT INTO Piece VALUES('{0}','{1}',{2})".format(tup[0],tup[1], tup[2])

                else:
                    valeur = rows[0][0] + tup[2]
                    commandeSQL = "UPDATE Piece SET Nombre={0} WHERE Categorie='{1}' AND NomPiece='{2}'".format(valeur,tup[0],tup[1])
                print(commandeSQL)

                cur.execute(commandeSQL)
                dict_renvoi['Reussite'] = True
                con.commit()
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return dict_renvoi

    def ChoisirPiece(self, listeTuple):
        print(listeTuple)
        dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            for tup in listeTuple:
                commandeSQL = "SELECT Nombre FROM Piece WHERE Categorie='{0}' AND NomPiece='{1}'".format(tup[0], tup[1])
                print(commandeSQL)

                cur.execute(commandeSQL)
                rows = cur.fetchall()

                if len(rows) == 0:
                    print("ERREUR PAS DE PIECE ASSOCIE")
                else:
                    nombrePiece = int(rows[0][0])
                    if(nombrePiece >= tup[2]):
                        nombreRestant = nombrePiece - tup[2]
                        commandeSQL = "UPDATE Piece SET Nombre={0} WHERE Categorie='{1}' AND NomPiece='{2}'".format(nombreRestant, tup[0], tup[1])
                        print(commandeSQL)
                        cur.execute(commandeSQL)
                        con.commit()
                    else:
                        print("Nombre  de piece insuffisante")

                    dict_renvoi['Reussite'] = True
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return dict_renvoi

    def ObtenirListeCategorie(self):
        try:
            con = lite.connect(self._pathnamePiece)
            listeCategorie = list()
            cur = con.cursor()
            commandeSQL = "SELECT DISTINCT Categorie FROM Piece"
            print(commandeSQL)

            cur.execute(commandeSQL)
            rows = cur.fetchall()

            if len(rows) == 0:
                print("ERREUR PAS DE CATEGORIE")
            else:

                for row in rows:
                    listeCategorie.append(row[0])

        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return listeCategorie


    def ObtenirListePiece(self, categorie):
        try:
            con = lite.connect(self._pathnamePiece)
            listeCategorie = list()
            cur = con.cursor()
            commandeSQL = "SELECT DISTINCT NomPiece FROM Piece WHERE Categorie ='{0}'".format(categorie)
            print(commandeSQL)

            cur.execute(commandeSQL)
            rows = cur.fetchall()

            if len(rows) == 0:
                print("ERREUR PAS DE CATEGORIE")
            else:
                for row in rows:
                    listeCategorie.append(row[0])
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return listeCategorie

    def _ActualiserPiece(self, pieces):
        try:
            if not os.path.exists(self.piece_file):  # vérifie si le fichier de configuration existe
                raise OSError
            else:
                with open(self.piece_file, 'w') as fichierPiece:  # ouvre le fichier et l'actualise
                    fichierPiece.write(yaml.dump(pieces, default_flow_style=False))
        except OSError:
            print("Could not update: ", self.piece_file)

    def _getConf(self):
        try:
            with open(self.conf_file, 'r') as fichierConf:  # try: ouvrir le fichier et le lire
                conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", self.conf_file)  # définir ce qu'il faut faire pour corriger

        return conf

    def _getPiece(self):
        try:
            with open(self.piece_file, 'r') as fichierPiece:
                piece = yaml.load(fichierPiece)
        except IOError:
            print("Could not read file: ", self.piece_file)
        return piece


    def _AfficherBD(self):
        con = lite.connect(self._pathnamePiece)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Piece")
            rows = cur.fetchall()
            print("BDD contenu")
            for row in rows:
                print(row)


#la BD ne reconnaît pas les champs entrées. Revoir le typo de la chaîne de caractère pour toutes les commdandes SQL

if __name__ == "__main__":  # Execution lorsque le fichier est lance
    # if True:
    # TESTS
    manager = PieceManager("test.db")

    data1 = ("ECG", "IRM")

    dict_request = {'DescriptionSituation': 'bris'}
    list1 = list()
    list1.append(("vis", "1", 10, ))
    list1.append(("vis", "10mm", 100, ))
    manager.AjouterPiece(list1)
    manager._AfficherBD()


    print(manager.ObtenirListeCategorie())
    print("Choix pieces")
    manager.ChoisirPiece(list1)
    manager._AfficherBD()
    print(manager.ObtenirListePiece("vis"))

    # manager.ModifierNombrePiece({"a": 4})
    # manager.AjouterNombrePiece("a", 10)
    # dic_request = {'AvantLe': datetime.date(2016, 03, 12)}
    #               'ApresLe': datetime.date(2016, 06, 10)}

    # print(manager.AjouterPiece('2', data1))                       # Ajout de 2 équipements de suite (pour tester...
    # manager.AjouterPiece(1, data2)                        # ... la vérification des champs)
    # print(manager.SupprimerPiece('1', '2'))                       # id_supp en int
    # print(len(manager.RechercherPiece(dic_request)))
    # print(manager.RechercherPiece(dict_request))
    # print(manager.ModifierPiece('2', '3', data1))                     # id_modif en int


