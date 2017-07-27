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
                "CREATE TABLE IF NOT EXISTS Piece(IdPiece INTEGER PRIMARY KEY, Categorie TEXT, NomPiece TEXT, Nombre Integer)")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS PieceUtilisee(IdEquipement INTEGER, IdBonTravail INTEGER, IdPiece INTEGER, "
                "NombreUtilise INTEGER, FOREIGN KEY(IdEquipement) REFERENCES Equipement(Id), FOREIGN KEY(idPiece) REFERENCES Piece(IdPiece))")
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
                    commandeSQL= "INSERT INTO Piece(Categorie, NomPiece, Nombre) VALUES('{0}','{1}',{2})".format(tup[0],tup[1], tup[2])
                else:
                    valeur = rows[0][0] + tup[2]
                    print(rows[0][0], tup[2])
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
            print("AJOUT")
            self._AfficherBD()
            return dict_renvoi

    def ChoisirPiece(self, listeTuple, idEquipement, idBDt, modification = False):
        print(listeTuple)
        dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            for tup in listeTuple:
                commandeSQL = "SELECT Nombre, IdPiece FROM Piece WHERE Categorie='{0}' AND NomPiece='{1}'".format(tup[0], tup[1])
                print(commandeSQL)

                cur.execute(commandeSQL)
                rows = cur.fetchall()

                if len(rows) == 0:
                    print("ERREUR PAS DE PIECE ASSOCIE")
                else:
                    nombrePiece = int(rows[0][0])
                    idPiece = rows[0][1]
                    if modification:
                        nombreUtilisee = self.rechercherNombrePieceUtilisee(idEquipement, idBDt, idPiece)
                        if (nombrePiece + nombreUtilisee >= tup[2]):
                            nombreRestant = nombrePiece - tup[2] + nombreUtilisee
                            commandeSQL = "UPDATE Piece SET Nombre={0} WHERE Categorie='{1}' AND NomPiece='{2}'".format(
                                nombreRestant, tup[0], tup[1])
                            print(commandeSQL)
                            cur.execute(commandeSQL)
                            con.commit()
                            self.selectionnerPiece(idEquipement, idBDt, idPiece, tup[2], modification)
                        else:
                            print("Nombre de piece insuffisante")

                    else:
                        if(nombrePiece >= tup[2]):
                            nombreRestant = nombrePiece - tup[2]
                            commandeSQL = "UPDATE Piece SET Nombre={0} WHERE Categorie='{1}' AND NomPiece='{2}'".format(nombreRestant, tup[0], tup[1])
                            print(commandeSQL)
                            cur.execute(commandeSQL)
                            con.commit()
                            self.selectionnerPiece(idEquipement, idBDt, idPiece, tup[2])
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
        self._AfficherBD()
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

    def ObtenirCategorie(self, categorie):
        pieces = dict()
        try:
            con = lite.connect(self._pathnamePiece)
            con.row_factory = lite.Row
            cur = con.cursor()

            commandeSQL = "SELECT NomPiece, Nombre FROM Piece WHERE Categorie ='{0}'".format(categorie)
            print(commandeSQL)

            cur.execute(commandeSQL)
            rows = cur.fetchall()

            if len(rows) == 0:
                print("ERREUR PAS DE CATEGORIE")
            else:
                for row in rows:
                    pieces[row[0]] = (row[1])
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return pieces

    def selectionnerPiece(self, idEq, id, idPiece, quantity, modification = False):
        print("METHODE SELECTIONNE PIECE")
        print(id, quantity)
        dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            commandeSQL = "SELECT NombreUtilise FROM PieceUtilisee WHERE IdBonTravail={0} AND IdPiece={1}".format(id, idPiece)
            print(commandeSQL)
            cur.execute(commandeSQL)
            rows = cur.fetchall()
            if len(rows) == 0:
                commandeSQL = "INSERT INTO PieceUtilisee VALUES({0},{1}, {2}, {3})".format(idEq, id, idPiece, quantity)
            else:
                if modification:
                    valeur = quantity
                else:
                    valeur = rows[0][0] + quantity
                commandeSQL = "UPDATE PieceUtilisee SET NombreUtilise={0} WHERE IdBonTravail={1} AND IdPiece={2} AND" \
                              " AND IdEquipement={3}".format(valeur, id, idPiece, idEq)
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

    def rechercherNombrePieceUtilisee(self, idEquipement, idBdt, idPiece):
        print("RECHERCHE",id, idPiece)
        nombrePieceUtilisee = 0
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            commandeSQL = "SELECT NombreUtilise FROM PieceUtilisee WHERE IdBonTravail={0} AND IdPiece={1 AND " \
                          "IdEquipement = {2}".format(idBdt, idPiece, idEquipement)
            print(commandeSQL)
            cur.execute(commandeSQL)
            rows = cur.fetchall()
            if len(rows) == 0:
                nombrePieceUtilisee = 0
            else:
                nombrePieceUtilisee = rows[0][0]
        except lite.Error as e:
            if con:
                con.rollback()
            print("Error %s:" % e.args[0])
        finally:
            if con:
                con.close()
            return nombrePieceUtilisee

    def obtenirPieceAssocieBonTravail(self, idEquipement, idBdT):
        print("HELLO")
        rows = list()
        self._AfficherBDPieceUtilisee()
        try:
            con = lite.connect(self._pathnamePiece)
            cur = con.cursor()
            commandeSQL = "SELECT Categorie, NomPiece, NombreUtilise FROM Piece INNER JOIN PieceUtilisee" \
                          " ON Piece.IdPiece = PieceUtilisee.IdPiece WHERE PieceUtilisee.IdBonTravail = {0}" \
                          " AND PieceUtilisee.IdEquipement = {1}".format(str(idBdT), str(idEquipement))
            print(commandeSQL)
            cur.execute(commandeSQL)
            rows = cur.fetchall()
            print(len(rows))
            for row in rows:
                print(row)

        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return rows


    def _AfficherBD(self):
        con = lite.connect(self._pathnamePiece)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Piece")
            rows = cur.fetchall()
            print("BDD contenu")
            for row in rows:
                print(row)

    def _AfficherBDPieceUtilisee(self):
        con = lite.connect(self._pathnamePiece)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM PieceUtilisee")
            rows = cur.fetchall()
            print("BDD contenu")
            for row in rows:
                print(row)


