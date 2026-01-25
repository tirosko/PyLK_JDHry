import pygame
import random
import time
import sys

pygame.init()

# --- Nastavenia okna ---
SIRKA = 600
VYSKA = 400
OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Klikni na cieľ – reflexová hra")

# --- Farby ---
BIELA = (255, 255, 255)
CERVENA = (230, 80, 80)
ZELENA = (80, 220, 120)
ZLTA = (240, 200, 80)
POZADIE = (40, 40, 40)

# --- Fonty ---
font = pygame.font.SysFont("arial", 32)
font_maly = pygame.font.SysFont("arial", 24)

# --- Herné nastavenia ---
POCET_KOL = 10
RADIUS = 25


def nahodna_pozicia():
    x = random.randint(RADIUS, SIRKA - RADIUS)
    y = random.randint(RADIUS, VYSKA - RADIUS)
    return x, y


def odpoctavanie():
    for cislo in ["3", "2", "1", "ŠTART"]:
        OKNO.fill(POZADIE)
        text = font.render(cislo, True, BIELA)
        OKNO.blit(text, (SIRKA//2 - text.get_width() //
                  2, VYSKA//2 - text.get_height()//2))
        pygame.display.update()
        time.sleep(1)


def farba_podla_reakcie(t):
    if t < 0.25:
        return ZELENA
    if t < 0.45:
        return ZLTA
    return CERVENA


def main():
    odpoctavanie()

    kolo = 0
    reakcie = []
    ciel_x, ciel_y = nahodna_pozicia()
    start_casu = time.time()
    posledna_reakcia = None
    animacia_timer = 0

    while True:
        OKNO.fill(POZADIE)

        # --- Koniec hry ---
        if kolo >= POCET_KOL:
            celkovy_cas = sum(reakcie)
            priemer = celkovy_cas / POCET_KOL

            text1 = font.render("Hotovo!", True, BIELA)
            text2 = font_maly.render(
                f"Celkový čas: {celkovy_cas:.3f} s", True, BIELA)
            text3 = font_maly.render(
                f"Priemerná reakcia: {priemer:.3f} s", True, BIELA)

            OKNO.blit(text1, (SIRKA//2 - text1.get_width()//2, 120))
            OKNO.blit(text2, (SIRKA//2 - text2.get_width()//2, 180))
            OKNO.blit(text3, (SIRKA//2 - text3.get_width()//2, 220))

            pygame.display.update()
            continue

        # --- Animácia zásahu ---
        if animacia_timer > 0:
            pygame.draw.circle(OKNO, farba_podla_reakcie(
                posledna_reakcia), (ciel_x, ciel_y), RADIUS + 10)
            animacia_timer -= 1
        else:
            pygame.draw.circle(OKNO, CERVENA, (ciel_x, ciel_y), RADIUS)

        # --- Text kola ---
        text_kolo = font_maly.render(
            f"Kolo: {kolo + 1}/{POCET_KOL}", True, BIELA)
        OKNO.blit(text_kolo, (10, 10))

        # --- Posledná reakcia ---
        if posledna_reakcia is not None:
            txt = font_maly.render(
                f"Posledná reakcia: {posledna_reakcia:.3f} s", True, BIELA)
            OKNO.blit(txt, (10, 40))

        # --- Udalosti ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                vzdialenost = ((mx - ciel_x)**2 + (my - ciel_y)**2) ** 0.5

                if vzdialenost <= RADIUS:
                    reakcia = time.time() - start_casu
                    reakcie.append(reakcia)
                    posledna_reakcia = reakcia
                    animacia_timer = 10

                    kolo += 1
                    if kolo < POCET_KOL:
                        ciel_x, ciel_y = nahodna_pozicia()
                        start_casu = time.time()

        pygame.display.update()


if __name__ == "__main__":
    main()
