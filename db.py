import sqlite3
from datetime import datetime

class WypozyczalniaGier:
    def __init__(self, nazwa_bazy='./wypozyczalnia.sqlite3'):
        self.conn = sqlite3.connect(nazwa_bazy)
        self.cursor = self.conn.cursor()
        self._inicjalizuj_baze()

    def _inicjalizuj_baze(self):
        self.cursor.execute('PRAGMA foreign_keys = ON')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS gry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tytul TEXT NOT NULL,
                platforma TEXT NOT NULL,
                czy_dostepna INTEGER DEFAULT 1
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS wypozyczenia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_gry INTEGER NOT NULL,
                imie_klienta TEXT NOT NULL,
                data_wypozyczenia TEXT NOT NULL,
                data_zwrotu TEXT,
                FOREIGN KEY (id_gry) REFERENCES gry(id)
            )
        ''')
        self.conn.commit()

    def dodaj_gre(self, tytul, platforma):
        self.cursor.execute('INSERT INTO gry (tytul, platforma) VALUES (?, ?)', (tytul, platforma))
        self.conn.commit()
        return True, f"Dodano grę: {tytul} ({platforma})"

    def pobierz_dostepne_gry(self):
        self.cursor.execute('SELECT id, tytul, platforma FROM gry WHERE czy_dostepna = 1')
        return self.cursor.fetchall()

    def wypozycz_gre(self, imie_klienta, id_gry):
        self.cursor.execute('SELECT czy_dostepna, tytul FROM gry WHERE id = ?', (id_gry,))
        wynik = self.cursor.fetchone()
        
        if not wynik:
            return False, "Błąd: Gra o podanym ID nie istnieje."
        if wynik[0] == 0:
            return False, f"Błąd: Gra '{wynik[1]}' jest już wypożyczona."
            
        data_wypozyczenia = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.cursor.execute('UPDATE gry SET czy_dostepna = 0 WHERE id = ?', (id_gry,))
        self.cursor.execute('''
            INSERT INTO wypozyczenia (id_gry, imie_klienta, data_wypozyczenia) 
            VALUES (?, ?, ?)
        ''', (id_gry, imie_klienta, data_wypozyczenia))
        self.conn.commit()
        
        return True, f"Sukces: {imie_klienta} wypożyczył/a grę '{wynik[1]}'."

    def zwroc_gre(self, id_gry):
        self.cursor.execute('SELECT czy_dostepna FROM gry WHERE id = ?', (id_gry,))
        wynik = self.cursor.fetchone()
        
        if not wynik:
            return False, "Błąd: Gra o podanym ID nie istnieje."
        if wynik[0] == 1:
            return False, "Błąd: Ta gra nie jest obecnie wypożyczona (jest na stanie)."
            
        data_zwrotu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.cursor.execute('UPDATE gry SET czy_dostepna = 1 WHERE id = ?', (id_gry,))
        self.cursor.execute('''
            UPDATE wypozyczenia 
            SET data_zwrotu = ? 
            WHERE id_gry = ? AND data_zwrotu IS NULL
        ''', (data_zwrotu, id_gry))
        self.conn.commit()
        
        return True, f"Sukces: Zwrócono grę o ID {id_gry}."

    def pobierz_aktywne_wypozyczenia(self):
        self.cursor.execute('''
            SELECT w.id, g.tytul, w.imie_klienta, w.data_wypozyczenia 
            FROM wypozyczenia w
            JOIN gry g ON w.id_gry = g.id
            WHERE w.data_zwrotu IS NULL
        ''')
        return self.cursor.fetchall()

    def usun_wszystkie_zapisy(self):
        self.cursor.execute('DELETE FROM wypozyczenia')
        self.cursor.execute('DELETE FROM gry')
        self.conn.commit()
        return True, "Wszystkie zapisy zostały usunięte."

    def zamknij_polaczenie(self):
        self.conn.close()
        
        
if __name__ == "__main__":
    wypozyczalniaTESTMAIN = WypozyczalniaGier()
    # wypozyczalniaTESTMAIN.dodaj_gre("The Legend of Zelda: Breath of the Wild", "Nintendo Switch")
    # wypozyczalniaTESTMAIN.dodaj_gre("God of War", "PlayStation 4")
    # print(wypozyczalniaTESTMAIN.pobierz_dostepne_gry())
    # wypozyczalniaTESTMAIN.wypozycz_gre("Adam", 1)
    # print(wypozyczalniaTESTMAIN.pobierz_aktywne_wypozyczenia())
    # wypozyczalniaTESTMAIN.zwroc_gre(1)
    # print(wypozyczalniaTESTMAIN.pobierz_dostepne_gry())
    # wypozyczalniaTESTMAIN.zamknij_polaczenie()
    
    # print(wypozyczalniaTESTMAIN.usun_wszystkie_zapisy())