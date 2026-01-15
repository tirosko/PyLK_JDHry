
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
LOD_R = 15

# Nakreslí červený trojuholník ako loď
lod_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
# Nakreslí červenú kružnicu v strede obrazovky
# Polomer kruhu (veľkosť ponorky)
lod_id2 = c.create_oval(0, 0, 30, 30, outline="blue")

# Premenné „STRED_X“ a „STRED_Y“ obsahujú súradnice stredu obrazovky
STRED_X = SIRKA / 2
STRED_Y = VYSKA / 2
c.move(lod_id, STRED_X, STRED_Y)
c.move(lod_id2, STRED_X, STRED_Y)

# Funkcia „pohyb“ posúva loď na súradnice „x“ a „y“


def pohyb(event):
    x, y = event.x, event.y
    c.move(lod_id, x, y)
    c.move(lod_id2, x, y)
    c.update()


okno.mainloop()
