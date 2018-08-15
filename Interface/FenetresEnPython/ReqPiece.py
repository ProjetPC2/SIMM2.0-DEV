# -*- coding: utf-8 -*-
import os
import glob

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from reportlab.lib import utils
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

from Interface.FenetresEnPython.ReqPieceUI import Ui_ReqPiece

class ReqPiece(Ui_ReqPiece):

    def __init__(self, widget):
        self.setupUi(widget)

    def notify_file_opened(self):
        """Fonction gerant la creation d'une fenetre de verification
        lors de la fermeture de la fenetre"""
        self.messageBox = QMessageBox()
        self.messageBox.setStyleSheet("QPushButton {\n"
                                        "color: black;\n"
                                        "background-color:rgb(245, 245, 245);\n"
                                        "border-width: 1px;\n"
                                        "border-color: grey;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 4px;\n"
                                        "padding: 3px;\n"
                                        "font: bold 12px;\n"
                                        "padding-left: 5px;\n"
                                        "padding-right: 5px;\n"
                                        "min-width: 80px;\n"
                                        "max-width:220px;\n"
                                        "min-height: 30px;\n"
                                        "max-height: 30px;\n"
                                        "}\n")
        self.messageBox.setText("Fermer le fichier pour permettre toute modification")
        self.messageBox.setWindowTitle("SIMM 2.1")
        self.messageBox.setWindowIcon(QIcon('Images/SIMM2.0.png'))
        self.boutonOk = QPushButton("OK")
        self.messageBox.addButton(self.boutonOk, QMessageBox.AcceptRole)
        retour = self.messageBox.exec()
        print(retour)
    
    def populate(self, pics, imagesPerRow=2, flags=Qt.KeepAspectRatioByExpanding):
        row = col = 0
        for pic in pics:
            pic_label =  QtWidgets.QLabel()
            pixmap = QPixmap(pic)
            pic_width, pic_height = 120, 120
            pic_size = QSize(pic_width, pic_height)
            pixmap = pixmap.scaled(pic_size, flags)
            pic_label.setPixmap(pixmap)
            self.gridLayout.addWidget(pic_label, row, col)
            pic_label.show()
            col += 1
            if col % imagesPerRow == 0:
                row += 1
                col = 0

    def get_image(self, path, width=3*inch, alignement='LEFT'):
        img = utils.ImageReader(path)
        iw, ih = img.getSize()
        aspect = ih / float(iw)
        final_im = Image(path, width=width, height=(width * aspect))
        final_im.hAlign = alignement
        return final_im

    def generate_reqPiece_PDF(self, part_im_paths):
        self.reqforms_directory = os.path.join(os.environ["HOMEPATH"], "Desktop", "Requisitions")
        # directory =  os.path.join(os.path.expandvars('$HOME'), 'Desktop', 'Réquisitions')
        if not os.path.exists(self.reqforms_directory):
            os.makedirs(self.reqforms_directory)

        outfilename = "requisition_"+self.cat_equip_label.text()+"_"+self.cat_piece_label.text()+"_"+self.ID_label.text()+".pdf"
        outfilepath = os.path.join(self.reqforms_directory, outfilename)
        doc = SimpleDocTemplate(outfilepath, pagesize=letter,
                        rightMargin=72, leftMargin=72, 
                        topMargin=36, bottomMargin=18)
        Story = []

        Logo_HHA = self.get_image("Images\\Logo_HHA.jpg",  width=2.5*inch, alignement='LEFT')
        
        # dead code to test again, do not remove
        '''
        table_style = TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT')
            # ('ALIGN', (1, 0), (1, 0), 'RIGHT')
        ])

        # Logo_PC2 = self.get_image("Images\\Logo_PC2_extended.png", width=1.5*inch, alignement='RIGHT')
        tbl_data = [
            [Logo_HHA]
        ]
        tbl = Table(tbl_data)
        # tbl.setStyle(table_style)
        '''
        
        Story.append(Logo_HHA)
        
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        # title
        centered_title = ParagraphStyle(name="centeredStyle", alignment=TA_CENTER, fontName="Helvetica-Bold")
        Story.append(Spacer(4, 12))
        ptext = '<font size=16>%s</font>' % "Formulaire de réquisition de pièce"
        Story.append(Paragraph(ptext, style=centered_title))
        Story.append(Spacer(4, 12))

        sub_title = ParagraphStyle(name="centeredStyle", alignment=TA_LEFT, fontName="Helvetica-Bold")

        # Equipement
        ptext = '<font size=12>%s</font>' % self.equipement_title_label.text() + ':'
        Story.append(Paragraph(ptext, style=sub_title))
        Story.append(Spacer(1, 12))

        ptext = '<font size=10>%s</font>' % self.ID_title_label.text() + ' ' + self.ID_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.cat_equip_title_label.text() + ' ' + self.cat_equip_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.marque_title_label.text() + ' ' + self.marque_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.modele_title_label.text() + ' ' + self.modele_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.unite_title_label.text() + ' ' + self.unite_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.salle_title_label.text() + ' ' + self.salle_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.nom_tech_title_label.text() + ' ' + self.nom_tech_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.date_title_label.text() + ' ' + self.date_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(2, 12))

        # Part
        ptext = '<font size=12>%s</font>' % self.piece_associee_title_label.text() + ':'
        Story.append(Paragraph(ptext, style=sub_title))
        Story.append(Spacer(1, 12))

        ptext = '<font size=10>%s</font>' % self.cat_piece_title_label.text() + ' ' + self.cat_piece_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.nom_piece_title_label.text() + ' ' + self.nom_piece_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.nbr_unites_title_label.text() + ' ' + self.nbr_unites_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.desc_situation_title_label.text() + ' ' + self.desc_situation_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.desc_intervention_title_label.text() + ' ' + self.desc_intervention_label.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=10>%s</font>' % self.pages_manuel_label.text() + ' ' + self.pages_manuel_lineEdit.text()
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(2, 12))

        # image
        ptext = '<font size=12>%s</font>' % self.photo_piece_title_label.text()
        Story.append(Paragraph(ptext, style=sub_title))
        Story.append(Spacer(1, 12))
        if not part_im_paths:
            doc.build(Story)
        else:
            try:
                for path in part_im_paths:
                    Story.append(self.get_image(path, width=5*inch))
                    Story.append(Spacer(1, 12))
                doc.build(Story)
            except IOError:
                self.notify_file_opened()
        self.merge_reqForms()

    # refactor!
    # remove logos everywhere beside the first 
    def merge_reqForms(self):
        output_path = os.path.join(os.environ["HOMEPATH"], "Desktop", "Requisitions", "Requisitions.pdf")
        pdf_merger = PdfFileMerger()
    
        for path in glob.glob(os.path.join(self.reqforms_directory, '*.pdf')):
            pdf_merger.append(os.path.join(os.environ["HOMEPATH"], "Desktop", "Requisitions", path))
    
        with open(output_path, 'wb') as fileobj:
            pdf_merger.write(fileobj)

    def compress_pdf(self, pdf_path):
        pass
