import sys
import os
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'wypozyczalnia.sqlite3')

from db import WypozyczalniaGier
wypozyczalniaDB = WypozyczalniaGier(nazwa_bazy=DB_PATH)

# ui z designera
class Ui_MainWindow(object):
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
        
        # show games btn
        self.btn_show_games = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_show_games.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_show_games.setObjectName("btn_show_games")
        self.verticalLayoutLeft.addWidget(self.btn_show_games)
        
        
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
        
        self.labelDodajWyp = QtWidgets.QLabel(parent=self.group_wypozyczenia)
        self.labelDodajWyp.setObjectName("labelDodajWyp")
        self.layout_wyp.addWidget(self.labelDodajWyp)
        
        # szukajka
        self.combo_wyszukaj_gre = QtWidgets.QComboBox(parent=self.group_wypozyczenia)
        self.combo_wyszukaj_gre.setEditable(True)
        self.combo_wyszukaj_gre.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.combo_wyszukaj_gre.setObjectName("combo_wyszukaj_gre")
        self.layout_wyp.addWidget(self.combo_wyszukaj_gre)
        
        self.inp_wyp_imie = QtWidgets.QLineEdit(parent=self.group_wypozyczenia)
        self.inp_wyp_imie.setObjectName("inp_wyp_imie")
        self.layout_wyp.addWidget(self.inp_wyp_imie)
        
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
        
        # gry
        self.group_gry = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_gry.setObjectName("group_gry")
        self.layout_gry = QtWidgets.QVBoxLayout(self.group_gry)
        self.layout_gry.setObjectName("layout_gry")
        
        self.labelDodajGre = QtWidgets.QLabel(parent=self.group_gry)
        self.labelDodajGre.setObjectName("labelDodajGre")
        self.layout_gry.addWidget(self.labelDodajGre)
        
        self.inp_dodaj_tytul = QtWidgets.QLineEdit(parent=self.group_gry)
        self.inp_dodaj_tytul.setObjectName("inp_dodaj_tytul")
        self.layout_gry.addWidget(self.inp_dodaj_tytul)
        
        self.inp_dodaj_platforma = QtWidgets.QLineEdit(parent=self.group_gry)
        self.inp_dodaj_platforma.setObjectName("inp_dodaj_platforma")
        self.layout_gry.addWidget(self.inp_dodaj_platforma)
        
        self.inp_dodaj_ilosc = QtWidgets.QSpinBox(parent=self.group_gry)
        self.inp_dodaj_ilosc.setObjectName("inp_dodaj_ilosc")
        self.inp_dodaj_ilosc.setMinimum(1)
        self.inp_dodaj_ilosc.setMaximum(999)
        self.inp_dodaj_ilosc.setPrefix("Ilość sztuk: ")
        self.layout_gry.addWidget(self.inp_dodaj_ilosc)
        
        self.btn_dodaj_gre = QtWidgets.QPushButton(parent=self.group_gry)
        self.btn_dodaj_gre.setObjectName("btn_dodaj_gre")
        self.layout_gry.addWidget(self.btn_dodaj_gre)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.layout_gry.addItem(spacerItem1)
        
        self.labelUsunGre = QtWidgets.QLabel(parent=self.group_gry)
        self.labelUsunGre.setObjectName("labelUsunGre")
        self.layout_gry.addWidget(self.labelUsunGre)
        
        # self.inp_usun_gry_id = QtWidgets.QLineEdit(parent=self.group_gry)
        # self.inp_usun_gry_id.setObjectName("inp_usun_gry_id")
        # self.layout_gry.addWidget(self.inp_usun_gry_id)
        # szukajka v.2 usungre
        self.combo_usun_gry = QtWidgets.QComboBox(parent=self.group_wypozyczenia)
        self.combo_usun_gry.setEditable(True)
        self.combo_usun_gry.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.combo_usun_gry.setObjectName("combo_usun_gry")
        self.layout_gry.addWidget(self.combo_usun_gry)
        
        
        self.btn_usun_gre = QtWidgets.QPushButton(parent=self.group_gry)
        self.btn_usun_gre.setObjectName("btn_usun_gre")
        self.layout_gry.addWidget(self.btn_usun_gre)
        
        # Hard reset bazy
        self.btn_hard_reset_baza = QtWidgets.QPushButton(parent=self.group_gry)
        self.btn_hard_reset_baza.setObjectName("btn_hard_reset")
        self.layout_gry.addWidget(self.btn_hard_reset_baza)
        
        self.verticalLayoutRight.addWidget(self.group_gry)
        
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
        self.btn_show_games.setText(_translate("MainWindow", "🎮 Pokaż gry"))
        
        # prawo
        self.group_wypozyczenia.setTitle(_translate("MainWindow", "Zarządzanie Wypożyczeniami"))
        self.labelDodajWyp.setText(_translate("MainWindow", "Dodaj nowe wypożyczenie:"))
        self.combo_wyszukaj_gre.setPlaceholderText(_translate("MainWindow", "Wpisz tytuł gry, aby wyszukać..."))
        self.inp_wyp_imie.setPlaceholderText(_translate("MainWindow", "Imię i nazwisko klienta..."))
        self.btn_dodaj_wyp.setText(_translate("MainWindow", "Wypożycz grę"))
        self.labelUsunWyp.setText(_translate("MainWindow", "Zakończ/Usuń wypożyczenie:"))
        self.inp_usun_wyp_id.setPlaceholderText(_translate("MainWindow", "Podaj ID Wypożyczenia (z tabeli)..."))
        self.btn_usun_wyp.setText(_translate("MainWindow", "Usuń wypożyczenie (Zwrot)"))
        
        # prawo - gry
        self.group_gry.setTitle(_translate("MainWindow", "Zarządzanie Bazą Gier"))
        self.labelDodajGre.setText(_translate("MainWindow", "Dodaj nową grę do bazy:"))
        self.inp_dodaj_tytul.setPlaceholderText(_translate("MainWindow", "Tytuł gry..."))
        self.inp_dodaj_platforma.setPlaceholderText(_translate("MainWindow", "Platforma (np. PC, PS5)..."))
        self.btn_dodaj_gre.setText(_translate("MainWindow", "Dodaj grę"))
        self.labelUsunGre.setText(_translate("MainWindow", "Usuń grę z bazy trwale:"))
        # self.inp_usun_gry_id.setPlaceholderText(_translate("MainWindow", "ID Gry do usunięcia..."))
        self.combo_usun_gry.setPlaceholderText(_translate("MainWindow", "Wpisz tytuł gry do usunięcia..."))
        self.btn_usun_gre.setText(_translate("MainWindow", "Usuń grę"))
        self.btn_hard_reset_baza.setText(_translate("MainWindow", "⚠️ Usuń wszystkie dane ⚠️"))


