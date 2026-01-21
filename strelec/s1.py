# Importuje všetky funkcie v Tkinteri
from tkinter import Tk, Canvas
# Nastaví veľkosť okna
VYSKA = 500
SIRKA = 800

okno = Tk()
# Pomenovanie hry
okno.title("Bublinový strelec")
# Nastaví sa tmavo modrá ako farba pozadia (more)
# Vytvorí grafické plátno, na ktoré sa bude kresliť
c = Canvas(okno, width=SIRKA, height=VYSKA, bg="darkblue")
c.pack()

okno.mainloop()
