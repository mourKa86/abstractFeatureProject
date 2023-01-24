from PyQt5.QtCore import QObject
from controller.velocityFilter import VelocityFilter

class MainController(QObject):
    def __init__(self):
        super().__init__()

    def applyFilter(self):
        data = []
        filteredData = VelocityFilter(data)