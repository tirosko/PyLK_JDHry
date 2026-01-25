import pygame
import random
import sys

pygame.init()

# --- Nastavenia okna ---
SIRKA = 500
VYSKA = 600
OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Utekaj pred blokom")

# --- Farby ---
BIELA = (255, 255, 255)
CERVENA = (220, 70, 70)
MODRA = (70, 120, 220)
Cierna = (0, 0, 0)

# --- Hráč ---
hrac_velkost = 40
hrac_x = SIRKA // 2 - hrac_velkost // 2
hrac_y = VYSKA - hrac_velkost - 20
hrac_rychlost = 6

# --- Prekážky ---
prekazka_sirka = 60
prekazka_vyska = 40
prekazky = []
rychlost_prekazok = 4

# --- Font ---
font = pygame.font.SysFont("arial", 32)


def vytvor_prekazku():
    x = random.randint(0, SIRKA - prekazka_sirka)
    y = -prekazka_vyska
    prekazky.append([x, y])


def kresli_hraca():
    pygame.draw.rect(OKNO, MODRA, (hrac_x, hrac_y, hrac_velkost, hrac_velkost))


def kresli_prekazky():
    for x, y in prekazky:
        pygame.draw.rect(OKNO, CERVENA, (x, y, prekazka_sirka, prekazka_vyska))


def pohyb_prekazok():
    global prekazky
    for i in range(len(prekazky)):
        prekazky[i][1] += rychlost_prekazok
    prekazky = [p for p in prekazky if p[1] < VYSKA + 50]


def kolizia(hrac_rect, prekazky):
    for x, y in prekazky:
        if hrac_rect.colliderect(pygame.Rect(x, y, prekazka_sirka, prekazka_vyska)):
            return True
    return False


def main():
    global hrac_x
    clock = pygame.time.Clock()
    spawn_timer = 0
    score = 0

    while True:
        clock.tick(60)
        OKNO.fill((40, 40, 40))

        # --- Udalosti ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Ovládanie hráča ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hrac_x > 0:
            hrac_x -= hrac_rychlost
        if keys[pygame.K_RIGHT] and hrac_x < SIRKA - hrac_velkost:
            hrac_x += hrac_rychlost

        # --- Spawn prekážok ---
        spawn_timer += 1
        if spawn_timer > 40:
            vytvor_prekazku()
            spawn_timer = 0

        # --- Pohyb prekážok ---
        pohyb_prekazok()

        # --- Kreslenie ---
        kresli_hraca()
        kresli_prekazky()

        # --- Skóre ---
        score += 1
        text_score = font.render(f"Skóre: {score}", True, BIELA)
        OKNO.blit(text_score, (10, 10))

        # --- Kolízia ---
        hrac_rect = pygame.Rect(hrac_x, hrac_y, hrac_velkost, hrac_velkost)
        if kolizia(hrac_rect, prekazky):
            game_over = font.render("KONIEC HRY!", True, BIELA)
            OKNO.blit(game_over, (SIRKA//2 - game_over.get_width()//2, VYSKA//2))
            pygame.display.update()
            pygame.time.wait(2000)
            return

        pygame.display.update()


if __name__ == "__main__":
    main()
