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



ciara=c.create_line(0,0,5,25)
c.pack

okno.mainloop()