# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE MODIFICATION : 15 juin 2016
#
# DESCRIPTION : CLASSE BON_TRAVAIL_MANAGER
# Permet la gestion de bons de travails dans une base de données. Ces bons de travail sont associés à des
# équipements d'une autre base de données (voir la classe EquipementManager).
# Les fonctions possibles sont : AjouterBonTravail, SupprimerBonTravail, ModificerBonTravail,
# RechercherBonTravail.
# Un fichier de configuration est nécessaire au bon fonctionnement de cette classe (fichier_conf.yaml). *À compléter
############################################################################################################

import yaml
from tinydb import *
from BDD.yamlStorage import YAMLStorage  ## RAJOUT BDD.
import os
import datetime
import copy
import sqlite3 as lite
import sys
import time


class BonTravailManager:
    def __init__(self, pathname):
        self._pathname = pathname                           # pathname de la base de données des bons de travail
        self.conf_file = 'fichier_conf.yaml'                         # nom du fichier de configuration
        self.piece_file = 'fichier_piece.yaml'
        try:
            con = lite.connect(self._pathname)
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS BonTravail(IdEquipement INTEGER, NumeroBonTravail INTEGER, DescriptionSituation TEXT,"
                + " NomTechnicien Text, Date TEXT, TempsEstime TEXT, DescriptionIntervention TEXT, EtatBDT TEXT, Assistance TEXT, "
                + " Outils INTEGER, Pieces INTEGER, Formation INTEGER, Manuel INTEGER,"
                + "FOREIGN KEY(idEquipement) REFERENCES Equipement(Id))")
            con.commit()
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()

    def AjouterBonTravail(self, id_equipement, dictio):
        conf = self._getConf()
        dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathname)
            cur = con.cursor()
            id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)
            print("ID PROCHAIN BDT", id_bdt)
            print(self._verifierChamps(dictio, conf))
            print(self._verifierDict(dictio, conf))
            if id_bdt == -1:  # Equipement non existant
                print("The equipment doesn't exist. ID :", id_equipement)

            elif self._verifierChamps(dictio, conf) and self._verifierDict(dictio, conf):  # Vérification du dictionnaire
                dictio["IdEquipement"] = str(id_equipement)
                dictio["NumeroBonTravail"] = str(id_bdt)
                print(dictio)
                commandeSQL = "INSERT INTO BonTravail(IdEquipement, NumeroBonTravail, DescriptionSituation, NomTechnicien, " \
                              + " Date, TempsEstime, DescriptionIntervention, EtatBDT, Outils, Pieces, Formation," \
                              + " Manuel  ) VALUES ('" \
                              + dictio["IdEquipement"] + "', '" + dictio["NumeroBonTravail"] + "', '"\
                              + dictio["DescriptionSituation"] + "', '" + dictio["NomTechnicien"] + "', '" + str(dictio["Date"]) \
                              + "', '" + str(dictio["TempsEstime"]) + "', '" + dictio["DescriptionIntervention"] + "', '" \
                              + dictio["EtatBDT"] + "', '" + str(dictio["Outils"]) \
                              + "', '" + str(dictio["Pieces"]) + "', '" + str(dictio["Formation"]) + "', '" + str(dictio["Manuel"]) +" ');"

                '''
                commandeSQL = "INSERT INTO BonTravail(IdEquipement, NumeroBonTravail, DescriptionSituation, NomTechnicien, " \
                              + "Date, TempEstime, DescriptionIntervention, Etat, Assistance) VALUES ('" \
                              + dictio["IdEquipement"] + "', '" + dictio["NumeroBonTravail"] + "', '"\
                              + dictio["DescriptionSituation"] + "', '" + dictio["NomTechnicien"] + "', '" + str(dictio["Date"]) \
                              + "', '" + str(dictio["TempEstime"]) + "', '" + dictio["DescriptionIntervention"] + "', '" + dictio["Etat"] + "', '" \
                              + dictio["Assistance"] + "' );"
                '''
                print(commandeSQL)
                cur.execute(commandeSQL)

                dict_renvoi['Reussite'] = True  # ajout du nouvel équipement dans la base de données
                con.commit()

        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return dict_renvoi

                #db = self._getDB()



        # Renvoyer ID de l'equipement ajoute en plus dans le dictionnaire renvoye a l'interface

    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):  # id_supp en int
        dict_renvoi = {'Reussite': False}
        # ouverture de la base des données contenant les équipements
        try:
            con = lite.connect(self._pathname)
            cur = con.cursor()
            '''cur.execute("SELECT * FROM BonTravail")

            rows = cur.fetchall()
            print("Avant suppression")
            for row in rows:
                print(row)
            print(type(id_supp))'''
            commandeSQL = "DELETE FROM BonTravail WHERE IdEquipement = {0} AND NumeroBonTravail = {1}".format(id_eq_supp, id_bdt_supp)
            cur.execute(commandeSQL)
            dict_renvoi = {'Reussite': True}
            con.commit()
            '''cur.execute("SELECT * FROM BonTravail")

            rows = cur.fetchall()
            print("Apres suppression")
            for row in rows:
                print(row)
            '''
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return dict_renvoi

    def RechercherBonTravail(self, regex_dict):

        con = lite.connect(self._pathname)
        rows = list()
        try:
            con.row_factory = lite.Row

            cur = con.cursor()
            commmand_sql = "SELECT * FROM BonTravail "
            compteur = 0
            list_data = []
            if(len(regex_dict) > 0):
                commmand_sql += "WHERE "
                for key, value in regex_dict.items():
                    compteur += 1
                    # Pour chaque champ de la recherche
                    if (key == 'IdEquipement'):
                        commmand_sql += key + "= ? "
                    else:
                        if not isinstance(value, datetime.date):  # S'il ne s'agit pas d'une date
                            commmand_sql += key + " = ?"
                        else:  # S'il s'agit d'une date
                            if key == 'ApresLe':  # Chercher après la date
                                commmand_sql +=  "Date > ? "
                            if key == 'AvantLe':  # Chercher avant la date
                                commmand_sql +=  "Date < ? "
                    list_data.append((value))

                    if (compteur < len(regex_dict)):
                        commmand_sql += " AND "

                print("Commande: ", commmand_sql)
                print("Recherche Bon Travail en cours")
                print("REGEX", regex_dict)
                cur.execute(commmand_sql, list_data)
            else:
                cur.execute(commmand_sql)
            rows = cur.fetchall()

            if(len(rows) > 0):
                print("Element trouve")
            else:
                print("Aucun element trouve")
            print(type(rows))
            for row in rows:
                dictTemp = dict()
                print("type de row ", row)
                #ATTENTION : le format de la date contient les heures
            #    print("%s %s %s" % (row["Id"], row["DateDernierEntretien"], datetime.datetime.strptime(row["DateAcquisition"],"%Y-%m-%d" )))
            #    print("%s %s %s" % (type(row["Id"]), type(row["DateDernierEntretien"]), type(datetime.datetime.strptime(row["DateAcquisition"],"%Y-%m-%d" ))))
                print(row)
            con.close()
            self._AfficherBD()

        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return rows

    def RechercherBonTravaiGenerique(self, regex_dict):

        con = lite.connect(self._pathname)
        rows = list()
        try:
            con.row_factory = lite.Row

            cur = con.cursor()
            commmand_sql = "SELECT IdEquipement, NumeroBonTravail, CategorieEquipement," \
                           " Modele, CentreService, EtatBDT, Date, DescriptionSituation FROM BonTravail INNER JOIN" \
                           " Equipement ON Equipement.Id = BonTravail.IdEquipement "
            compteur = 0
            list_data = []
            if(len(regex_dict) > 0):
                commmand_sql += "WHERE "
                for key, value in regex_dict.items():
                    compteur += 1
                    # Pour chaque champ de la recherche
                    if (key == 'IdEquipement'):
                        commmand_sql += key + "= ? "
                    else:
                        if not isinstance(value, datetime.date):  # S'il ne s'agit pas d'une date
                            commmand_sql += key + " = ?"
                        else:  # S'il s'agit d'une date
                            if key == 'ApresLe':  # Chercher après la date
                                commmand_sql +=  "Date > ? "
                            if key == 'AvantLe':  # Chercher avant la date
                                commmand_sql +=  "Date < ? "
                    list_data.append(str(value))

                    if (compteur < len(regex_dict)):
                        commmand_sql += " AND "

                print("Commande: ", commmand_sql)
                print("Recherche Bon Travail en cours")
                print("REGEX", regex_dict)
                cur.execute(commmand_sql, list_data)
            else:
                cur.execute(commmand_sql)
            rows = cur.fetchall()

            if(len(rows) > 0):
                print("Element trouve")
            else:
                print("Aucun element trouve")
            print(type(rows))
            for row in rows:
                dictTemp = dict()
                print("type de row ", row)
                #ATTENTION : le format de la date contient les heures
            #    print("%s %s %s" % (row["Id"], row["DateDernierEntretien"], datetime.datetime.strptime(row["DateAcquisition"],"%Y-%m-%d" )))
            #    print("%s %s %s" % (type(row["Id"]), type(row["DateDernierEntretien"]), type(datetime.datetime.strptime(row["DateAcquisition"],"%Y-%m-%d" ))))
                print(row)
            con.close()
            print("AFFICHAGE DE LA BDD")
            self._AfficherBD()

        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return rows

    def RechercherBonTravailRapport(self, regex_dict):

        con = lite.connect(self._pathname)
        rows = list()
        try:
            con.row_factory = lite.Row

            cur = con.cursor()
            commmand_sql = "SELECT * FROM BonTravail INNER JOIN Equipement ON Equipement.Id = BonTravail.IdEquipement "
            compteur = 0
            list_data = []
            if (len(regex_dict) > 0):
                commmand_sql += "WHERE "
                for key, value in regex_dict.items():
                    compteur += 1
                    # Pour chaque champ de la recherche
                    if (key == 'IdEquipement'):
                        commmand_sql += key + "= ? "
                    else:
                        if not isinstance(value, datetime.date):  # S'il ne s'agit pas d'une date
                            commmand_sql += key + " = ?"
                        else:  # S'il s'agit d'une date
                            if key == 'ApresLe':  # Chercher après la date
                                commmand_sql += "Date >= ? "
                            if key == 'AvantLe':  # Chercher avant la date
                                commmand_sql += "Date <= ? "
                    list_data.append(str(value))

                    if (compteur < len(regex_dict)):
                        commmand_sql += " AND "

                print("Commande: ", commmand_sql)
                print("Recherche Bon Travail en cours")
                print("REGEX", regex_dict)
                commmand_sql += " ORDER BY EtatBDT DESC, Date DESC"
                cur.execute(commmand_sql, list_data)
            else:
                cur.execute(commmand_sql)
            rows = cur.fetchall()

            if (len(rows) > 0):
                print("Element trouve")
            else:
                print("Aucun element trouve")
            print(type(rows))
            for row in rows:
                dictTemp = dict()
                print("type de row ", row)
                # ATTENTION : le format de la date contient les heures
                #    print("%s %s %s" % (row["Id"], row["DateDernierEntretien"], datetime.datetime.strptime(row["DateAcquisition"],"%Y-%m-%d" )))
                #    print("%s %s %s" % (type(row["Id"]), type(row["DateDernierEntretien"]), type(datetime.datetime.strptime(row["DateAcquisition"],"%Y-%m-%d" ))))
                print(row)
            con.close()
            self._AfficherBD()

        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()
            return rows

    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        conf = self._getConf()

        con = lite.connect(self._pathname)
        with con:
            cur = con.cursor()

            dict_renvoi = {'Reussite': False}
            commmand_sql = "UPDATE BonTravail "
            if (len(dict_modif) > 0):
                commmand_sql += "SET "
            data = []
            compteur = 0
            for key, value in dict_modif.items():
                compteur += 1
                commmand_sql += key + "=? "
                data.append(str(value))
                if(compteur < len(dict_modif)):
                    commmand_sql += ", "
            commmand_sql += " WHERE IdEquipement = ? AND NumeroBonTravail = ?"
            print("Command: ", commmand_sql)
            data.append(id_eq_modif)
            data.append(id_bdt_modif)
            print(data)
            tuple_data = tuple(data)
            print(tuple_data)
            # Verifier que tout ce qui est dans dict_modif est conforme à la forme d'un équipement et COMPLET
            if self._verifierChamps(dict_modif, conf) and self._verifierDict(dict_modif, conf):
                cur.execute(commmand_sql, tuple_data)
                dict_renvoi['Reussite'] = True
                con.commit()
        if con:
            con.close()
        return dict_renvoi


    def _AfficherBD(self):
        con = lite.connect(self._pathname)

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM BonTravail")

            rows = cur.fetchall()
            print("BDD contenu")
            for row in rows:
                print(row)

    def _ObtenirProchainIDdeBDT(self, id_equip):
        print("Fonction obtention")
        con = lite.connect(self._pathname)
        dernier_ID = 0
        with con:
            cur = con.cursor()
            commandSql = "SELECT * FROM BonTravail WHERE IdEquipement ={0}".format(id_equip)
            cur.execute(commandSql)
            rows = cur.fetchall()
            dernier_ID = len(rows)
        prochain_ID = int(dernier_ID) + 1

        return prochain_ID

    def _verifierChamps(self, dictio, conf):
        conforme = True
        listeOfLegalKeys_temp = list(
            conf['champsAcceptes-BDT'])  # Enregistrer les champs possibles à partir du fichier de configuration
        for key, value in dictio.items():  # Vérifier pour chaque champ sa présence dans dictio
            if key in listeOfLegalKeys_temp:  # Si champ présent dans champs possibles
                listeOfLegalKeys_temp.remove(key)  # Le retirer de la liste temporaire
            else:  # Sinon afficher erreur pour ce champ
                conforme = False  # Le dictionnaire n'est pas conforme
        if (not conforme) or (len(listeOfLegalKeys_temp) is not 0):
            return False
        else:
            return True

    def _verifierDict(self, dictio, conf):
        conforme = True

        # Récupérer la liste des champs auxquels on peut ajouter des valeurs
        list_champ_ajout = list(conf['BDT_ChampAjoutPermis'])
        # Récupérer la liste des champs auxquels on ne peut pas ajouter des valeurs
        list_champ_pas_ajout = list(conf['BDT_ChampAjoutNonPermis'])
        # Récupérer la liste des champs qui doivent avoir des valeurs avec un format précis
        list_champ_format_precis = list(conf['BDT_ChampFormatPrecis'])

        for key, value in dictio.items():
            if key in list_champ_ajout:  # Si le champ permet des ajouts de valeurs
                list_temp = list(conf[key])
                if value not in list_temp:  # Et que la valeur n'est pas dans la liste
                    conf[key].append(value)  # Ajouter la valeur
            elif key in list_champ_pas_ajout:  # Si le champ ne permet pas d'ajout
                list_temp = list(conf[key])
                if value not in list_temp:  # Et que la valeur n'est pas dans la liste
                    conforme = False  # Le dictionnaire n'est pas conforme
            elif key in list_champ_format_precis:  # Si le champ doit avoir une valeur avec un format précis
                if (not isinstance(value, datetime.date)) and (
                not isinstance(value, datetime.time)):  # Vérifier le format de datetime.date()
                    conforme = False

        self._ActualiserConfiguration(conf)  # Actualiser le fichier de configuration avec les nouvelles valeurs
        return conforme

    def _ActualiserConfiguration(self, conf):
        with open('fichier_conf.yaml', 'w') as fichierConf:
            fichierConf.write(yaml.dump(conf, default_flow_style=False))

    def _ActualiserPiece(self, pieces):
        try:
            if not os.path.exists(self.piece_file):
                pass  # TODO a completer pour l'ajout des piece dans le fichier
        except:
            pass

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

    def _getDB(self):
        try:
            if not os.path.exists(self._pathname):
                raise OSError("Oups nous ne trouvons plus la bdd Bon De Travail!")  # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)

        return db

    def _getEquipDB(self):
        try:
            if not os.path.exists(self._equip_pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
            else:
                db = TinyDB(self._equip_pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)

        return db



if __name__ == "__main__":  # Execution lorsque le fichier est lance
#if True:
    # TESTS
    manager = BonTravailManager('Equipement.db')

    '''data1 = {'Date': datetime.date(2016, 2, 22),
             'TempsEstime': datetime.time(2, 30),
             'DescriptionSituation': 'Vraiment brisé',
             'DescriptionIntervention': 'Blablabla-modif',
             'EtatBDT': 'Ouvert',
             'NomTechnicien': 'Kerlin',
             'Formation': 1,
             'Outils': 0,
             'Pieces': 1,
             'Manuel': 0}

    data2 = {'Date': datetime.date(2016, 2, 22),
             'TempsEstime': datetime.time(2, 30),
             'DescriptionSituation': 'Vraiment brisé',
             'DescriptionIntervention': 'Blablabla-modif',
             'EtatBDT': 'Ouvert',
             'NomTechnicien': 'Kerlin',
             'Formation': 1,
             'Outils': 0,
             'Pieces': 1,
             'Manuel': 0}

    dic_request = {'IdEquipement': '1'}

    dic_request = {'AvantLe': datetime.date(2018, 12, 12)}
    '''
    #print(manager.AjouterBonTravail('1', data1))                       # Ajout de 2 équipements de suite (pour tester...
    manager._AfficherBD()
    #manager.AjouterBonTravail(1, data2)                        # ... la vérification des champs)
    #print(manager.SupprimerBonTravail('1', '2'))                       # id_supp en int
    #print("RECHERCHE")
    #print((manager.RechercherBonTravaiGenerique({"IdEquipement" : 1})))
    #print(manager.RechercherBonTravail(dict_request))
    #print("MODIFICATION")
    #print(manager.ModifierBonTravail('1', '1', data2))                     # id_modif en int
    #manager._AfficherBD()
    #print(manager._ObtenirProchainIDdeBDT("1"))
    #print("Recherche specifique")
    #print((manager.RechercherBonTravaiGenerique({"IdEquipement": 1})))


