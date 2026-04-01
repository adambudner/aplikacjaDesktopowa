import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QTableWidget, QLabel, 
                             QLineEdit, QGroupBox, QHeaderView, QMessageBox)
from db import WypozyczalniaGier

wypozyczalniaDB = WypozyczalniaGier()


class WypozyczalniaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zarządzanie Wypożyczalnią Gier")
        self.resize(950, 600)
        
        # Główny widget okna
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Główny układ poziomy (dzieli okno na lewą i prawą stronę)
        main_layout = QHBoxLayout(central_widget)
        
        # ==========================================
        # LEWA STRONA: TABELA WYPOŻYCZEŃ
        # ==========================================
        left_layout = QVBoxLayout()
        
        lbl_tabela = QLabel("<b>Aktualne wypożyczenia:</b>")
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["ID Wypoż.", "Gra", "Klient", "Data od"])
        # Rozciągnięcie kolumn na całą szerokość tabeli
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.btn_refresh = QPushButton("🔄 Odśwież widok")
        self.btn_refresh.setMinimumHeight(40)
        self.btn_refresh.clicked.connect(self.akcja_odswiez)
        
        left_layout.addWidget(lbl_tabela)
        left_layout.addWidget(self.tabela)
        left_layout.addWidget(self.btn_refresh)
        
        # ==========================================
        # PRAWA STRONA: PANELE STEROWANIA
        # ==========================================
        right_layout = QVBoxLayout()
        right_layout.setSpacing(15) # Odstępy między grupami
        
        # --- GRUPA 1: ZARZĄDZANIE WYPOŻYCZENIAMI ---
        group_wypozyczenia = QGroupBox("Zarządzanie Wypożyczeniami")
        layout_wyp = QVBoxLayout()
        
        # Dodaj wypożyczenie
        layout_wyp.addWidget(QLabel("Dodaj nowe wypożyczenie:"))
        self.inp_wyp_id_gry = QLineEdit()
        self.inp_wyp_id_gry.setPlaceholderText("ID Gry...")
        self.inp_wyp_imie = QLineEdit()
        self.inp_wyp_imie.setPlaceholderText("Imię i nazwisko klienta...")
        self.btn_dodaj_wyp = QPushButton("Wypożycz grę")
        self.btn_dodaj_wyp.clicked.connect(self.akcja_dodaj_wypozyczenie)
        
        layout_wyp.addWidget(self.inp_wyp_id_gry)
        layout_wyp.addWidget(self.inp_wyp_imie)
        layout_wyp.addWidget(self.btn_dodaj_wyp)
        
        # Oddzielenie wizualne
        layout_wyp.addSpacing(10)
        
        # Usuń wypożyczenie / Zgłoś zwrot
        layout_wyp.addWidget(QLabel("Zakończ/Usuń wypożyczenie:"))
        self.inp_usun_wyp_id = QLineEdit()
        self.inp_usun_wyp_id.setPlaceholderText("ID Wypożyczenia lub ID Gry...")
        self.btn_usun_wyp = QPushButton("Usuń wypożyczenie (Zwrot)")
        self.btn_usun_wyp.clicked.connect(self.akcja_usun_wypozyczenie)
        
        layout_wyp.addWidget(self.inp_usun_wyp_id)
        layout_wyp.addWidget(self.btn_usun_wyp)
        group_wypozyczenia.setLayout(layout_wyp)
        
        # --- GRUPA 2: ZARZĄDZANIE ASORTYMENTEM (GRY) ---
        group_gry = QGroupBox("Zarządzanie Baza Gier")
        layout_gry = QVBoxLayout()
        
        # Dodaj grę
        layout_gry.addWidget(QLabel("Dodaj nową grę do bazy:"))
        self.inp_dodaj_tytul = QLineEdit()
        self.inp_dodaj_tytul.setPlaceholderText("Tytuł gry...")
        self.inp_dodaj_platforma = QLineEdit()
        self.inp_dodaj_platforma.setPlaceholderText("Platforma (np. PC, PS5)...")
        self.btn_dodaj_gre = QPushButton("Dodaj grę")
        self.btn_dodaj_gre.clicked.connect(self.akcja_dodaj_gre)
        
        layout_gry.addWidget(self.inp_dodaj_tytul)
        layout_gry.addWidget(self.inp_dodaj_platforma)
        layout_gry.addWidget(self.btn_dodaj_gre)
        
        # Oddzielenie wizualne
        layout_gry.addSpacing(10)
        
        # Usuń grę
        layout_gry.addWidget(QLabel("Usuń grę z bazy trwale:"))
        self.inp_usun_gry_id = QLineEdit()
        self.inp_usun_gry_id.setPlaceholderText("ID Gry do usunięcia...")
        self.btn_usun_gre = QPushButton("Usuń grę")
        self.btn_usun_gre.setStyleSheet("background-color: #ffcccc;") # Lekko czerwony przycisk ostrzegawczy
        self.btn_usun_gre.clicked.connect(self.akcja_usun_gre)
        
        layout_gry.addWidget(self.inp_usun_gry_id)
        layout_gry.addWidget(self.btn_usun_gre)
        group_gry.setLayout(layout_gry)
        
        # Dodawanie grup do prawego panelu
        right_layout.addWidget(group_wypozyczenia)
        right_layout.addWidget(group_gry)
        right_layout.addStretch() # Wypycha panele do góry, żeby nie latały po całym ekranie
        
        # ==========================================
        # ŁĄCZENIE POŁÓWEK OKNA
        # ==========================================
        main_layout.addLayout(left_layout, stretch=2) # Tabela zajmuje 2/3 szerokości
        main_layout.addLayout(right_layout, stretch=1) # Formularze zajmują 1/3 szerokości


    # ==========================================
    # METODY (LOGIKA PRZYCISKÓW)
    # ==========================================
    
    def akcja_odswiez(self):
        print("Akcja: Odświeżam tabelę...")
        wypozyczalniaDB.pobierz_aktywne_wypozyczenia()
        QMessageBox.information(self, "Info", "Tabela odświeżona! (Tutaj podepnij pobieranie z bazy)")

    def akcja_dodaj_wypozyczenie(self):
        id_gry = self.inp_wyp_id_gry.text()
        imie = self.inp_wyp_imie.text()
        print(f"Akcja: Dodaj wypożyczenie -> Gra ID: {id_gry}, Klient: {imie}")
        
        wypozyczalniaDB.wypozycz_gre(imie, id_gry)
        
        self.inp_wyp_id_gry.clear()
        self.inp_wyp_imie.clear()

    def akcja_usun_wypozyczenie(self):
        id_wyp = self.inp_usun_wyp_id.text()
        print(f"Akcja: Usuń wypożyczenie (Zwrot) -> ID: {id_wyp}")
        
        wypozyczalniaDB.zwroc_gre(id_wyp)
        
        self.inp_usun_wyp_id.clear()

    def akcja_dodaj_gre(self):
        tytul = self.inp_dodaj_tytul.text()
        platforma = self.inp_dodaj_platforma.text()
        print(f"Akcja: Dodaj grę -> Tytuł: {tytul}, Platforma: {platforma}")
        
        wypozyczalniaDB.dodaj_gre(tytul, platforma)
        
        self.inp_dodaj_tytul.clear()
        self.inp_dodaj_platforma.clear()

    def akcja_usun_gre(self):
        id_gry = self.inp_usun_gry_id.text()
        print(f"Akcja: Usuń grę -> ID: {id_gry}")
        
        wypozyczalniaDB.usun_gre(id_gry)
        
        self.inp_usun_gry_id.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    
    # Ustawienie prostego, jasnego stylu aplikacji (opcjonalne)
    app.setStyle("Fusion")
    
    okno = WypozyczalniaApp()
    okno.show()
    sys.exit(app.exec())