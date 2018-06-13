# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE  MODIFICATION : 15 juin 2016
#
# DESCRIPTION : CLASSE EQUIPEMENT_MANAGER
# Permet la gestion d'une base de données d'Équipements à partir de dictionnaires.
# Les fonctions possibles sont : AjouterEquipement, SupprimerEquipement, ModificerEquipement,
# RechercherEquipement.
# Un fichier de configuration est nécessaire au bon fonctionnement de cette classe (fichier_conf.yaml). *À compléter
############################################################################################################

# Ajouter fonction ActualiserConfiguration qui ecrit dans le fichier de configuration la configuration actualisee
# Cette fonction devra etre appelee apres chaque fonction suivante :
# AjouterEquipement
# SupprimerEquipement
# ModifierEquipement
# pour etre surs que la configuration est toujours maintenu a jour

# Pour les fonctions qui dialoguent avec l'interface, renvoyer un dictionnaire
# avec le champ Reussite a True ou False selon la reussite de la fonction
# - Ajouter équipement
# - Supprimer équipement
# - Modifier équipement

import yaml
from tinydb import *
from BDD.yamlStorage import YAMLStorage  ## RAJOUT BDD.
import os
import datetime
import copy
import sqlite3 as lite
import sys
import time


class EquipementManager:
    def __init__(self, pathname):
        self._pathnameEQ = pathname  # pathname de la base de données des équipements
        self.conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        self.stats_file = 'fichier_stats.yaml'

        try:
            con = lite.connect(self._pathnameEQ)
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS Equipement(Id INTEGER PRIMARY KEY, CategorieEquipement TEXT, Marque TEXT, Modele TEXT, "
                + " NumeroSerie TEXT, Salle TEXT, CentreService TEXT, DateAcquisition TEXT, DateDernierEntretien TEXT, FreqEntretien INTEGER "
                + " Provenance TEXT, CodeAsset TEXT, EtatService TEXT, EtatConservation TEXT, Commentaires TEXT, PdfPath TEXT)")
        except lite.Error as e:
            if con:
                con.rollback()

            print("Error %s:" % e.args[0])

        finally:

            if con:
                con.close()

    def AjouterEquipement(self, dictio):
        conf = self._getConf()
        stats = self._getStats()
        dict_renvoi = {'Reussite': False}
        try:
            con = lite.connect(self._pathnameEQ)
            cur = con.cursor()
            if self._verifierChamps(dictio, conf) and self._verifierDict(dictio, conf,stats):  # ARRANGER FONCTION AVANT
                '''commandeSQL = "INSERT INTO Equipement(CategorieEquipement, Marque, Modele, NumeroSerie, Salle, CentreService," \
                              + " Provenance, CodeAsset, EtatService, EtatConservation,"\
                              + " Commentaires ) VALUES ('" + dictio["CategorieEquipement"] + "', '" + dictio["Marque"] + "', '"\
                              + dictio["Modele"] + "', '" + dictio["NumeroSerie"] + "', '" + dictio["Salle"] + "', '" + dictio["CentreService"]\
                              + "', '" + dictio["Provenance"] + "', '" + dictio["CodeAsset"] + "', '" + dictio["EtatService"] + "', '" + dictio["EtatConservation"]\
                              + "', '" + dictio["Commentaires"] + "' );"
                '''
                '''commandeSQL = "INSERT INTO Equipement(CategorieEquipement, Marque, Modele, NumeroSerie, Salle, CentreService, " \
                              + "DateAcquisition, DateDernierEntretien, FreqEntretien, Provenance, CodeAsset, EtatService, EtatConservation," \
                              + " Commentaires, PdfPath)" \
                              + " VALUES ('" + dictio["CategorieEquipement"]  \
                              + "', '" + dictio["Marque"] + "', '" + dictio["Modele"] + "', '" + dictio["NumeroSerie"] \
                              + "', '" + dictio["Salle"] + "', '" + dictio["CentreService"] + "', '" + str(dictio["DateAcquisition"]) \
                              + "', '" + str(dictio["DateDernierEntretien"]) + "', '" + dictio["FreqEntretien"] + "', '" + dictio["Provenance"] \
                              + "', '" + dictio["CodeAsset"] + "', '" + dictio["EtatService"] + "', '" + dictio["EtatConservation"] \
                              + "', '" + dictio["Commentaires"] + "', '" + dictio["PdfPath"] + "');"
                '''
                commandeSQL = "INSERT INTO Equipement(CategorieEquipement, Marque, Modele, NumeroSerie, Salle, CentreService, " \
                              + "DateAcquisition, DateDernierEntretien, FreqEntretien, Provenance, CodeAsset, EtatService, EtatConservation," \
                              + " Commentaires, PdfPath) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                tupleData = (dictio["CategorieEquipement"], dictio["Marque"], dictio["Modele"], dictio["NumeroSerie"], dictio["Salle"], dictio["CentreService"],
                             str(dictio["DateAcquisition"]), str(dictio["DateDernierEntretien"]), dictio["FreqEntretien"], dictio["Provenance"], dictio["CodeAsset"], dictio["EtatService"],
                             dictio["EtatConservation"], dictio["Commentaires"], dictio["PdfPath"])
                cur.execute(commandeSQL, tupleData)

                dict_renvoi['Reussite'] = True  # ajout du nouvel équipement dans la base de données
                con.commit()
                self._AfficherBD()
                self._miseAJourStats(ancien_dict=None, nouveau_dict=dictio, stats_dict=stats)
                self._ActualiserConfiguration(conf)

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

    def SupprimerEquipement(self, id_supp):  # id_supp en int
        #stats = self._getStats()

        dict_renvoi = {'Reussite': False}
        # ouverture de la base des données contenant les équipements
        try:
            con = lite.connect(self._pathnameEQ)
            cur = con.cursor()
            '''cur.execute("SELECT * FROM Equipement")

            rows = cur.fetchall()
            print("Avant suppression")
            for row in rows:
                print(row)
            print(type(id_supp))'''
            commandeSQL = "DELETE FROM Equipement WHERE Id = %d " %id_supp
            cur.execute(commandeSQL)
            dict_renvoi = {'Reussite': True}
            con.commit()
            '''cur.execute("SELECT * FROM Equipement")

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

    def RechercherEquipement(self, regex_dict):

        con = lite.connect(self._pathnameEQ)
        rows = list()
        try:
            con.row_factory = lite.Row

            cur = con.cursor()
            commmand_sql = "SELECT * FROM Equipement "
            compteur = 0
            if(len(regex_dict) > 0):
                commmand_sql += "WHERE "
                for key, value in regex_dict.items():
                    compteur += 1
                    '''if(key == "Id"):
                        try:
                            id = int(regex_dict["Id"])
                            regex_dict["Id"] = id
                        except ValueError:
                            print("Conversion impossible")
                    '''
                    commmand_sql += key + "=:" + key
                    if (compteur < len(regex_dict)):
                        commmand_sql += " AND "

                print("Commande: ", commmand_sql)
                print("Recherche d'equipement en cours")
                print("REGEX", regex_dict)
                cur.execute(commmand_sql, regex_dict)
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
                print("OHEQJOQIJD")
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

    def ModifierEquipement(self, id_modif, dict_modif):
        conf = self._getConf()
        stats = self._getStats()

        con = lite.connect(self._pathnameEQ)
        with con:
            cur = con.cursor()

            #commande_sql1 = "Select * FROM Equipement WHERE Id = %d " %id_modif
            #cur.execute(commande_sql1)
            #ancien_dict = cur.fetchall()
            # Il suffirait de rendre la variable ancien_dict dans le même format de Tuple que dict_modif
            #self._miseAJourStats(ancien_dict=ancien_dict, nouveau_dict=dict_modif, stats_dict=stats)

            dict_renvoi = {'Reussite': False}
            commmand_sql = "UPDATE Equipement "
            if (len(dict_modif) > 0):
                commmand_sql += "SET "
            data = []
            compteur = 0
            for key, value in dict_modif.items():
                compteur += 1
                commmand_sql += key + "=? "
                data.append(value)
                if(compteur < len(dict_modif)):
                    commmand_sql += ", "
            commmand_sql += " WHERE Id = ?"
            print("Command: ", commmand_sql)
            data.append(id_modif)
            tuple_data = tuple(data)
            # Verifier que tout ce qui est dans dict_modif est conforme à la forme d'un équipement et COMPLET
            if self._verifierChamps(dict_modif, conf) and self._verifierDict(dict_modif, conf, stats):
                cur.execute(commmand_sql, tuple_data)
                print(commmand_sql, tuple_data)
                dict_renvoi['Reussite'] = True
                con.commit()
        if con:
            con.close()
        return dict_renvoi

    def MiseAJourDateEquipement(self, id, date):
        conf = self._getConf()
        stats = self._getStats()

        con = lite.connect(self._pathnameEQ)
        with con:
            cur = con.cursor()

            # commande_sql1 = "Select * FROM Equipement WHERE Id = %d " %id_modif
            # cur.execute(commande_sql1)
            # ancien_dict = cur.fetchall()
            # Il suffirait de rendre la variable ancien_dict dans le même format de Tuple que dict_modif
            # self._miseAJourStats(ancien_dict=ancien_dict, nouveau_dict=dict_modif, stats_dict=stats)
            command_sql = "SELECT DateDernierEntretien FROM Equipement WHERE Id = {0}".format(id)
            cur.execute(command_sql)
            rows = cur.fetchall()
            print("SELECTION,", rows)


            command_sql = "UPDATE Equipement SET DateDernierEntretien = '{0}'".format(date)
            command_sql += " WHERE Id = {0}".format(id)
            print("Command: ", command_sql)
            cur.execute(command_sql)
            con.commit()
        if con:
            con.close()

    def _AfficherBD(self):
        con = lite.connect(self._pathnameEQ)

        with con:
            con.row_factory = lite.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM Equipement")

            rows = cur.fetchall()
            print("BDD contenu")
            for row in rows:
                print(row)

    def _ObtenirProchainID(self):
        con = lite.connect(self._pathnameEQ)
        dernier_ID = 0
        with con:
            cur = con.cursor()
            cur.execute("SELECT * From Equipement")

            rows = cur.fetchall()
            dernier_ID = len(rows)

        prochain_ID = int(dernier_ID) + 1

        return prochain_ID

    def _verifierChamps(self, dictio, conf):
        conforme = True
        list_accepted_key_temp = list(
            conf['champsAcceptes-Equipement'])  # récupère la liste des 'accepted keys' dans le fichier de configuration
        for key, value in dictio.items():
            if key in list_accepted_key_temp:
                list_accepted_key_temp.remove(key)  # retire la clée du dictionnaire si elle est présente
            else:
                conforme = False  # si on rencontre une clée non-attendue, le dictionnaire n'est pas conforme
        if (not conforme) or (len(
                list_accepted_key_temp) != 0):  # on renvoit Faux si la liste n'est pas vide (tous les champs attendus ne
            return False  # sont pas présents) ou si on a un champ en trop
        else:
            return True

    # Deux étapes :
    # Étape 1: Vérifier que tous les champs attendus sont là
    # Étape 2: Vérifier qu'il n'y a pas un champ non attendu qui est là
    # Verifier si les valeurs des champs sont dans la configuration, si non ajouter la nouvelle valeur au dictionnaire
    def _verifierDict(self, dictio, conf, stats):
        # stats = self._getStats()

        conforme = True
        # récupère la liste des champs auxquels on peut ajouter des valeurs
        list_champ_ajout = list(conf['Equipement_ChampAjoutPermis'])
        # récupère la liste des champs auxquels on ne peut pas ajouter des valeurs
        list_champ_pas_ajout = list(conf['Equipement_ChampAjoutNonPermis'])
        # récupère la liste des champs qui doivent avoir un format précis
        list_champ_format_precis = list(conf['Equipement_ChampFormatPrecis'])
        # récupère la liste des champs qui doivent être ajoutés au fichier de stats
        list_champ_fichier_stat = list(conf['StatsAjoutFichier'])
        for key, value in dictio.items():  # parcourir le dictionnaire
            # print(key,value)
            if key in list_champ_ajout:  # à la recherche d'un champ que l'on peut ajouter des valeurs
                list_temp = list(conf[key])  # si la valeur recue n'est pas dans la le fichier de conf
                if value not in list_temp:  # on l'ajoute
                    conf[key].append(value)
            elif key in list_champ_pas_ajout:  # on regarde si la key fait partie des champs dont l'ajout de valeur n'est pas permis
                list_temp = list(conf[key])
                if value not in list_temp:  # si la valeur du dictio ne fait pas partie de la liste non modifiable, on renvoie false
                    conforme = False
            elif key in list_champ_format_precis:
                if not isinstance(value, datetime.date):  # PB: spécifique aux instances datetime.date...
                    conforme = False
            if key in list_champ_fichier_stat:  # vérifie si clée fait partie des champs qui modifient le fichier de stats
                if (key == 'Provenance') and (
                            value not in stats['nbEquipementProvenance']):  # ajoute la provenance au fichier de stats
                    stats['nbEquipementProvenance'][value] = 0
                if key == 'CategorieEquipement':
                    if dictio['CentreService'] not in stats[
                        'nbEquipementCentreService']:  # vérifie si le centre de service associé à l'éq. est dans le fichier de stats
                        stats['nbEquipementCentreService'][
                            dictio['CentreService']] = dict()  # si non, ajout du centre de service
                    if value not in stats['nbEquipementCentreService'][
                        dictio['CentreService']]:  # vérifie si l'équipement est dans le centre de service associé
                        stats['nbEquipementCentreService'][dictio['CentreService']][
                            value] = 0  # si non, ajout de l'éq. dans le centre de service associé
        self._ActualiserConfiguration(
            conf)  # actualise le fichier de configuration et de stats pour qu'il contienne la nouvelle entrée
        self._ActualiserStats(stats)
        return conforme  # retourne un booléen qui indique si le dictionnaire est conforme ou non

    def _ActualiserConfiguration(self, conf):
        try:
            if not os.path.exists(self.conf_file):  # vérifie si le fichier de configuration existe
                raise OSError
            else:
                with open(self.conf_file, 'w') as fichierConf:  # ouvre le fichier et l'actualise
                    fichierConf.write(yaml.dump(conf, default_flow_style=False))
        except OSError:
            print("Could not update: ", self.conf_file)

    # Cette méthode renvoie le nombre d'équipements contenus dans la base de données
    def _statsNbTotalEquipement(self):
        con = lite.connect(self._pathnameEQ)
        dernier_ID = 0
        with con:
            cur = con.cursor()
            print(type(cur.lastrowid))
            cur.execute("SELECT COUNT(*) From Equipement")

            rows = cur.fetchall()

        print(rows[0][0])
        return rows[0][0]

    # Cette méthode renvoie un dictionnaire avec comme clées les trois états de service possibles et comme valeur le
    # nombre d'équipements par état de service
    # key: {'En service', 'En maintenance', 'Au rebut'}
    def _statsNbEquipementEtatService(self):
        con = lite.connect(self._pathnameEQ)
        dernier_ID = 0
        with con:
            cur = con.cursor()
            print(type(cur.lastrowid))
            cur.execute("SELECT DISTINCT EtatService From Equipement")
            rows = cur.fetchall()
            conf = self._getConf()
            listeEtatService = conf["EtatService"]
            dictEtatService =  dict()
            for etatService in listeEtatService:
                commandeSQL = "SELECT count(*) FROM Equipement WHERE EtatService = '{0}'".format(etatService)
                print(commandeSQL)
                cur.execute(commandeSQL)
                rows = cur.fetchall()
                dictEtatService[etatService] = rows[0][0]
                print(etatService)
            return dictEtatService

    # Cette méthode renvoie un dictionnaire avec comme clées les quatre états de conservation possibles et comme valeur le
    # nombre d'équipements par état de conservation
    # key: {'Quasi neuf', 'Acceptable', 'En fin de vie', 'Desuet'}
    def _statsNbEquipementEtatConservation(self):
        con = lite.connect(self._pathnameEQ)
        with con:
            cur = con.cursor()
            print(type(cur.lastrowid))
            cur.execute("SELECT DISTINCT EtatConservation From Equipement")
            rows = cur.fetchall()
            conf = self._getConf()
            listeEtatConservation = conf["EtatConservation"]
            dictEtatConservation = dict()
            for etatConservation in listeEtatConservation:
                commandeSQL = "SELECT count(*) FROM Equipement WHERE EtatConservation = '{0}'".format(etatConservation)
                print(commandeSQL)
                cur.execute(commandeSQL)
                rows = cur.fetchall()
                dictEtatConservation[etatConservation] = rows[0][0]
                print(etatConservation)
            return dictEtatConservation

    # Cette méthode renvoie un dictionnaire avec comme clées les provenance possibles et comme valeur le
    # nombre d'équipements par provenance
    def _statsNbEquipementProvenance(self):
        con = lite.connect(self._pathnameEQ)
        with con:
            cur = con.cursor()
            print(type(cur.lastrowid))
            cur.execute("SELECT DISTINCT Provenance From Equipement")
            rows = cur.fetchall()
            conf = self._getConf()
            listeProvenance = conf["Provenance"]
            dictProvenance = dict()
            for provenance in listeProvenance:
                commandeSQL = "SELECT count(*) FROM Equipement WHERE Provenance = '{0}'".format(provenance)
                print(commandeSQL)
                cur.execute(commandeSQL)
                rows = cur.fetchall()
                dictProvenance[provenance] = rows[0][0]
                print(provenance)
            return dictProvenance

    # Cette méthode renvoie un dictionnaire à deux niveaux. Le premier niveau a comme clée les différents centres de
    # de service ('CentreService') qui se trouvent dans le fichier de configuration. Dans le champs des données pour ces clées,
    # on retrouve un dictionnaire (2e niveau) qui lui a comme clée les catégories d'équipements ('CategorieEquipement') que l'on
    # retrouve dans le fichier de configuration. Il est à noter que lorsqu'un centre de service ne possède pas d'équipements
    # d'un type X (ex. IRM), le champ contenant la clée X et la valeur 0 au deuxième niveau est retiré du dictionnaire.
    def _statsNbEquipementCentreServiceCategorie(self):
        stats = self._getStats()

        dict_renvoi = dict()
        con = lite.connect(self._pathnameEQ)
        with con:
            cur = con.cursor()
            cur.execute("SELECT DISTINCT CentreService From Equipement")
            rows = cur.fetchall()
            conf = self._getConf()
            listeCentreService = list()
            for row in rows:
                listeCentreService.append(row[0])
                dict_renvoi[row[0]] = dict()
            print(len(rows))
            print("Liste centre ",listeCentreService)
            listeCategorieEquipemement = conf["CategorieEquipement"]
            for centreService in listeCentreService:
                for categorieEquipement in listeCategorieEquipemement:
                    commandeSQL = 'SELECT count(*) FROM Equipement WHERE CentreService = "{0}" AND CategorieEquipement = "{1}"'.format(centreService, categorieEquipement)
                    print(commandeSQL)
                    cur.execute(commandeSQL)
                    rows = cur.fetchall()
                    if rows[0][0] > 0:
                        dict_renvoi[centreService][categorieEquipement] = rows[0][0]
            print(dict_renvoi)
            return dict_renvoi


    # Cette méthode permet de mettre à jour self._stats pour refléter les changements à la base de données lors
    # de l'ajout, de la suppression ou de la modification d'un équipement. Il met les champs à jour dans la variable globale
    # de la classe EquipementManager:_stats. L'utilisateur doit tout de même faire appel à la fonction _ActualiserStats pour mettre à
    # jour le fichier contenant les statistiques (fichier_stats.yaml)
    def _miseAJourStats(self, ancien_dict, nouveau_dict, stats_dict):
        if ancien_dict is None and nouveau_dict is not None:  # cas où on ajoute un equipement
            print('cas de ajout')
            stats_dict['nbEquipement'] += 1
            stats_dict['nbEquipementEtatConservation'][nouveau_dict['EtatConservation']] += 1
            stats_dict['nbEquipementEtatService'][nouveau_dict['EtatService']] += 1
            stats_dict['nbEquipementCentreService'][nouveau_dict['CentreService']][
                nouveau_dict['CategorieEquipement']] += 1
            stats_dict['nbEquipementProvenance'][nouveau_dict['Provenance']] += 1
        elif nouveau_dict is None and ancien_dict is not None:  # cas où on supprime un équipement
            print('cas de la suppression')
            stats_dict['nbEquipement'] -= 1
            stats_dict['nbEquipementEtatConservation'][ancien_dict['EtatConservation']] -= 1
            stats_dict['nbEquipementEtatService'][ancien_dict['EtatService']] -= 1
            stats_dict['nbEquipementCentreService'][ancien_dict['CentreService']][
                ancien_dict['CategorieEquipement']] -= 1
            stats_dict['nbEquipementProvenance'][ancien_dict['Provenance']] -= 1
        elif nouveau_dict is not None and ancien_dict is not None:  # cas où on modifie un équipement
            print('cas de la modification')
            if ancien_dict['EtatConservation'] != nouveau_dict['EtatConservation']:
                stats_dict['nbEquipementEtatConservation'][ancien_dict['EtatConservation']] -= 1
                stats_dict['nbEquipementEtatConservation'][nouveau_dict['EtatConservation']] += 1
            if ancien_dict['EtatService'] != nouveau_dict['EtatService']:
                stats_dict['nbEquipementEtatService'][ancien_dict['EtatService']] -= 1
                stats_dict['nbEquipementEtatService'][nouveau_dict['EtatService']] += 1
            if ancien_dict['Provenance'] != nouveau_dict['Provenance']:
                stats_dict['nbEquipementProvenance'][ancien_dict['Provenance']] -= 1
                stats_dict['nbEquipementProvenance'][nouveau_dict['Provenance']] += 1
            if ancien_dict['CentreService'] != nouveau_dict['CentreService'] or ancien_dict['CategorieEquipement'] != \
                    nouveau_dict['CategorieEquipement']:
                stats_dict['nbEquipementCentreService'][ancien_dict['CentreService']][
                    ancien_dict['CategorieEquipement']] -= 1
                stats_dict['nbEquipementCentreService'][nouveau_dict['CentreService']][
                    nouveau_dict['CategorieEquipement']] += 1
        self._ActualiserStats(stats_dict)

    # Cette fonction parcoure la base de données et recalcule les statistiques en cas de bug du logiciel. On s'assure
    # d'avoir les statistiques à jour
    def _recalculStats(self):
        stats = self._getStats()
        print("fichier actuel de stats", stats)
        conf = self._getConf()
        db = self._getDB()
        Equipement = Query()

        # recupère les champs possibles pour EtatService
        list_EtatService = list(conf['EtatService'])
        # récupère les champs possibles pour EtatConservation
        list_EtatConservation = list(conf['EtatConservation'])
        # récupère les champs possibles pour la provenance
        list_Provenance = list(conf['Provenance'])
        # récupère les champs possibles pour le centre de service
        list_CentreService = list(conf['CentreService'])
        # récupère les champs possibles pour la CategorieEquipement
        list_CategorieEquipement = list(conf['CategorieEquipement'])
        print("Fin recuperation des differents listes")
        # Nombre total d'équipements
        stats['nbEquipement'] = len(db)

        # Nombre d'équipement selon l'état de service
        for element in list_EtatService:
            stats['nbEquipementEtatService'][element] = db.count(Equipement['EtatService'] == element)

        # Nombre d'équipement selon l'état de service
        for element in list_EtatConservation:
            stats['nbEquipementEtatConservation'][element] = db.count(Equipement['EtatConservation'] == element)

        stats['nbEquipementProvenance'] = dict()
        stats['nbEquipementCentreService'] = dict()
        print("Debut comptage selon provenance")
        # Nombre d'équipement selon la provenance
        for element in list_Provenance:
            print((stats['nbEquipementProvenance']))
            if (stats['nbEquipementProvenance'] is None):
                stats['nbEquipementProvenance'] = dict()
            # if element not in stats:  # ajoute la provenance au fichier de stats
            #     stats['nbEquipementProvenance'][element] = 0
            stats['nbEquipementProvenance'][element] = db.count(Equipement['Provenance'] == element)
        print("Debut comptage selon categorie par centre de service")
        # Nombre d'équipement de chaque catégorie par centre de service
        print(list_CentreService)
        for centre in list_CentreService:
            print("Calcul pour le centre : ", centre)
            if stats['nbEquipementCentreService'] is None:
                stats['nbEquipementCentreService'] = dict()
            if centre not in stats[
                'nbEquipementCentreService']:  # vérifie si le centre de service associé à l'éq. est dans le fichier de stats
                stats['nbEquipementCentreService'][centre] = dict()  # si non, ajout du centre de service
            for categorie in list_CategorieEquipement:
                print("recherche pour la categorie : ", categorie)
                recherche_temp = db.count((Equipement['CentreService'] == centre) &
                                          (Equipement['CategorieEquipement'] == categorie))
                if recherche_temp != 0:
                    stats['nbEquipementCentreService'][centre][categorie] = recherche_temp
        print("Fin comptage")
        self._ActualiserStats(stats)
        print("Actualisation des stats finie")

    def _ActualiserStats(self, stats):
        try:
            if not os.path.exists(self.stats_file):  # vérifie si le fichier de configuration existe
                raise OSError
            else:
                with open(self.stats_file, 'w') as fichierStat:  # ouvre le fichier et l'actualise
                    fichierStat.write(yaml.dump(stats, default_flow_style=False))
        except OSError:
            print("Could not update: ", self.stats_file)

    def _getConf(self):
        try:
            with open(self.conf_file, 'r') as fichierConf:  # try: ouvrir le fichier et le lire
                conf = yaml.load(fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", self.conf_file)  # définir ce qu'il faut faire pour corriger

        return conf

    def _getStats(self):
        try:
            with open(self.stats_file, 'r') as statFile:
                stats = yaml.load(statFile)
        except IOError:
            print("Could not read file: ", self.stats_file)

        return stats

    def _getDB(self):
        try:
            if not os.path.exists(self._pathnameEQ):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathnameEQ, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)

        return db




if __name__ == "__main__":  # Execution lorsque le fichier est lance
    if True:
        #  TESTS
        manager = EquipementManager('Equipement.db')

        data = {'CategorieEquipement': 'Stéthoscope',
                'Marque': 'Lit de la muerte',
                'Modele': 'E432',
                'NumeroSerie': '1134',
                'Salle': 'A867',
                'CentreService': 'Urgence',
                'DateAcquisition': datetime.date(2008, 7, 12),
                'DateDernierEntretien': datetime.date(2011, 2, 27),
                'FreqEntretien': 30,
                'Provenance': 'Poly',
                'EtatService': '',
                'EtatConservation': 'Quasi neuf',
                'CodeAsset': '1234',
                'Commentaires': '',
                'PdfPath': ''}

        manager2 = EquipementManager('Equipement_B.db')


        #print("PROCHAIN ID, ", manager._ObtenirProchainID())
        # print(manager._VerifierDict(data))
        # dic_request = {'CategorieEquipement': 'ECG',
        #               'Marque': 'Peter',
        #               'Modele': 'blabla'}
        #dic_request = {'CategorieEquipement': 'Analyseur CD4 \(VIH\)'}
        #               'Salle': 'B',
        #               'CentreService': '',
        #               'NumeroSerie': '',
        #               'Provenance': '',
        #               'EtatService': '',
        #               'EtatConservation': ''}

        # dic_request = {'Marque': 'uerte'}
        #print(manager.AjouterEquipement(data))
        #print(manager.SupprimerEquipement(2))
        #  id_supp en int
        # print(dic_request)
        #print(manager.RechercherEquipement({}))

        #print("Derniere requete BDD")
        equipements = manager._AfficherBD()
        for equipement in equipements:
            print(equipement)
            print(manager2.AjouterEquipement(equipement))

        # Stats
        '''print(manager._statsNbTotalEquipement())
        print(manager._statsNbEquipementEtatService())
        print(manager._statsNbEquipementEtatConservation())
        print(manager._statsNbEquipementProvenance())
        print(manager._statsNbEquipementCentreServiceCategorie())
        '''
        #manager._recalculStats()
