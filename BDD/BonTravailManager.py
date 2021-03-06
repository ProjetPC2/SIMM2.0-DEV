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
        self.conf_file = 'fichier_conf.yaml'                         # nom du fichier de configuration
        self.piece_file = 'fichier_piece.yaml'

    def AjouterBonTravail(self, id_equipement, dictio):
        # Ajout du bon de travail dans la base de données
        conf = self._getConf()
        db = self._getDB()
        db_equip = self._getEquipDB()
        Equipement = Query()
        list_ajout_champ_equipement = list(conf['BDT_Ajout_Champ_Equipement'])   # récupère la liste des informations à ajouter dans le dictionnaire
        dict_renvoi = {'Reussite': False}                       # Initialisation du dictionnaire de renvoie
        dict_equipement = db_equip.get(Equipement['ID'] == id_equipement)  # récupère l'équipement via la BDD des équipements
        id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)    # id du nouveau bon de travail

        if id_bdt == -1:                                        # Equipement non existant
            print("The equipment doesn't exist. ID :", id_equipement)
            return dict_renvoi
        elif self._verifierChamps(dictio, conf) and self._verifierDict(dictio, conf):   # Vérification du dictionnaire
            dictio['ID-EQ'] = str(id_equipement)
            dictio['ID-BDT'] = str(id_bdt)
            for key, value in dict_equipement.items():     # récupère les infos pertinentes et les ajoute au dictionnaire du bon de travail
                if key in list_ajout_champ_equipement:
                    dictio[key] = value
            print(dictio)
            if db.insert(dictio) != list([]):                   # ajout du nouveau bdt dans la db
                # Mise à jour du nombre de bons de travail pour cet équipement dans la base de données des équipements
                Equipement = Query()
                db_equip.update(increment('NbBonTravail'), Equipement['ID'] == id_equipement)
                dict_renvoi['Reussite'] = True                  # Ajout réalisé
                self._ActualiserConfiguration(conf)                 # Actualisation du fichier conf
        else:
            print('An error occured')
        
        return dict_renvoi

    # il faut update le champ dans NbBonTravail dans l'équipement
    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):
        BonTravail = Query()
        dict_renvoi = {'Reussite': False}                       # Initialisation du dictionnaire de renvoi à false
        db = self._getDB()

        if db.remove((BonTravail['ID-EQ'] == id_eq_supp) & (BonTravail['ID-BDT'] == id_bdt_supp)) != list([]):  # suppression du bdt
            dict_renvoi['Reussite'] = True                      # Suppression réussie
        
        return dict_renvoi


    def RechercherBonTravail(self, regex_dict):
        db = self._getDB()
        conf = self._getConf()
        recherche = Query()
        firstEntry = True
        for key, value in regex_dict.items():
            # Pour chaque champ de la recherche
            if (key == 'ID-EQ'):
                # Dans le cas de la recherche par ID
                if firstEntry:                                  # Si c'est la première recherche
                    queryUser = recherche["ID-EQ"] == value
                    firstEntry = False
                else:
                    queryUser = (queryUser) & (recherche['ID_EQ'] == value)
            else:
                if not isinstance(value, datetime.date):           # S'il ne s'agit pas d'une date
                    if firstEntry:                                  # Si c'est la première recherche
                        queryUser = (recherche[key].search(value))  # Trouver dans la base de données la valeur correspondante
                        firstEntry = False
                    else:
                        queryUser = (queryUser) & (recherche[key].search(value))
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

        print(queryUser)
        result = db.search(queryUser)                           # Rechercher la combinaison de chaque champ de recherche
        return result


    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        BonTravail = Query()
        dict_renvoi = {'Reussite': False}                       # Initialisation du dictionnaire de renvoie à false
        db = self._getDB()
        conf = self._getConf()
        if self._verifierChamps(dict_modif, conf) and self._verifierDict(dict_modif, conf):
            print('ICI')
            if db.update(dict_modif, (BonTravail['ID-EQ'] == id_eq_modif) & (BonTravail['ID-BDT'] == id_bdt_modif)) != []:
                dict_renvoi['Reussite'] = True                  # Mise à jour de l'équipement réussie
        self._ActualiserConfiguration(conf)                         # Actualiser le fichier de configuration
        return dict_renvoi


    def _ObtenirProchainIDdeBDT(self, id_equip):
        Equipement = Query()
        db = self._getEquipDB()
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


    def _verifierChamps(self, dictio, conf):
        conforme = True
        listeOfLegalKeys_temp = list(conf['champsAcceptes-BDT'])  # Enregistrer les champs possibles à partir du fichier de configuration
        for key, value in dictio.items():                       # Vérifier pour chaque champ sa présence dans dictio
            if key in listeOfLegalKeys_temp:                    # Si champ présent dans champs possibles
                listeOfLegalKeys_temp.remove(key)               # Le retirer de la liste temporaire
            else:                                               # Sinon afficher erreur pour ce champ
                conforme = False                                # Le dictionnaire n'est pas conforme
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
            if key in list_champ_ajout:                         # Si le champ permet des ajouts de valeurs
                list_temp = list(conf[key])
                if value not in list_temp:                      # Et que la valeur n'est pas dans la liste
                    conf[key].append(value)               # Ajouter la valeur
            elif key in list_champ_pas_ajout:                   # Si le champ ne permet pas d'ajout
                list_temp = list(conf[key])
                if value not in list_temp:                      # Et que la valeur n'est pas dans la liste
                    conforme = False                            # Le dictionnaire n'est pas conforme
            elif key in list_champ_format_precis:               # Si le champ doit avoir une valeur avec un format précis
                if (not isinstance(value, datetime.date)) and (not isinstance(value, datetime.time)):        # Vérifier le format de datetime.date()
                    conforme = False

        self._ActualiserConfiguration(conf)                         # Actualiser le fichier de configuration avec les nouvelles valeurs
        return conforme

    def _ActualiserConfiguration(self, conf):
        pass
        '''
        with open('fichier_conf.yaml', 'w') as fichierConf:
            fichierConf.write(yaml.dump(conf, default_flow_style=False))
        '''

    def _ActualiserPiece(self, pieces):
        try:
            if not os.path.exists(self.piece_file):
                pass #TODO a completer pour l'ajout des piece dans le fichier
        except:
            pass

    def _getConf(self):
        try:
            with open(self.conf_file, 'r') as fichierConf:            # try: ouvrir le fichier et le lire
                conf = yaml.load(fichierConf)
        except IOError:                                                             # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", self.conf_file)                          # définir ce qu'il faut faire pour corriger

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
                raise OSError("Oups nous ne trouvons plus la bdd Bon De Travail!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        
        return db

    def _getEquipDB(self):
        try:
            if not os.path.exists(self._equip_pathname):
                raise OSError("Oups nous ne trouvons plus la bdd équipements!")    # erreur si le path n'existe pas
            else:
                db = TinyDB(self._equip_pathname, storage=YAMLStorage)  # data base des équipements
        except OSError as e:
            print(e)
        
        return db


if __name__ == "__main__":  # Execution lorsque le fichier est lance
#if True:
    # TESTS
    manager = BonTravailManager('DataBase_BDT.yaml', 'DataBase_Equipement.yaml')

    data1 = {'Date': datetime.date(2016, 2, 22),
             'TempsEstime': datetime.time(2, 30),
             'DescriptionSituation': 'Vraiment brisé',
             'DescriptionIntervention': 'Blablabla-modif',
             'EtatBDT': 'Ouvert',
             'NomTechnicien': 'Kerlin'}

    dic_request = {'CategorieEquipement': 'Saturomètre \(Oxymètre\)'}

    #dic_request = {'AvantLe': datetime.date(2016, 03, 12)}
    #               'ApresLe': datetime.date(2016, 06, 10)}

    #print(manager.AjouterBonTravail('2', data1))                       # Ajout de 2 équipements de suite (pour tester...
    #manager.AjouterBonTravail(1, data2)                        # ... la vérification des champs)
    #print(manager.SupprimerBonTravail('1', '2'))                       # id_supp en int
    print((manager.RechercherBonTravail(dic_request)))
    #print(manager.RechercherBonTravail(dict_request))
    #print(manager.ModifierBonTravail('2', '3', data1))                     # id_modif en int
























