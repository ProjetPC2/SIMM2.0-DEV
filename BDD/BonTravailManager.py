# coding=utf-8
from tinydb import *
from tinydb.operations import increment
from yamlStorage import YAMLStorage
import datetime
import re


class BonTravailManager:
    def __init__(self, bdt_pathname, equip_pathname):
        self._pathname = bdt_pathname                           # pathname de la base de données des bons de travail
        self._equip_pathname = equip_pathname

    def AjouterBonTravail(self, id_equipement, dictio):
        # Ajout du bon de travail dans la base de données
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)    # id du nouveau bon de travail
        dictio['ID-EQ'] = id_equipement
        dictio['ID-BDT'] = id_bdt
        db.insert(dictio)                                       # ajout du nouveau bdt dans la db

        # Mise à jour du nombre de bons de travail pour cet équipement dans la base de données des équipements
        db_equip = TinyDB(self._equip_pathname, storage=YAMLStorage)
        Equipement = Query()
        db_equip.update(increment('Nombre de bons de travail'), Equipement['ID'] == id_equipement)


    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        result = db.remove((BonTravail['ID-EQ'] == id_eq_supp) & (BonTravail['ID-BDT'] == id_bdt_supp))  # suppression du bdt
        return result

    def RechercherBonTravail(self, regex_dict):
        db = TinyDB(self._pathname, storage=YAMLStorage)
        recherche = Query()
        firstEntry = True
        for key, value in regex_dict.items():
            if firstEntry:
                queryUser = (recherche[key].matches(value))
                firstEntry = False
            else:
                queryUser = (queryUser) & (recherche[key].matches(value))
        result = db.search(queryUser)
        return result

    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        # modif du dict associé au bdt
        db.update(dict_modif, (BonTravail['ID-EQ'] == id_eq_modif) & (BonTravail['ID-BDT'] == id_bdt_modif))

    def _ObtenirProchainIDdeBDT(self, id_equip):
        Equipement = Query()
        db = TinyDB(self._equip_pathname, storage=YAMLStorage)
        equipement_ = db.get((Equipement['ID'] == id_equip))
        nb_bdt_pour_eq = equipement_['Nombre de bons de travail']
        # faire étape de vérification si l'équipement existe
        if nb_bdt_pour_eq is None:                                  # vérifier si des bons ont déjà été enregistrés
            new_id_bdt = 1
        else:
            new_id_bdt = nb_bdt_pour_eq + 1                         # nouvel id de bdt
        return new_id_bdt


# TESTS
manager = BonTravailManager('DataBase_BDT.json', 'DataBase_Equipement.json')

data = {'Date': datetime.date.today(),                              # format de la date à vérifier
        'Temps estime': '2-modif',
        'Description de la situation': 'test-modif'}

dic_request = {'Description de la situation': 'test',               # VÉRIFIER LA RECHERCHE POUR LES DATES...
               'Temps estime': '2'}


#manager.AjouterBonTravail(1, data)
#manager.SupprimerBonTravail(1, 2)                  # id_supp en int
#print(manager.RechercherBonTravail(dic_request))
#manager.ModifierBonTravail(1, 2, data)                # id_modif en int























