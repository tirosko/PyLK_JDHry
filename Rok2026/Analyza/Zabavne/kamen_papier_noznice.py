import pygame
import random
import sys

pygame.init()

# --- Nastavenia okna ---
SIRKA = 600
VYSKA = 400
OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Kameň – Papier – Nožnice")

# --- Farby ---
BIELA = (255, 255, 255)
CERVENA = (220, 70, 70)
MODRA = (70, 120, 220)
ZELENA = (70, 200, 120)
Cierna = (0, 0, 0)

# --- Fonty ---
font = pygame.font.SysFont("arial", 32)
font_maly = pygame.font.SysFont("arial", 24)

# --- Herné možnosti ---
moznosti = ["kamen", "papier", "noznice"]


def nakresli_tlacidlo(text, x, y, sirka, vyska, farba):
    pygame.draw.rect(OKNO, farba, (x, y, sirka, vyska), border_radius=10)
    napis = font_maly.render(text, True, BIELA)
    OKNO.blit(napis, (x + sirka//2 - napis.get_width() //
              2, y + vyska//2 - napis.get_height()//2))
    return pygame.Rect(x, y, sirka, vyska)


def vyhodnot(hrac, pc):
    if hrac == pc:
        return "Remíza"
    if (hrac == "kamen" and pc == "noznice") or \
       (hrac == "papier" and pc == "kamen") or \
       (hrac == "noznice" and pc == "papier"):
        return "Vyhral si!"
    return "Prehral si!"


def main():
    vysledok = ""
    pc_volba = ""

    while True:
        OKNO.fill((40, 40, 40))

        # Nadpis
        nadpis = font.render("Kameň – Papier – Nožnice", True, BIELA)
        OKNO.blit(nadpis, (SIRKA//2 - nadpis.get_width()//2, 20))

        # Tlačidlá
        tl_kamen = nakresli_tlacidlo("Kameň", 50, 120, 150, 60, MODRA)
        tl_papier = nakresli_tlacidlo("Papier", 225, 120, 150, 60, ZELENA)
        tl_noznice = nakresli_tlacidlo("Nožnice", 400, 120, 150, 60, CERVENA)

        # Zobrazenie výsledku
        if pc_volba:
            text_pc = font_maly.render(
                f"Počítač: {pc_volba.capitalize()}", True, BIELA)
            OKNO.blit(text_pc, (SIRKA//2 - text_pc.get_width()//2, 220))

        if vysledok:
            text_vysl = font.render(vysledok, True, BIELA)
            OKNO.blit(text_vysl, (SIRKA//2 - text_vysl.get_width()//2, 270))

        # Udalosti
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                if tl_kamen.collidepoint(mx, my):
                    hrac = "kamen"
                elif tl_papier.collidepoint(mx, my):
                    hrac = "papier"
                elif tl_noznice.collidepoint(mx, my):
                    hrac = "noznice"
                else:
                    hrac = None

                if hrac:
                    pc_volba = random.choice(moznosti)
                    vysledok = vyhodnot(hrac, pc_volba)

        pygame.display.update()


if __name__ == "__main__":
    main()
