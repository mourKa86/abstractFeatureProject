from PyQt5.QtWidgets import QApplication
from controller.mainController import MainController
from view.mainView import MainWindow

import sys
import os

def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_controller = MainController()
        self.main_view = MainWindow(self.main_controller)

        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
