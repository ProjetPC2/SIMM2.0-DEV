
from PyQt5 import QtWidgets

from Interface.FenetresEnPython.FenetrePersonnalisableUI import Ui_FenetrePersonnalisable


class FenetrePersonnalisable(Ui_FenetrePersonnalisable):

    def __init__(self, widget):
        self.setupUi(widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFrame = QtWidgets.QWidget()
    ui = FenetrePersonnalisable(MainFrame)
    MainFrame.show()
    sys.exit(app.exec_())
