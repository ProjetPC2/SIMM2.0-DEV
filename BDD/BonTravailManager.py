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
from tinydb.operations import increment
from BDD.yamlStorage import YAMLStorage
import datetime
import os

# vérifier l'ouverture du fichier de conf, fichier de BDD equipement, fichier BDD BdT avec des exceptions


class BonTravailManager:
    def __init__(self, bdt_pathname, equip_pathname):
        self._pathname = bdt_pathname                           # pathname de la base de données des bons de travail
        self._equip_pathname = equip_pathname                   # pathname de la base de données associées des équipements
        conf_file = 'fichier_conf.yaml'                         # nom du fichier de configuration
        try:                                                    # essaie d'ouvrir le fichier et de le lire
            with open(conf_file, 'r') as fichierConf:
                self._conf = yaml.load(fichierConf)
        except IOError:                                         # Si une erreur est détectée lors de l'ouverture du fichier
            print('Could not read the file', conf_file)         # Message d'erreur

    def AjouterBonTravail(self, id_equipement, dictio):
        # Ajout du bon de travail dans la base de données
        try:
            if not os.path.exists(self._pathname):              # erreur si le path n'existe pas
                raise OSError("Oups nous ne trouvons plus la bdd des bons de travail!")
            if not os.path.exists(self._equip_pathname):
                raise OSError("Oups nous ne trouvons plus la bdd des equipements!")
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des bons de travail
                db_equip = TinyDB(self._equip_pathname, storage=YAMLStorage)
        except OSError as e:
            print(e)

        dict_renvoi = {'Reussite': False}                       # Initialisation du dictionnaire de renvoie
        id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)    # id du nouveau bon de travail
        if id_bdt == -1:                                        # Equipement non existant
            print("The equipment doesn't exist. ID :", id_equipement)
            return dict_renvoi
        elif self._verifierChamps(dictio) and self._verifierDict(dictio):   # Vérification du dictionnaire
            dictio['ID-EQ'] = str(id_equipement)
            dictio['ID-BDT'] = str(id_bdt)
            if db.insert(dictio) != list([]):                   # ajout du nouveau bdt dans la db
                # Mise à jour du nombre de bons de travail pour cet équipement dans la base de données des équipements
                Equipement = Query()
                db_equip.update(increment('NbBonTravail'), Equipement['ID'] == id_equipement)
                dict_renvoi['Reussite'] = True                  # Ajout réalisé
                self._ActualiserConfiguration()                 # Actualisation du fichier conf
                return dict_renvoi
        else:
            print('An error occured')
            return dict_renvoi

    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):
        BonTravail = Query()
        dict_renvoi = {'Reussite': False}                       # Initialisation du dictionnaire de renvoi à false
        try:
            if not os.path.exists(self._pathname):              # erreur si le path n'existe pas
                raise OSError("Oups nous ne trouvons plus la bdd des bons de travail!")
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des bons de travail
        except OSError as e:
            print(e)

        if db.remove((BonTravail['ID-EQ'] == id_eq_supp) & (BonTravail['ID-BDT'] == id_bdt_supp)) != list([]):  # suppression du bdt
            dict_renvoi['Reussite'] = True                      # Suppression réussie
        self._ActualiserConfiguration()                         # Actualiser le fichier de configuration
        return dict_renvoi

    def RechercherBonTravail(self, regex_dict):
        db = TinyDB(self._pathname, storage=YAMLStorage)
        recherche = Query()
        firstEntry = True
        for key, value in regex_dict.items():
            # Pour chaque champ de la recherche
            if (key == "ID-EQ"):
                # Dans le cas de la recherche par ID
                queryUser = recherche["ID-EQ"] == value
            else:
                if not isinstance(value, datetime.date):            # S'il ne s'agit pas d'une date
                    if firstEntry:                                  # Si c'est la première recherche
                        queryUser = (recherche[key].matches(value))  # Trouver dans la base de données la valeur correspondante
                        firstEntry = False
                    else:
                        queryUser = (queryUser) & (recherche[key].matches(value))
                else:                                               # S'il s'agit d'une date
                    if key == 'ApresLe':                            # Chercher après la date
                        if firstEntry:                              # Si c'est la première recherche
                            queryUser = (recherche['Date'] >= value)
                            firstEntry = False
                        else:
                            queryUser = (queryUser) & (recherche['Date'] >= value)
                    if key == 'AvantLe':                            # Chercher avant la date
                        if firstEntry:                              # Si c'est la première recherche
                            queryUser = (recherche['Date'] <= value)
                            firstEntry = False
                        else:
                            queryUser = (queryUser) & (recherche['Date'] <= value)

        result = db.search(queryUser)                           # Rechercher la combinaison de chaque champ de recherche
        return result

    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        BonTravail = Query()
        dict_renvoi = {'Reussite': False}                       # Initialisation du dictionnaire de renvoie à false
        try:
            if not os.path.exists(self._pathname):              # erreur si le path n'existe pas
                raise OSError("Oups nous ne trouvons plus la bdd des bons de travail!")
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des bons de travail
        except OSError as e:
            print(e)

        if self._verifierChamps(dict_modif) and self._verifierDict(dict_modif):
            if db.update(dict_modif, (BonTravail['ID-EQ'] == id_eq_modif) & (BonTravail['ID-BDT'] == id_bdt_modif)) != []:
                dict_renvoi['Reussite'] = True                  # Mise à jour de l'équipement réussie
        self._ActualiserConfiguration()                         # Actualiser le fichier de configuration
        return dict_renvoi

    def _ObtenirProchainIDdeBDT(self, id_equip):
        Equipement = Query()
        db = TinyDB(self._equip_pathname, storage=YAMLStorage)
        equipement_ = db.get((Equipement['ID'] == id_equip))    # Aller chercher l'équipement associé au bon de travail
        if equipement_ is None:                                 # Si l'équipement n'existe pas
            return -1
        else:                                                   # S'il existe, déterminer le nouveau numéro du BDT
            nb_bdt_pour_eq = equipement_['NbBonTravail']
            if nb_bdt_pour_eq is None:                          # vérifier si des bons ont déjà été enregistrés
                new_id_bdt = 1
            else:
                new_id_bdt = nb_bdt_pour_eq + 1                 # nouvel id de bdt
            return new_id_bdt

    def configParser(configFile):
        config = yaml.load(configFile)
        for k in ['swsets']:
            if k in config:
                tup = ()
                for v in config[k]:
                    tup += (v,)
                config[k] = tup
        return config

    def _verifierChamps(self, dictio):
        conforme = True
        listeOfLegalKeys_temp = list(self._conf['champsAcceptes-BDT'])  # Enregistrer les champs possibles à partir du fichier de configuration
        for key, value in dictio.items():                       # Vérifier pour chaque champ sa présence dans dictio
            if key in listeOfLegalKeys_temp:                    # Si champ présent dans champs possibles
                listeOfLegalKeys_temp.remove(key)               # Le retirer de la liste temporaire
            else:                                               # Sinon afficher erreur pour ce champ
                conforme = False                                # Le dictionnaire n'est pas conforme
        if (not conforme) or (len(listeOfLegalKeys_temp) is not 0):
            return False
        else:
            return True

    def _verifierDict(self, dictio):
        conforme = True

        # Récupérer la liste des champs auxquels on peut ajouter des valeurs
        list_champ_ajout = list(self._conf['BDT_ChampAjoutPermis'])
        # Récupérer la liste des champs auxquels on ne peut pas ajouter des valeurs
        list_champ_pas_ajout = list(self._conf['BDT_ChampAjoutNonPermis'])
        # Récupérer la liste des champs qui doivent avoir des valeurs avec un format précis
        list_champ_format_precis = list(self._conf['BDT_ChampFormatPrecis'])

        for key, value in dictio.items():
            if key in list_champ_ajout:                         # Si le champ permet des ajouts de valeurs
                list_temp = list(self._conf[key])
                if value not in list_temp:                      # Et que la valeur n'est pas dans la liste
                    self._conf[key].append(value)               # Ajouter la valeur
            elif key in list_champ_pas_ajout:                   # Si le champ ne permet pas d'ajout
                list_temp = list(self._conf[key])
                if value not in list_temp:                      # Et que la valeur n'est pas dans la liste
                    conforme = False                            # Le dictionnaire n'est pas conforme
            elif key in list_champ_format_precis:               # Si le champ doit avoir une valeur avec un format précis
                if not isinstance(value, datetime.date):        # Vérifier le format de datetime.date()
                    conforme = False

        self._ActualiserConfiguration()                         # Actualiser le fichier de configuration avec les nouvelles valeurs
        return conforme

    def _ActualiserConfiguration(self):
        with open('fichier_conf.yaml', 'w') as fichierConf:
            fichierConf.write(yaml.dump(self._conf, default_flow_style=False))


if __name__ == "__main__":  # Execution lorsque le fichier est lance
#if True:
    # TESTS
    manager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')

    data1 = {'Date': datetime.date(2016, 2, 22),
             'TempsEstime': 'Cam-modif',
             'DescriptionSituation': 'Larose-modif',
             'DescriptionIntervention': 'Blablabla-modif',
             'EtatBDT': 'Ferme'}


    #dic_request = {'AvantLe': datetime.date(2016, 03, 12)}
                   #'ApresLe': datetime.date(2016, 06, 10)}


    #print(manager.AjouterBonTravail('1', data1))                       # Ajout de 2 équipements de suite (pour tester...
    #manager.AjouterBonTravail(1, data2)                        # ... la vérification des champs)
    #print(manager.SupprimerBonTravail('1', '2'))                       # id_supp en int
    #print(len(manager.RechercherBonTravail(dic_request)))
    #print(manager.RechercherBonTravail(dic_request))
    #print(manager.ModifierBonTravail('1', '2', data1))                     # id_modif en int























