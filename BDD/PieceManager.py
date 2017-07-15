# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE MODIFICATION : 15 juin 2016
#
# DESCRIPTION : CLASSE PIECE_MANAGER
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


# vérifier l'ouverture du fichier de conf, fichier de BDD equipement, fichier BDD BdT avec des exceptions

class PieceManager:
    def __init__(self):
        self.piece_file = 'fichier_pieces.yaml'

    def AjouterPiece(self, listeTuple):
        print(listeTuple)
        piece = self._getPiece()
        if piece['CategoriePiece'] is None:
            piece['CategoriePiece'] = dict()
        dictCategoriePiece = (
            piece['CategoriePiece'])  # récupère la liste des categories d'equipement
        for tuple in listeTuple:
            print(tuple)
            categorie, nomPiece, nombre = tuple
            if categorie not in dictCategoriePiece:
                print(categorie)
                piece["CategoriePiece"][categorie] = dict()
                print(piece['CategoriePiece'])
            print(nomPiece)

            if nomPiece not in piece['CategoriePiece'][categorie]:
                piece['CategoriePiece'][categorie][nomPiece] = nombre
            else:
                piece['CategoriePiece'][categorie][nomPiece] += nombre
        self._ActualiserPiece(piece)  # Actualisation du fichier conf

    # def AjouterNombrePiece(self, nomPiece, nombre):
    #     piece = self._getPiece()
    #     if nomPiece not in piece['QuantitePiece']:
    #         pass
    #     else:
    #         piece['QuantitePiece'][nomPiece] += nombre
    #         self._ActualiserPiece(piece)  # Actualisation du fichier conf

    # def ModifierNombrePiece(self, dictionnaire):
    #     piece = self._getPiece()
    #     for key, value in dictionnaire.items():
    #         piece['QuantitePiece'][key] -= value
    #     self._ActualiserPiece(piece)

    def ChoisirPiece(self, listeTuple):
        print(listeTuple)
        piece = self._getPiece()
        if piece['CategoriePiece'] is None:
            piece['CategoriePiece'] = dict()
        dictCategoriePiece = dict(
            piece['CategoriePiece'])  # récupère la liste des categories d'equipement
        for tuple in listeTuple:
            print(tuple)
            categorie, nomPiece, nombre = tuple
            if(piece['CategoriePiece'][categorie][nomPiece] >= nombre):
                piece['CategoriePiece'][categorie][nomPiece] -= nombre
            else:
                print("nombre de piece insuffisante")
                pass
        self._ActualiserPiece(piece)  # Actualisation du fichier conf

    def ObtenirListeCategorie(self):
        piece = self._getPiece()
        listeCategorie = list()
        if piece['CategoriePiece'] is None:
            return listeCategorie
        else:
            for key in piece['CategoriePiece']:
                listeCategorie.append(key)
            return listeCategorie

    def ObtenirListePiece(self, categorie):
        piece = self._getPiece()
        listePiece = list()
        if piece['CategoriePiece'] is None:
            return listePiece
        else:
            if categorie not in piece['CategoriePiece']:
                return listePiece
            else:
                if piece['CategoriePiece'][categorie] is None:
                    return listePiece
                else:
                    for piece in piece['CategoriePiece'][categorie]:
                        listePiece.append(piece)
                    return listePiece

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



if __name__ == "__main__":  # Execution lorsque le fichier est lance
    # if True:
    # TESTS
    manager = PieceManager()

    data1 = ("ECG", "IRM")

    dict_request = {'DescriptionSituation': 'bris'}
    list1 = list()
    list1.append(("vis", "8mm", 10, ))
    list1.append(("vis", "10mm", 100, ))
    manager.AjouterPiece(list1)
    print(manager.ObtenirListeCategorie())
    manager.ChoisirPiece(list1)
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
























