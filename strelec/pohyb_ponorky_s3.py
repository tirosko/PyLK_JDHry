

from tkinter import Tk, Canvas

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
lod_id2 = c.create_oval(0, 0, 30, 30, outline="red")

# Premenné „STRED_X“ a „STRED_Y“ obsahujú súradnice stredu obrazovky
STRED_X = SIRKA / 2
STRED_Y = VYSKA / 2
c.move(lod_id, STRED_X, STRED_Y)
c.move(lod_id2, STRED_X, STRED_Y)

# Ponorka pôjde pri stlačení klávesov takto rýchlo
LOD_RYCH = 10


def hyb_lod(udalost):
    if udalost.keysym == "Up":
        # Ak sa stlačí šípka nahor, obe časti ponorky stúpajú
        c.move(lod_id, 0, -LOD_RYCH)
        c.move(lod_id2, 0, -LOD_RYCH)
    elif udalost.keysym == "Down":
        # Tieto riadky sa aktivujú, ak sa stlačí šípka nadol - ponorka klesá.
        c.move(lod_id, 0, LOD_RYCH)
        c.move(lod_id2, 0, LOD_RYCH)
    elif udalost.keysym == "Left":
        # Ponorka sa po stlačení šípky vľavo hýbe vľavo
        c.move(lod_id, -LOD_RYCH, 0)
        c.move(lod_id2, -LOD_RYCH, 0)
    elif udalost. keysym == "Right":
        # Po stlačení šípky vpravo sa ponorka hýbe vpravo
        c.move(lod_id, LOD_RYCH, 0)
        c.move(lod_id2, LOD_RYCH, 0)


# Prikáže Pythonu, aby spustil „hyb_lod“, keď sa stlačí akýkoľvek kláves
c.bind_all("<Key>", hyb_lod)

okno.mainloop()
