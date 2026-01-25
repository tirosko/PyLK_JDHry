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
pygame.display.set_caption("Klikni na cieľ – hardcore verzia")

# --- Farby ---
BIELA = (255, 255, 255)
POZADIE = (40, 40, 40)

# --- Fonty ---
font = pygame.font.SysFont("arial", 32)
font_maly = pygame.font.SysFont("arial", 24)

# --- Herné nastavenia ---
POCET_KOL = 10
START_RADIUS = 30
RADIUS_DECREASE = 2
CASOVY_LIMIT = 1.2
CASOVY_LIMIT_HARDCORE = 0.7

# --- Zvuky ---
try:
    script_dir = os.path.dirname(__file__)
    zvuk_hit = pygame.mixer.Sound(os.path.join(script_dir, "hit.wav"))
    zvuk_fail = pygame.mixer.Sound(os.path.join(script_dir, "fail.wav"))
    # pygame.mixer.music.load(os.path.join(script_dir, "music.wav"))
    # pygame.mixer.music.play(-1)
except:
    zvuk_hit = None
    zvuk_fail = None


def nahodna_farba():
    return (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255)
    )


def nahodna_farba_hardcore():
    return (
        random.randint(180, 255),
        random.randint(0, 80),
        random.randint(0, 80)
    )


def nahodna_pozicia(radius):
    x = random.randint(radius, SIRKA - radius)
    y = random.randint(radius, VYSKA - radius)
    return x, y


def odpoctavanie():
    for cislo in ["3", "2", "1", "ŠTART"]:
        OKNO.fill(POZADIE)
        text = font.render(cislo, True, BIELA)
        OKNO.blit(text, (SIRKA//2 - text.get_width() //
                  2, VYSKA//2 - text.get_height()//2))
        pygame.display.update()
        time.sleep(1)


def uloz_rekord(cas, hardcore):
    subor = "rekordy_hardcore.txt" if hardcore else "rekordy.txt"
    with open(subor, "a", encoding="utf-8") as f:
        f.write(f"{cas:.3f}\n")


def nacitaj_rekord(hardcore):
    subor = "rekordy_hardcore.txt" if hardcore else "rekordy.txt"
    if not os.path.exists(subor):
        return None
    with open(subor, "r", encoding="utf-8") as f:
        hodnoty = [float(x.strip()) for x in f.readlines() if x.strip()]
    return min(hodnoty) if hodnoty else None


def menu():
    hardcore = False

    while True:
        OKNO.fill(POZADIE)

        nadpis = font.render("Klikni na cieľ", True, BIELA)
        OKNO.blit(nadpis, (SIRKA//2 - nadpis.get_width()//2, 60))

        tl_play = pygame.Rect(SIRKA//2 - 100, 150, 200, 60)
        tl_hardcore = pygame.Rect(SIRKA//2 - 100, 230, 200, 60)

        pygame.draw.rect(OKNO, (100, 160, 240), tl_play, border_radius=10)
        pygame.draw.rect(OKNO, (200, 60, 60), tl_hardcore, border_radius=10)

        OKNO.blit(font_maly.render("Hrať", True, BIELA),
                  (tl_play.x + 70, tl_play.y + 18))
        OKNO.blit(font_maly.render("Hardcore", True, BIELA),
                  (tl_hardcore.x + 50, tl_hardcore.y + 18))

        rekord = nacitaj_rekord(False)
        rekord_hc = nacitaj_rekord(True)

        if rekord:
            OKNO.blit(font_maly.render(
                f"Rekord: {rekord:.3f} s", True, BIELA), (20, 330))
        if rekord_hc:
            OKNO.blit(font_maly.render(
                f"Hardcore rekord: {rekord_hc:.3f} s", True, BIELA), (20, 360))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tl_play.collidepoint(event.pos):
                    return False
                if tl_hardcore.collidepoint(event.pos):
                    return True


def hra(hardcore):
    odpoctavanie()

    kolo = 0
    reakcie = []
    radius = START_RADIUS
    radius_decrease = RADIUS_DECREASE * (2 if hardcore else 1)
    limit = CASOVY_LIMIT_HARDCORE if hardcore else CASOVY_LIMIT

    farba = nahodna_farba_hardcore() if hardcore else nahodna_farba()
    x, y = nahodna_pozicia(radius)
    start = time.time()

    while True:
        OKNO.fill(POZADIE)

        # --- Koniec hry ---
        if kolo >= POCET_KOL:
            priemer = sum(reakcie) / len(reakcie)
            uloz_rekord(priemer, hardcore)

            OKNO.fill(POZADIE)
            OKNO.blit(font.render("Hotovo!", True, BIELA), (240, 120))
            OKNO.blit(font_maly.render(
                f"Priemer: {priemer:.3f} s", True, BIELA), (240, 180))
            OKNO.blit(font_maly.render(
                "Klikni pre návrat do menu", True, BIELA), (180, 220))
            pygame.display.update()

            # Čakanie na kliknutie pre návrat do menu
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return
                time.sleep(0.1)

        # --- Časový limit ---
        if time.time() - start > limit:
            if zvuk_fail:
                zvuk_fail.play()

            if hardcore:
                # okamžitá smrť
                OKNO.blit(font.render("ZLYHAL SI!", True, BIELA), (220, 160))
                pygame.display.update()
                time.sleep(2)
                return

            reakcie.append(limit)
            kolo += 1
            radius -= radius_decrease
            x, y = nahodna_pozicia(radius)
            farba = nahodna_farba_hardcore() if hardcore else nahodna_farba()
            start = time.time()

        # --- Kreslenie cieľa ---
        pygame.draw.circle(OKNO, farba, (x, y), radius)

        # --- Text kola ---
        OKNO.blit(font_maly.render(
            f"Kolo: {kolo+1}/{POCET_KOL}", True, BIELA), (10, 10))

        # --- Udalosti ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if ((mx - x)**2 + (my - y)**2)**0.5 <= radius:
                    if zvuk_hit:
                        zvuk_hit.play()

                    reakcia = time.time() - start
                    reakcie.append(reakcia)

                    kolo += 1
                    radius -= radius_decrease
                    x, y = nahodna_pozicia(radius)
                    farba = nahodna_farba_hardcore() if hardcore else nahodna_farba()
                    start = time.time()
                else:
                    if zvuk_fail:
                        zvuk_fail.play()

        pygame.display.update()


def main():
    while True:
        hardcore = menu()
        hra(hardcore)


if __name__ == "__main__":
    main()
