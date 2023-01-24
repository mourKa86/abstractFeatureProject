from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os
import toml

def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)

class MainWindow(QtWidgets.QWidget):
    def __init__(self, main_controller):
        super().__init__()
        self._main_controller = main_controller
        self._ui = uic.loadUi(relpath('mainWindow.ui'),self)

        settings = toml.decoder.load(relpath("..\\settings.toml"))

        self.velocityFilterApply = settings["filters"].get("velocityFilter").get("apply", False)

        self._ui.filterGroupBox.setVisible(self.velocityFilterApply)

