# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SupportPC2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SupportPC2(object):
    def setupUi(self, SupportPC2):
        SupportPC2.setObjectName("SupportPC2")
        SupportPC2.resize(1572, 800)
        SupportPC2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        SupportPC2.setStyleSheet("background: white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(SupportPC2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutTitre = QtWidgets.QHBoxLayout()
        self.layoutTitre.setObjectName("layoutTitre")
        self.label = QtWidgets.QLabel(SupportPC2)
        self.label.setStyleSheet("background:white;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/PC2_logo.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.layoutTitre.addWidget(self.label)
        self.labelSupportPC2_2 = QtWidgets.QLabel(SupportPC2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelSupportPC2_2.setFont(font)
        self.labelSupportPC2_2.setStyleSheet("background:white;")
        self.labelSupportPC2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSupportPC2_2.setObjectName("labelSupportPC2_2")
        self.layoutTitre.addWidget(self.labelSupportPC2_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutTitre.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layoutTitre)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.logoPC2 = QtWidgets.QLabel(SupportPC2)
        self.logoPC2.setMinimumSize(QtCore.QSize(300, 300))
        self.logoPC2.setSizeIncrement(QtCore.QSize(200, 0))
        self.logoPC2.setText("")
        self.logoPC2.setPixmap(QtGui.QPixmap("Images/PC2.png"))
        self.logoPC2.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPC2.setObjectName("logoPC2")
        self.verticalLayout.addWidget(self.logoPC2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelDescription = QtWidgets.QLabel(SupportPC2)
        self.labelDescription.setStyleSheet("background:white;")
        self.labelDescription.setTextFormat(QtCore.Qt.PlainText)
        self.labelDescription.setWordWrap(True)
        self.labelDescription.setObjectName("labelDescription")
        self.verticalLayout.addWidget(self.labelDescription)
        self.labelContact = QtWidgets.QLabel(SupportPC2)
        self.labelContact.setStyleSheet("background:white;")
        self.labelContact.setObjectName("labelContact")
        self.verticalLayout.addWidget(self.labelContact)
        self.labelBackup = QtWidgets.QLabel(SupportPC2)
        self.labelBackup.setObjectName("labelBackup")
        self.verticalLayout.addWidget(self.labelBackup)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.boutonSupprimerEquipement = QtWidgets.QPushButton(SupportPC2)
        self.boutonSupprimerEquipement.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.boutonSupprimerEquipement.setFont(font)
        self.boutonSupprimerEquipement.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/garbage (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSupprimerEquipement.setIcon(icon)
        self.boutonSupprimerEquipement.setObjectName("boutonSupprimerEquipement")
        self.horizontalLayout_8.addWidget(self.boutonSupprimerEquipement)
        self.boutonSupprimerBon = QtWidgets.QPushButton(SupportPC2)
        self.boutonSupprimerBon.setEnabled(False)
        self.boutonSupprimerBon.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonSupprimerBon.setIcon(icon1)
        self.boutonSupprimerBon.setIconSize(QtCore.QSize(32, 32))
        self.boutonSupprimerBon.setObjectName("boutonSupprimerBon")
        self.horizontalLayout_8.addWidget(self.boutonSupprimerBon)
        self.boutonRinitialiserStatistiques = QtWidgets.QPushButton(SupportPC2)
        self.boutonRinitialiserStatistiques.setEnabled(False)
        self.boutonRinitialiserStatistiques.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/refresh-button-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boutonRinitialiserStatistiques.setIcon(icon2)
        self.boutonRinitialiserStatistiques.setIconSize(QtCore.QSize(24, 24))
        self.boutonRinitialiserStatistiques.setObjectName("boutonRinitialiserStatistiques")
        self.horizontalLayout_8.addWidget(self.boutonRinitialiserStatistiques)
        self.BoutonVerrou = QtWidgets.QPushButton(SupportPC2)
        self.BoutonVerrou.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BoutonVerrou.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #edf2f8, stop: 1 #c8d9ea);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 213, 243);\n"
"}\n"
"")
        self.BoutonVerrou.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/verrou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoutonVerrou.setIcon(icon3)
        self.BoutonVerrou.setObjectName("BoutonVerrou")
        self.horizontalLayout_8.addWidget(self.BoutonVerrou)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(SupportPC2)
        QtCore.QMetaObject.connectSlotsByName(SupportPC2)

    def retranslateUi(self, SupportPC2):
        _translate = QtCore.QCoreApplication.translate
        SupportPC2.setWindowTitle(_translate("SupportPC2", "Form"))
        self.labelSupportPC2_2.setText(_translate("SupportPC2", "Support Projet PC2 - S.I.M.M."))
        self.labelDescription.setText(_translate("SupportPC2", "Projet PC2 est un organisme à but non-lucratif fondé et dirigé par des étudiants de Polytechnique Montréal. Notre mission est de se rendre dans différents pays en développement pour outiller nos bénéficiaires afin qu’ils puissent eux-mêmes contribuer à l’amélioration de la santé, de l’éducation et de l’environnement dans leur pays. Nous tentons de donner une seconde vie au matériel informatique et médical en se rendant sur place pour offrir des formations sur l’utilisation et la maintenance de ces équipements. Notre stratégie est axée sur la maximisation des ressources déjà disponibles et le partage de connaissances. C’est en travaillant en collaboration avec nos bénéficiaires que nous pouvons y arriver. C’est dans le cadre d’une mission médicale, notamment grâce à la collaboration de l’organisme PC2, la croix rouge canadienne et l’hôpital Saint Michel, qu’apparaît le logiciel SIMM. Ce logiciel permet d’inventorier les équipements médicaux de l’hôpital et de faciliter la gestion du département de génie biomédical de l’hôpital Saint Michel de Jacmel en Haiti. La version de S.I.M.M.2.0 actualise la première version du logiciel S.I.M.M. 1.0 implantée en 2015 dans le même établissement. En cliquant sur le lien ci-dessus vous trouverez le manuel d’utilisation du logiciel. Il vous permettra de bénéficier d’une assistance technique ainsi que de vous familiariser aux différentes applications de S.I.M.M.2.0."))
        self.labelContact.setText(_translate("SupportPC2", "Contact : pc2poly@gmail.com"))
        self.labelBackup.setText(_translate("SupportPC2", "Backup : backup.hsmj@gmail.com"))
        self.boutonSupprimerEquipement.setText(_translate("SupportPC2", "Supprimer un\n"
" Équipement"))
        self.boutonSupprimerBon.setText(_translate("SupportPC2", "Supprimer un\n"
"Bon de Travail"))
        self.boutonRinitialiserStatistiques.setText(_translate("SupportPC2", "Réinitialisier les\n"
"  Statistiques"))

