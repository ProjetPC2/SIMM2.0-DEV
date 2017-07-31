import os
import sys
import time
from multiprocessing.pool import Pool

import yaml
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QApplication, QPushButton
from multiprocessing import Process
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer
from reportlab.rl_config import defaultPageSize

import random
import sys
from threading import Thread
import time

from BDD.EquipementManagerSQLite import EquipementManager
from Interface.FenetresEnPython.Fichiers import pathEquipementDatabase


class PDF():
    def __init__(self):
        # Thread.__init__(self)
        self.PAGE_WIDTH = defaultPageSize[1];
        self.PAGE_HEIGHT = defaultPageSize[0]

        self.Title = "Inventaire - S.I.M.M 2.0"
        self.pageinfo = "S.I.M.M 2.0"

        #TODO : a completer avec le nom de l'hopital
        self.nomHopital = "Hôpital Universitaire Justinien"

        #On autorise que les pdf
        # self.filter = "PDF (*.pdf)"
        # fileName = QFileDialog.getSaveFileName(None, 'Save file', "/home/SIMM2.0.pdf", filter)
        #On ouvre une fenetre de dialogue pour demander ou placer le fichier
        #On place le fichier par defaut dans le bureau avec le nom SIMM2.0.pdf
        # self.fileName = QFileDialog.getSaveFileName(None, 'Save file', os.path.expanduser("~/Desktop/SIMM2.0.pdf"), self.filter)
        # print("bouton", bouton.text())
        self.finImpression = Signal()

    def myFirstPage(self, canvas, doc):
        """Methode s'occupant de la mise en page du debut de document
        On va ici mettre les differentes informations utiles comme le titre, et les differentes informations d'impressions
        Cette methode fait la mise en page du debut du document"""
        canvas.saveState()
        canvas.setFont('Times-Bold',16)
        canvas.drawCentredString(self.PAGE_WIDTH/2.0, self.PAGE_HEIGHT-108, self.Title)
        canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d / %s" % (doc.page, self.pageinfo))
        espace_soulignement = 10
        facteurDivision = 10
        espacement = 130
        technicien = "Techniciens de l'Hôpital Universitaire Justinien"
        canvas.drawString(self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4, 'Hôpital Universitaire Justinien'
        canvas.line(self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement,
                    self.PAGE_WIDTH / facteurDivision + 230, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement)
        # canvas.setLineWidth(1.2)
        canvas.drawString(self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - 3 * espace_soulignement,
                          "Inventaire du parc d'équipements médicaux")
        canvas.drawString(500, 750, "12/12/2010")
        canvas.line(480, 747, 580, 747)
        canvas.drawString(6 * self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4,
                          "Délivré par l'atelier de génie biomédical de l'HUJ"
        canvas.line(6 * self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement,
                    6 * self.PAGE_WIDTH / facteurDivision + 295, 3 * self.PAGE_HEIGHT / 4 - espace_soulignement)
        date = time.strftime("%d/%m/%Y")
        # datetime.datetime.now()#datetime.time.strftime("%d/%m/%Y")
        canvas.drawString(6 * self.PAGE_WIDTH / facteurDivision, 3 * self.PAGE_HEIGHT / 4 - 3 * espace_soulignement,
                          "Date : %s" % date)
        canvas.drawString(6 * self.PAGE_WIDTH / facteurDivision + espacement, 3 * self.PAGE_HEIGHT / 4 - 3 * espace_soulignement,
                          "Technicien : %s" % technicien)
        # canvas.drawImage(ImageReader(os.path.join("Images","SIMM2.0.png")), 100, 100)#, width=None, height=None, mask=None)

        # canvas.save()
        canvas.restoreState()

    def myLaterPages(self, canvas, doc):
        """Methode permettant d'avoir la numerotation de la page en bas a gauche
        Affichage du numero de la page et du nom du logiciel"""
        canvas.saveState()
        canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, self.pageinfo))
        canvas.restoreState()

    def creationPDF(self, path):
        doc = SimpleDocTemplate(path, pagesize = landscape(A4))
        # Conteneur elements pour les objets qui vont etre dessines sur le pdf
        # Ajout d'un espacement
        elements = [Spacer(0, 2 * inch)]
        # Ajout du logo de SIMM 2.0
        elements.append(self.get_image(os.path.join("Images","SIMM2.0.png"), width=5 * cm))
        elements.append(Spacer(0, 1 * inch))
        #Creation du style par defaut
        styleSheet = getSampleStyleSheet()
        style = styleSheet["Normal"]

        #Recuperation des donnees utiles dans les fichiers de la BDD
        equipementManager = EquipementManager(pathEquipementDatabase)
        conf_file = 'fichier_conf.yaml'  # pathname du fichier de configuration
        try:
            self.fichierConf = open(conf_file, 'r')  # try: ouvrir le fichier et le lire
            with self.fichierConf:
                conf = yaml.load(self.fichierConf)
        except IOError:  # attrape l'erreur IOError si elle se présente et renvoie
            print("Could not read file: ", conf_file)  # définir ce qu'il faut faire pour corriger

        # récupère la liste des centres de services dans le fichier de configuration
        listeCentreService = list(conf['CentreService'])

        #Creation du tableau avec les informations concernant le centre de service
        for centreService in listeCentreService:
            listeEquipement = equipementManager.RechercherEquipement({"CentreService" : centreService})
            listeTotal = list()
            listeColonne = ["ID", "CategorieEquipement", "Marque", "Modele", "CentreService", "EtatService", "Provenance"]
            listeColonne1 = [Paragraph("<b>ID</b>", style),
                             Paragraph("<b>Categorie Equipement</b>", style),
                             Paragraph("<b>Marque</b>", style),
                             Paragraph("<b>Modele</b>", style),
                             Paragraph("<b>Centre Service</b>", style),
                             Paragraph("<b>Etat Service</b>", style),
                             Paragraph("<b>Provenance</b>", style)]

            listeTotal.append(listeColonne1)
            if (any(listeEquipement)):
                # Cas ou l'equipement existe
                for i, dictionnaire in enumerate(listeEquipement):
                    # Recuperation des donnees sous forme de string
                    print(dictionnaire)
                    listTemp = list()
                    # for element in dictionnaire.values():
                    #     listTemp.append(element)
                    listTemp.append(Paragraph(str(dictionnaire["ID"]), styleSheet['Normal']))
                    listTemp.append(Paragraph(dictionnaire["CategorieEquipement"],styleSheet['Normal']))
                    listTemp.append(Paragraph(dictionnaire["Marque"], styleSheet['Normal']))
                    listTemp.append(Paragraph(dictionnaire["Modele"], styleSheet['Normal']))
                    listTemp.append(Paragraph(dictionnaire["CentreService"], styleSheet['Normal']))
                    listTemp.append(Paragraph(dictionnaire["EtatService"], styleSheet['Normal']))
                    listTemp.append(Paragraph(dictionnaire["Provenance"], styleSheet['Normal']))

                    listeTotal.append(listTemp)
            else:
                # Cas ou l'equipement n'existe pas
                pass

            tableauCentreService = Table(listeTotal, style=[('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                         ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                                         ('BOX', (0, 0), (-1, 0), 2, colors.black),
                                         ('BOX', (0, 0), (-1, -1), 2, colors.black),
                                         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                         ('FONTSIZE', (0, 0), (-1, -1), 12),
                                         ('FONTSIZE', (0, 0), (-1, 0), 14)

                                         ],)
            # t._argW[3] = 0.5 * inch

            #On ajoute les differents elements a la liste contenant les differents elements graphique du pdf
            #Ecriture de l'unite a laquelle appartient les equipements
            Service = ("<b><u>Unite %s : </u></b>" % centreService)
            titreTableau = Paragraph(Service, style)
            elements.append(titreTableau)
            elements.append(Spacer(0,10))
            elements.append(tableauCentreService)
            elements.append(Spacer(0, 50))

        # Ecriture du document pdf
        doc.build(elements, onFirstPage=self.myFirstPage, onLaterPages= self.myLaterPages)
        print("termine")
        self.finImpression.finImpression.emit()
        # if(bouton is not None):
        #     bouton.setDisabled(False)


    def get_image(self, path, width=1*cm):
        """Methode permettant la creation de l'image"""
        img = ImageReader(path)
        iw, ih = img.getSize()
        aspect = ih / float(iw)
        return Image(path, width=width, height=(width * aspect))

    def run(self):
        if(self.fileName[0] != None and self.fileName[0] !=""):
            # p = Process(target=self.creationPDF, args=(self.fileName[0],))
            # self.creationPDF(self.fileName[0])
            # p.start()
            pool = Pool(processes=4)  # start 4 worker processes
            result = pool.apply_async(self.creationPDF, [self.fileName[0]])
        else:
            print("Sauvegarde annule")

class Signal(QObject):
    finImpression = pyqtSignal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # pdf = PDF(pdf.fileName[0])
    # print(pdf.fileName[0])
    # # pdf.creationPDF(pdf.fileName[0])
    # pdf.run()
    sys.exit(app.exec_())
