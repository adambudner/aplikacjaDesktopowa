import sys
from PyQt6.QtWidgets import *
    
class App(QWidget):
   def __init__(self):
        super().__init__()
        self.setIf()
        
   def setIf(self):
      self.setWindowTitle('Wypożyczalnia gier')
      self.resize(350, 250)
      
      glowny_uklad = QVBoxLayout()

        # --- PANEL GÓRNY (Odpowiednik JPanel) ---
        # Używamy QFrame, żeby pokazać wizualną ramkę
      panel_gorny = QFrame()
      panel_gorny.setFrameShape(QFrame.Shape.Box) # Ustawiamy styl ramki
        
        # Układ dla panelu górnego (Poziomy, żeby ustawić Label, Input i Przycisk w jednym rzędzie)
      uklad_gorny = QHBoxLayout()
        
        # 1. Label
      self.etykieta = QLabel("Podaj imię:")
      uklad_gorny.addWidget(self.etykieta)
        
        # 2. Input (QLineEdit)
      self.pole_input = QLineEdit()
      self.pole_input.setPlaceholderText("np. Jan") # Wskazówka w tle
      uklad_gorny.addWidget(self.pole_input)
        
        
        # Dodajemy układ poziomy do naszego panelu
      panel_gorny.setLayout(uklad_gorny)
        
        # --- POLE TEKSTOWE NA WYNIKI (TextArea) ---
      self.pole_wynikow = QTextEdit()
      self.pole_wynikow.setReadOnly(True) # Zabezpieczamy, żeby użytkownik nie mógł tam pisać ręcznie
      self.pole_wynikow.append("Witaj! Tutaj będą pojawiać się informacje.")

        # --- SKŁADANIE WSZYSTKIEGO W CAŁOŚĆ ---
      glowny_uklad.addWidget(panel_gorny)   # Dodajemy panel górny
      glowny_uklad.addWidget(self.pole_wynikow) # Dodajemy textarea poniżej

      self.setLayout(glowny_uklad)
      
if __name__ == "__main__":
   app = QApplication(sys.argv)
   okno = App()
   okno.show()
   sys.exit(app.exec())