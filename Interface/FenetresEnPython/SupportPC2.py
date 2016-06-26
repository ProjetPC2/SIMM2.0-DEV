# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SupportPC2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SupportPC2UI(object):
    def setupUi(self, SupportPC2):
        SupportPC2.setObjectName("SupportPC2")
        SupportPC2.resize(1350, 1273)
        self.verticalLayout = QtWidgets.QVBoxLayout(SupportPC2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSupportPC2 = QtWidgets.QLabel(SupportPC2)
        self.labelSupportPC2.setMaximumSize(QtCore.QSize(20000, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelSupportPC2.setFont(font)
        self.labelSupportPC2.setAutoFillBackground(False)
        self.labelSupportPC2.setStyleSheet("")
        self.labelSupportPC2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSupportPC2.setObjectName("labelSupportPC2")
        self.verticalLayout.addWidget(self.labelSupportPC2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.logoPC2 = QtWidgets.QLabel(SupportPC2)
        self.logoPC2.setMinimumSize(QtCore.QSize(300, 300))
        self.logoPC2.setSizeIncrement(QtCore.QSize(200, 0))
        self.logoPC2.setText("")
        self.logoPC2.setPixmap(QtGui.QPixmap("../Images/PC2.png"))
        self.logoPC2.setAlignment(QtCore.Qt.AlignCenter)
        self.logoPC2.setObjectName("logoPC2")
        self.verticalLayout.addWidget(self.logoPC2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.labelDescription = QtWidgets.QLabel(SupportPC2)
        self.labelDescription.setTextFormat(QtCore.Qt.PlainText)
        self.labelDescription.setWordWrap(True)
        self.labelDescription.setObjectName("labelDescription")
        self.verticalLayout.addWidget(self.labelDescription)
        self.labelContact = QtWidgets.QLabel(SupportPC2)
        self.labelContact.setObjectName("labelContact")
        self.verticalLayout.addWidget(self.labelContact)

        self.retranslateUi(SupportPC2)
        QtCore.QMetaObject.connectSlotsByName(SupportPC2)

    def retranslateUi(self, SupportPC2):
        _translate = QtCore.QCoreApplication.translate
        SupportPC2.setWindowTitle(_translate("SupportPC2", "Form"))
        self.labelSupportPC2.setText(_translate("SupportPC2", "Support PC2 - Projet S.I.M.M."))
        self.labelDescription.setText(_translate("SupportPC2", "Projet PC2 est un organisme à but non-lucratif fondé et dirigé par des étudiants de Polytechnique Montréal. Notre mission est de se rendre dans différents pays en développement pour outiller nos bénéficiaires afin qu’ils puissent eux-mêmes contribuer à l’amélioration de la santé, de l’éducation et de l’environnement dans leur pays. Nous tentons de donner une seconde vie au matériel informatique et médical en se rendant sur place pour offrir des formations sur l’utilisation et la maintenance de ces équipements. Notre stratégie est axée sur la maximisation des ressources déjà disponibles et le partage de connaissances. C’est en travaillant en collaboration avec nos bénéficiaires que nous pouvons y arriver.\n"
""))
        self.labelContact.setText(_translate("SupportPC2", "Contact : contact@xxx.com"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = SupportPC2UI()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
