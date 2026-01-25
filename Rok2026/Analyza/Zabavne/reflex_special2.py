import pygame
import random
import time
import sys
import os

pygame.init()

# --- Nastavenia okna ---
SIRKA = 600
VYSKA = 400
OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Klikni na cieľ – reflexová hra")

# --- Farby ---
BIELA = (255, 255, 255)
POZADIE = (40, 40, 40)

# --- Fonty ---
font = pygame.font.SysFont("arial", 32)
font_maly = pygame.font.SysFont("arial", 24)

# --- Herné nastavenia ---
POCET_KOL = 10
RADIUS = 25
CASOVY_LIMIT = 1.2  # sekundy na kliknutie


def nahodna_farba():
    return (
        random.randint(80, 255),
        random.randint(80, 255),
        random.randint(80, 255)
    )


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


def uloz_rekord(cas):
    subor = "rekordy.txt"
    with open(subor, "a", encoding="utf-8") as f:
        f.write(f"{cas:.3f}\n")


def nacitaj_rekord():
    subor = "rekordy.txt"
    if not os.path.exists(subor):
        return None
    with open(subor, "r", encoding="utf-8") as f:
        hodnoty = [float(x.strip()) for x in f.readlines() if x.strip()]
    return min(hodnoty) if hodnoty else None


def menu():
    while True:
        OKNO.fill(POZADIE)

        nadpis = font.render("Klikni na cieľ", True, BIELA)
        OKNO.blit(nadpis, (SIRKA//2 - nadpis.get_width()//2, 80))

        tlacitko = pygame.Rect(SIRKA//2 - 100, 180, 200, 60)
        pygame.draw.rect(OKNO, (100, 160, 240), tlacitko, border_radius=10)

        text = font_maly.render("Hrať", True, BIELA)
        OKNO.blit(text, (tlacitko.x + 70, tlacitko.y + 18))

        rekord = nacitaj_rekord()
        if rekord is not None:
            txt = font_maly.render(
                f"Najlepší čas: {rekord:.3f} s", True, BIELA)
            OKNO.blit(txt, (SIRKA//2 - txt.get_width()//2, 260))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tlacitko.collidepoint(event.pos):
                    return


def hra():
    odpoctavanie()

    kolo = 0
    reakcie = []
    ciel_x, ciel_y = nahodna_pozicia()
    farba_ciela = nahodna_farba()
    start_casu = time.time()
    posledna_reakcia = None
    animacia_timer = 0

    while True:
        OKNO.fill(POZADIE)

        # --- Koniec hry ---
        if kolo >= POCET_KOL:
            celkovy_cas = sum(reakcie)
            priemer = celkovy_cas / POCET_KOL

            uloz_rekord(priemer)

            text1 = font.render("Hotovo!", True, BIELA)
            text2 = font_maly.render(
                f"Celkový čas: {celkovy_cas:.3f} s", True, BIELA)
            text3 = font_maly.render(f"Priemer: {priemer:.3f} s", True, BIELA)

            OKNO.blit(text1, (SIRKA//2 - text1.get_width()//2, 120))
            OKNO.blit(text2, (SIRKA//2 - text2.get_width()//2, 180))
            OKNO.blit(text3, (SIRKA//2 - text3.get_width()//2, 220))

            pygame.display.update()
            continue

        # --- Časový limit ---
        if time.time() - start_casu > CASOVY_LIMIT:
            reakcie.append(CASOVY_LIMIT)
            posledna_reakcia = CASOVY_LIMIT
            kolo += 1
            if kolo < POCET_KOL:
                ciel_x, ciel_y = nahodna_pozicia()
                farba_ciela = nahodna_farba()
                start_casu = time.time()

        # --- Animácia zásahu ---
        if animacia_timer > 0:
            pygame.draw.circle(OKNO, BIELA, (ciel_x, ciel_y), RADIUS + 10)
            animacia_timer -= 1
        else:
            pygame.draw.circle(OKNO, farba_ciela, (ciel_x, ciel_y), RADIUS)

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
                    animacia_timer = 8

                    kolo += 1
                    if kolo < POCET_KOL:
                        ciel_x, ciel_y = nahodna_pozicia()
                        farba_ciela = nahodna_farba()
                        start_casu = time.time()

        pygame.display.update()


def main():
    while True:
        menu()
        hra()


if __name__ == "__main__":
    main()
