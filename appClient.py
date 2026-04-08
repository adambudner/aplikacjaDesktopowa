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
imie = "guest"


class MainWindowUi(object):
    def setupUi(self, MainWindow):
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
        
        self.labelTabela = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTabela.setObjectName("labelTabela")
        self.verticalLayoutLeft.addWidget(self.labelTabela)
        
        
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
        
        # wypozyczenia
        self.group_wypozyczenia = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_wypozyczenia.setObjectName("group_wypozyczenia")
        self.layout_wyp = QtWidgets.QVBoxLayout(self.group_wypozyczenia)
        self.layout_wyp.setObjectName("layout_wyp")
        
        # log
        self.label_loguj = QtWidgets.QLabel(parent=self.group_wypozyczenia)
        self.label_loguj.setObjectName("label_loguj")       
        self.layout_wyp.addWidget(self.label_loguj)
        
        self.inp_log = QtWidgets.QLineEdit(parent=self.group_wypozyczenia)
        self.inp_log.setObjectName("inp_log")
        self.layout_wyp.addWidget(self.inp_log)
        
        self.btn_loguj = QtWidgets.QPushButton(parent=self.group_wypozyczenia)
        self.btn_loguj.setObjectName("btn_loguj")
        self.layout_wyp.addWidget(self.btn_loguj)
        
        
        self.labelDodajWyp = QtWidgets.QLabel(parent=self.group_wypozyczenia)
        self.labelDodajWyp.setObjectName("labelDodajWyp")
        self.layout_wyp.addWidget(self.labelDodajWyp)
        
        self.combo_wyszukaj_gre = QtWidgets.QComboBox(parent=self.group_wypozyczenia)
        self.combo_wyszukaj_gre.setEditable(True)
        self.combo_wyszukaj_gre.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.combo_wyszukaj_gre.setObjectName("combo_wyszukaj_gre")
        self.layout_wyp.addWidget(self.combo_wyszukaj_gre)
        
        self.btn_dodaj_wyp = QtWidgets.QPushButton(parent=self.group_wypozyczenia)
        self.btn_dodaj_wyp.setObjectName("btn_dodaj_wyp")
        self.layout_wyp.addWidget(self.btn_dodaj_wyp)
        
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.layout_wyp.addItem(spacerItem)
        
        self.labelUsunWyp = QtWidgets.QLabel(parent=self.group_wypozyczenia)
        self.labelUsunWyp.setObjectName("labelUsunWyp")
        self.layout_wyp.addWidget(self.labelUsunWyp)
        
        self.inp_usun_wyp_id = QtWidgets.QLineEdit(parent=self.group_wypozyczenia)
        self.inp_usun_wyp_id.setObjectName("inp_usun_wyp_id")
        self.layout_wyp.addWidget(self.inp_usun_wyp_id)
        
        self.btn_usun_wyp = QtWidgets.QPushButton(parent=self.group_wypozyczenia)
        self.btn_usun_wyp.setObjectName("btn_usun_wyp")
        self.layout_wyp.addWidget(self.btn_usun_wyp)
        
        self.verticalLayoutRight.addWidget(self.group_wypozyczenia)
        
        # end
        # self.verticalLayoutRight.addWidget(self.group_gry)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayoutRight.addItem(spacerItem2)
        
        self.horizontalLayout.addLayout(self.verticalLayoutRight)
        self.horizontalLayout.setStretch(1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zarządzanie Wypożyczalnią Gier"))
        # lewo
        self.labelTabela.setText(_translate("MainWindow", "<b>Aktualne wypożyczenia:</b>"))
        self.tabela.setHorizontalHeaderLabels(["ID Wypoż.", "Gra", "Klient", "Data od"])
        self.btn_refresh.setText(_translate("MainWindow", "🔄 Odśwież widok")) 
        
        # prawo
        self.label_loguj.setText(_translate("MainWindow", "Zaloguj się:"))
        self.inp_log.setPlaceholderText(_translate("MainWindow", "Wpisz swoje imię..."))
        self.btn_loguj.setText(_translate("MainWindow", "Zaloguj"))
        self.group_wypozyczenia.setTitle(_translate("MainWindow", "Wypożyczanie gier"))
        self.labelDodajWyp.setText(_translate("MainWindow", "Wypożycz:"))
        self.combo_wyszukaj_gre.setPlaceholderText(_translate("MainWindow", "Wpisz tytuł gry, aby wyszukać..."))
        # self.inp_wyp_imie.setPlaceholderText(_translate("MainWindow", "Imię i nazwisko klienta..."))
        self.btn_dodaj_wyp.setText(_translate("MainWindow", "Wypożycz grę"))
        self.labelUsunWyp.setText(_translate("MainWindow", "Zwróć:"))
        self.inp_usun_wyp_id.setPlaceholderText(_translate("MainWindow", "Podaj ID Wypożyczenia (z tabeli)..."))
        self.btn_usun_wyp.setText(_translate("MainWindow", "Zwróć grę"))     
        
class App(QtWidgets.QMainWindow, MainWindowUi):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.setupUi(self)
        
        # autocomplete
        completer = QtWidgets.QCompleter(self.combo_wyszukaj_gre.model())
        completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.combo_wyszukaj_gre.setCompleter(completer)
        
        # akcje guziki
        self.btn_refresh.clicked.connect(self.akcja_odswiez)
        self.btn_loguj.clicked.connect(self.akcja_loguj)
        self.btn_dodaj_wyp.clicked.connect(self.akcja_dodaj_wypozyczenie)
        self.btn_usun_wyp.clicked.connect(self.akcja_usun_wypozyczenie)
        
        self.zaladuj_gry_do_wyszukiwarki()
        self.akcja_odswiez()
        
    def zaladuj_gry_do_wyszukiwarki(self):
        self.combo_wyszukaj_gre.clear()
        self.combo_wyszukaj_gre.addItem("--- Wybierz lub wyszukaj grę ---", None)
        
        gry_z_bazy = wypozyczalniaDB.pobierz_dostepne_gry()
        
        for wiersz in gry_z_bazy:
            id_gry = wiersz[0]
            tytul = wiersz[1]
            platforma = wiersz[2]
            ilosc_info = f" | Sztuk: {wiersz[3]}" if len(wiersz) > 3 else ""
            
            self.combo_wyszukaj_gre.addItem(f"{tytul} ({platforma}){ilosc_info}", id_gry)

    def akcja_odswiez(self):
        wypozyczenia = wypozyczalniaDB.pobierz_aktywne_wypozyczenia_imie(self.imie)
        
        self.tabela.setRowCount(0)
        self.tabela.setRowCount(len(wypozyczenia))
        
        for row_idx, row_data in enumerate(wypozyczenia):
            for col_idx, value in enumerate(row_data):
                self.tabela.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def akcja_loguj(self):
        imie_z_input = self.inp_log.text().strip()
        if not imie_z_input:
            QMessageBox.warning(self, "Błąd", "Wpisz swoje imię, aby się zalogować!")
            return
        
        imie = imie_z_input
        QMessageBox.information(self, "Git", f"Zalogowano jako: {imie}")
        self.inp_log.clear()
        self.akcja_odswiez()

    def akcja_dodaj_wypozyczenie(self):
        id_gry = self.combo_wyszukaj_gre.currentData()
        
        if id_gry is None or not self.imie:
            QMessageBox.warning(self, "Błąd", "Wybierz grę i wpisz imię!")
            return
            
        status, msg = wypozyczalniaDB.wypozycz_gre(self.imie, id_gry)
        
        if status:
            QMessageBox.information(self, "Git", msg)
            self.combo_wyszukaj_gre.setCurrentIndex(0) 
            self.zaladuj_gry_do_wyszukiwarki() 
            self.akcja_odswiez()
        else:
            QMessageBox.warning(self, "Ups", msg)

    def akcja_usun_wypozyczenie(self):
        id_wyp = self.inp_usun_wyp_id.text()
        if not id_wyp:
            return
            
        try:
            wypozyczalniaDB.cursor.execute('SELECT id_gry FROM wypozyczenia WHERE id = ? AND data_zwrotu IS NULL', (id_wyp,))
            wynik = wypozyczalniaDB.cursor.fetchone()
            
            if wynik:
                id_gry = wynik[0]
                data_zwrotu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                wypozyczalniaDB.cursor.execute('''
                    UPDATE wypozyczenia 
                    SET data_zwrotu = ? 
                    WHERE id = ?
                ''', (data_zwrotu, id_wyp))
                
                wypozyczalniaDB.cursor.execute('UPDATE gry SET ilosc = ilosc + 1 WHERE id = ?', (id_gry,))
                
                wypozyczalniaDB.conn.commit()
                
                QMessageBox.information(self, "Git", f"Zwrócono grę (Wypożyczenie ID: {id_wyp}). Zapas zwiększony o 1 szt.")
                self.inp_usun_wyp_id.clear()
                self.zaladuj_gry_do_wyszukiwarki() 
                self.akcja_odswiez()
            else:
                QMessageBox.warning(self, "Błąd", "Nie znaleziono aktywnego wypożyczenia o tym ID!")
        except Exception as e:
            QMessageBox.warning(self, "Błąd", f"Coś poszło nie tak podczas zwrotu: {e}")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    okno = App(imie)
    okno.show()
    sys.exit(app.exec())