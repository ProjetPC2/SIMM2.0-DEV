# def _statsNbTotalEquipement(self):
#     try:
#         if not os.path.exists(self._pathname):
#             raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
#         else:
#             db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
#     except OSError as e:
#         print(e)
#     return len(db)
#
#
# # Cette méthode renvoie un dictionnaire avec comme clées les trois états de service possibles et comme valeur le
# # nombre d'équipements par état de service
# # key: {'En service', 'En maintenance', 'Au rebut'}
#
# def _statsNbEquipementEtatService(self):
#     try:
#         if not os.path.exists(self._pathname):
#             raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
#         else:
#             db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
#     except OSError as e:
#         print(e)
#     list_etat_service = list(self._conf['EtatService'])  # récupère les états de services possibles
#     Equipement = Query()
#     dictRenvoiEtatService = {}
#     for element in list_etat_service:  # parcoure la liste des états de service et recherche dans bdd
#         dictRenvoiEtatService[element] = db.count(
#             Equipement['EtatService'] == element)  # combien d'équipements ont le champ
#     return dictRenvoiEtatService  # 'EtatService' à la valeur de element
#
#
# # Cette méthode renvoie un dictionnaire avec comme clées les quatre états de conservation possibles et comme valeur le
# # nombre d'équipements par état de conservation
# # key: {'Quasi neuf', 'Acceptable', 'En fin de vie', 'Desuet'}
#
# def _statsNbEquipementEtatConservation(self):
#     try:
#         if not os.path.exists(self._pathname):
#             raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
#         else:
#             db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
#     except OSError as e:
#         print(e)
#     list_etat_conservation = list(self._conf['EtatConservation'])  # récupère les états de conservation possibles
#     Equipement = Query()
#     dictRenvoiEtatConservation = {}
#     for element in list_etat_conservation:  # parcoure la liste des provenance et recherche dans bdd
#         dictRenvoiEtatConservation[element] = db.count(
#             Equipement['EtatConservation'] == element)  # combien d'équipements ont le champ
#     return dictRenvoiEtatConservation  # 'EtatConservation' à la valeur de element
#
#
# # Cette méthode renvoie un dictionnaire avec comme clées les provenance possibles et comme valeur le
# # nombre d'équipements par provenance
# def _statsNbEquipementProvenance(self):
#     try:
#         if not os.path.exists(self._pathname):
#             raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
#         else:
#             db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
#     except OSError as e:
#         print(e)
#     list_provenance = list(self._conf['Provenance'])  # récupère la liste des provenances possibles
#     Equipement = Query()
#     dictRenvoiProvenance = {}
#     for element in list_provenance:  # parcoure la liste des provenance et recherche dans bdd
#         dictRenvoiProvenance[element] = db.count(
#             Equipement['Provenance'] == element)  # combien d'équipements ont le champ
#     return dictRenvoiProvenance  # 'Provenance' à la valeur de element
#
#
# # Cette méthode renvoie un dictionnaire à deux niveaux. Le premier niveau a comme clée les différents centres de
# # de service ('CentreService') qui se trouvent dans le fichier de configuration. Dans le champs des données pour ces clées,
# # on retrouve un dictionnaire (2e niveau) qui lui a comme clée les catégories d'équipements ('CategorieEquipement') que l'on
# # retrouve dans le fichier de configuration. Il est à noter que lorsqu'un centre de service ne possède pas d'équipements
# # d'un type X (ex. IRM), le champ contenant la clée X et la valeur 0 au deuxième niveau est retiré du dictionnaire.
#
# def _statsNbEquipementCentreServiceCategorie(self):
#     try:
#         if not os.path.exists(self._pathname):
#             raise OSError("Oups nous ne trouvons plus la bdd équipements!")  # erreur si le path n'existe pas
#         else:
#             db = TinyDB(self._pathname, storage=YAMLStorage)  # data base des équipements
#     except OSError as e:
#         print(e)
#     list_centre_service = list(self._conf['CentreService'])  # récupère les listes pour 'CentreService'
#     list_categorie_equipement = list(
#         self._conf['CategorieEquipement'])  # et 'CategorieEquipement' dans le fichier de conf
#     Equipement = Query()
#     dictRenvoiCentreServiceCategorie = {}
#     for centre in list_centre_service:  # on parcoure d'abord les centres de service
#         dictRenvoiCentreServiceCategorie[centre] = {}
#         for categorie in list_categorie_equipement:
#             recherche_temp = db.count(
#                 (Equipement['CategorieEquipement'] == categorie) &  # On compte le nombre de fois qu'il y un equipement
#                 (Equipement[
#                      'CentreService'] == centre))  # qui est dans le même centre de service ET qui est de même catégorie
#             if recherche_temp != 0:  # On s'assure que la recherche ne retourne par 0, car ce n'est pas pertinent
#                 dictRenvoiCentreServiceCategorie[centre][categorie] = recherche_temp  # pour nos statistiques
#     return dictRenvoiCentreServiceCategorie
