import sys
import os
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

# fix na sciezke bazy - lapie tam gdzie plik py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'wypozyczalnia.sqlite3')

from db import WypozyczalniaGier
wypozyczalniaDB = WypozyczalniaGier(nazwa_bazy=DB_PATH)

class MainWindowUi(QtWidgets.QMainWindow):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # main 
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # lewo
        self.verticalLayoutLeft = QtWidgets.QVBoxLayout()
        self.verticalLayoutLeft.setObjectName("verticalLayoutLeft")
        
        self.tabela = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tabela.setColumnCount(4)
        self.tabela.setObjectName("tabela")
        self.tabela.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.verticalLayoutLeft.addWidget(self.tabela)
        
        self.btn_refresh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_refresh.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayoutLeft.addWidget(self.btn_refresh)
        
        self.horizontalLayout.addLayout(self.verticalLayoutLeft)
        self.horizontalLayout.setStretch(0, 2)
        
        # prawo
        self.verticalLayoutRight = QtWidgets.QVBoxLayout()
        self.verticalLayoutRight.setSpacing(15)
        self.verticalLayoutRight.setObjectName("verticalLayoutRight")
        
        
        
        
        
        # end
        self.verticalLayoutRight.addWidget(self.group_gry)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayoutRight.addItem(spacerItem2)
        
        self.horizontalLayout.addLayout(self.verticalLayoutRight)
        self.horizontalLayout.setStretch(1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # okno = App()
    # okno.show()
    sys.exit(app.exec())