#la BD ne reconnaît pas les champs entrées. Revoir le typo de la chaîne de caractère pour toutes les commdandes SQL

if __name__ == "__main__":  # Execution lorsque le fichier est lance
    # if True:
    # TESTS
    manager = PieceManager("Equipement.db")

    '''data1 = ("ECG", "IRM")

    dict_request = {'DescriptionSituation': 'bris'}
    list1 = list()
    list1.append(("vis", "1", 100, ))
    list1.append(("vis", "10mm", 100, ))
    list2 = list()
    list2.append(("vis", "1", 1300,))
    list2.append(("vis", "10mm", 15,))

    manager.AjouterPiece(list1)
    print("AFFICHAGE DE LA BDDDD")
    manager._AfficherBD()


    print(manager.ObtenirListeCategorie())
    print("Choix pieces")
    manager.ChoisirPiece(list1, 1, '1')
    manager._AfficherBD()
    print(manager.ObtenirListePiece("vis"))

    print("PIECE UTILISEE")
    print("AVANT")
    manager._AfficherBDPieceUtilisee()
    manager.ChoisirPiece(list2, 1, '1', True)
    print("PIECE Apres")
    manager._AfficherBDPieceUtilisee()
    print("AFFICHAGE BD PIECE")
    manager._AfficherBD()
    print("OBTENTION PIECe")
    print(manager.obtenirPieceAssocieBonTravail(1, "1"))'''
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


