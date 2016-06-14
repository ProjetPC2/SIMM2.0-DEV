# coding=utf-8
############################################################################################################
# NOM : Projet PC2
# DATE DE LA DERNIÈRE MODIFICATION : 9 juin 2016
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
from yamlStorage import YAMLStorage
import datetime

# vérifier l'ouverture du fichier de conf, fichier de BDD equipement, fichier BDD BdT avec des exceptions


class BonTravailManager:
    def __init__(self, bdt_pathname, equip_pathname):
        self._pathname = bdt_pathname                           # pathname de la base de données des bons de travail
        self._equip_pathname = equip_pathname                   # pathname de la base de données associées des équipements
        with open('fichier_conf.yaml', 'r') as fichierConf:     # ouverture du fichier conf
            self._conf = yaml.load(fichierConf)

    def AjouterBonTravail(self, id_equipement, dictio):
        # Ajout du bon de travail dans la base de données
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)    # id du nouveau bon de travail
        
        # vérifier que l'équipement existe avant de l'ajouter

        if self._verifierChamps(dictio):
            dictio['ID-EQ'] = str(id_equipement)
            dictio['ID-BDT'] = str(id_bdt)
            db.insert(dictio)                                   # ajout du nouveau bdt dans la db

            # Mise à jour du nombre de bons de travail pour cet équipement dans la base de données des équipements
            db_equip = TinyDB(self._equip_pathname, storage=YAMLStorage)
            Equipement = Query()
            db_equip.update(increment('NbBonTravail'), Equipement['ID'] == id_equipement)
            self._ActualiserConfiguration()
        else:
            print('Erreur dans le dictionnaire')

    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        result = db.remove((BonTravail['ID-EQ'] == id_eq_supp) & (BonTravail['ID-BDT'] == id_bdt_supp))  # suppression du bdt
        self._ActualiserConfiguration()
        return result

    def RechercherBonTravail(self, regex_dict):
        db = TinyDB(self._pathname, storage=YAMLStorage)
        recherche = Query()
        firstEntry = True
        for key, value in regex_dict.items():
            # if is not Qdate
            if firstEntry:
                queryUser = (recherche[key].matches(value))
                firstEntry = False
            else:
                queryUser = (queryUser) & (recherche[key].matches(value))
            #else:
            #   if FirstEntry:
                    # queryUser = recherche[key] >= value
                    # il faudra peut-être regarder la valeur de la clée pour savoir si on doit faire une recherche >= ou <=
            #   else
        result = db.search(queryUser)
        return result

    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        # modif du dict associé au bdt
        db.update(dict_modif, (BonTravail['ID-EQ'] == id_eq_modif) & (BonTravail['ID-BDT'] == id_bdt_modif))
        self._ActualiserConfiguration()

    def _ObtenirProchainIDdeBDT(self, id_equip):
        Equipement = Query()
        db = TinyDB(self._equip_pathname, storage=YAMLStorage)
        equipement_ = db.get((Equipement['ID'] == id_equip))
        nb_bdt_pour_eq = equipement_['NbBonTravail']
        # faire étape de vérification si l'équipement existe
        if nb_bdt_pour_eq is None:                              # vérifier si des bons ont déjà été enregistrés
            new_id_bdt = 1
        else:
            new_id_bdt = nb_bdt_pour_eq + 1                     # nouvel id de bdt
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
        listeOfLegalKeys_temp = list(self._conf['champsAcceptes-BDT'])      # Enregistrer les champs possibles
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
        conforme = self._verifierChamps(dictio)
        for key, value in dictio.items():
            #if key == 'Date':
            #    if not isinstance(value, datetime.date):
            #        conforme = False
            if (key == 'Temps estime') or \
               (key == 'Description de la situation'):
                if not isinstance(value, str):
                    conforme = False
        return conforme

    def _ActualiserConfiguration(self):
        with open('fichier_conf.yaml', 'w') as fichierConf:
            fichierConf.write(yaml.dump(self._conf, default_flow_style=False))


#if __name__ == "__main__":  # Execution lorsque le fichier est lance
if True:
    # TESTS
    manager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')

    data1 = {'Date': None,
             'TempsEstime': '1 semaine',
             'DescriptionSituation': 'blabla',
             'DescriptionIntervention': 'Grosse discussion',
             'EtatBDT': None}


    dic_request = {'Description de la situation': 'test',       # VÉRIFIER LA RECHERCHE POUR LES DATES...
                   'Temps estime': '2'}


    manager.AjouterBonTravail('1', data1)                       # Ajout de 2 équipements de suite (pour tester...
    #manager.AjouterBonTravail(1, data2)                        # ... la vérification des champs)
    #manager.SupprimerBonTravail(1, 2)                          # id_supp en int
    # print(manager.RechercherBonTravail(dic_request))
    #manager.ModifierBonTravail(1, 2, data)                     # id_modif en int























