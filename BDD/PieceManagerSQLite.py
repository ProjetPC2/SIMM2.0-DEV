# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE MODIFICATION : 15 juin 2016
#
# DESCRIPTION : CLASSE BON_TRAVAIL_MANAGER
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
        self.piece_file = 'fichier_pieces.yaml'

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
        #dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            commandeSQL = "SELECT Nombre FROM Piece WHERE Categorie={0} AND NomPiece={1}".format(listeTuple[0],listeTuple[1])
            cur.execute(commandeSQL)
            indice = cur.fetchall()
            if not indice:
                commandeSQLajout = "INSERT INTO Piece VALUES({0},{1},{2})".format(listeTuple[0],listeTuple[1],listeTuple[2])
                cur.execute(commandeSQLajout)
            else:
                valeur = indice+listeTuple[2]
                commandeSQL2="UPDATE Piece SET Nombre={0} WHERE Categorie={1} AND NomPiece={2}".format(valeur,listeTuple[0],listeTuple[1])
                cur.execute(commandeSQL2)
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return dict_renvoi

#la BD ne reconnaît pas les champs entrées. Revoir le typo de la chaîne de caractère pour toutes les commdandes SQL