from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class ReqPiece2PDF():
    def __init__(self):
        self.generatePDF()

    def generatePDF(self):
        doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
        
        Story = []
        logo = "C:\\Users\\Ala-eddine Kamate\\Desktop\\SIMM2.0-DEV\\Interface\\FenetresEnUI\\Images\\Logo_SIMM.png"

        im = Image(logo, 2*inch, 2*inch)
        im.hAlign = 'CENTER'
        Story.append(im)

        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        ptext = '<font size=12>%s</font>' % "hey"

        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))  

        doc.build(Story)           