# glowna apka
class WypozyczalniaApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # autocomplete
        completer = QtWidgets.QCompleter(self.combo_wyszukaj_gre.model())
        completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.combo_wyszukaj_gre.setCompleter(completer)
        
        # akcje guziki
        self.btn_refresh.clicked.connect(self.akcja_odswiez)
        self.btn_show_games.clicked.connect(self.akcja_pokaz_gry)
        self.btn_dodaj_wyp.clicked.connect(self.akcja_dodaj_wypozyczenie)
        self.btn_usun_wyp.clicked.connect(self.akcja_usun_wypozyczenie)
        self.btn_dodaj_gre.clicked.connect(self.akcja_dodaj_gre)
        self.btn_usun_gre.clicked.connect(self.akcja_usun_gre)
        self.btn_hard_reset_baza.clicked.connect(self.akcja_hard_reset_bazy)
        
        self.zaladuj_gry_do_wyszukiwarki()
        self.akcja_odswiez()

    def zaladuj_gry_do_wyszukiwarki(self):
        self.combo_wyszukaj_gre.clear()
        self.combo_wyszukaj_gre.addItem("--- Wybierz lub wyszukaj grę ---", None)
        
        # usun_gry
        self.combo_usun_gry.clear()
        self.combo_usun_gry.addItem("--- Wybierz lub wyszukaj grę do usunięcia ---", None)  
        
        gry_z_bazy = wypozyczalniaDB.pobierz_dostepne_gry()
        
        for wiersz in gry_z_bazy:
            id_gry = wiersz[0]
            tytul = wiersz[1]
            platforma = wiersz[2]
            ilosc_info = f" | Sztuk: {wiersz[3]}" if len(wiersz) > 3 else ""
            
            self.combo_wyszukaj_gre.addItem(f"{tytul} ({platforma}){ilosc_info}", id_gry)
            self.combo_usun_gry.addItem(f"{tytul} ({platforma}){ilosc_info}", id_gry)

    def akcja_odswiez(self):
        wypozyczenia = wypozyczalniaDB.pobierz_aktywne_wypozyczenia()
        
        self.tabela.setRowCount(0)
        self.tabela.setRowCount(len(wypozyczenia))
        
        for row_idx, row_data in enumerate(wypozyczenia):
            for col_idx, value in enumerate(row_data):
                self.tabela.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def akcja_dodaj_wypozyczenie(self):
        id_gry = self.combo_wyszukaj_gre.currentData()
        imie = self.inp_wyp_imie.text()
        
        if id_gry is None or not imie:
            QMessageBox.warning(self, "Błąd", "Wybierz grę i wpisz imię!")
            return
            
        status, msg = wypozyczalniaDB.wypozycz_gre(imie, id_gry)
        
        if status:
            QMessageBox.information(self, "Git", msg)
            self.combo_wyszukaj_gre.setCurrentIndex(0) 
            self.inp_wyp_imie.clear()
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

    def akcja_dodaj_gre(self):
        tytul = self.inp_dodaj_tytul.text()
        platforma = self.inp_dodaj_platforma.text()
        ilosc = self.inp_dodaj_ilosc.value() 
        
        if not tytul or not platforma:
            QMessageBox.warning(self, "Błąd", "Wpisz tytuł i platformę!")
            return
            
        # Zmieniona nazwa funkcji na Twoją
        try:
            status, msg = wypozyczalniaDB.dodaj_gre_z_iloscia(tytul, platforma, ilosc)
            QMessageBox.information(self, "Git", msg)
            
            self.inp_dodaj_tytul.clear()
            self.inp_dodaj_platforma.clear()
            self.inp_dodaj_ilosc.setValue(1) 
            self.zaladuj_gry_do_wyszukiwarki()
        except AttributeError:
            QMessageBox.warning(self, "Błąd", "Upewnij się, że w db.py funkcja naprawdę nazywa się 'dodaj_gra_z_iloscia'!")
        except Exception as e:
            QMessageBox.warning(self, "Błąd", f"Nieudane dodawanie: {e}")

    def akcja_usun_gre(self):
        id_gry = self.combo_usun_gry.currentData()
        if not id_gry:
            return
            
        try:
            wypozyczalniaDB.cursor.execute('DELETE FROM gry WHERE id = ?', (id_gry,))
            wypozyczalniaDB.conn.commit()
            QMessageBox.information(self, "Git", "Gra wyparowała z bazy.")
        except Exception as e:
            QMessageBox.warning(self, "Błąd", f"Coś chrupnęło: {e}")
            
        self.combo_usun_gry.setCurrentIndex(0)
        self.zaladuj_gry_do_wyszukiwarki()
        self.akcja_odswiez()
    
    def akcja_hard_reset_bazy(self):
        confirm = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno chcesz usunąć wszystkie zapisy? Akcja nieodwracalna" "⚠️", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            status, msg = wypozyczalniaDB.hard_reset_bazy()
            if status:
                QMessageBox.information(self, "Usunięto", msg)
                self.zaladuj_gry_do_wyszukiwarki()
                self.akcja_odswiez()
            else:
                QMessageBox.warning(self, "Ups", "Coś poszło nie tak")
    
    def akcja_pokaz_gry(self):
        gry = wypozyczalniaDB.pobierz_dostepne_gry()
        msg = "Dostępne gry:\n\n"
        for gra in gry:
            msg += f"ID: {gra[0]} | Tytuł: {gra[1]} | Platforma: {gra[2]} | Ilość: {gra[3]}\n"
        QMessageBox.information(self, "Dostępne Gry", msg)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    okno = WypozyczalniaApp()
    okno.show()
    sys.exit(app.exec())