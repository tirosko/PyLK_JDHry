# Analýza programu Memory Puzzle

## 1. Úvod do programu

Memory Puzzle je hra postavená na knižnici Pygame, kde hráč musí nájsť páry identických ikon (rovnaký tvar a farba).

## 2. Konfigurácia hry (Globálne Konštanty)

### Výkon a Okno

- **FPS = 60**: Počet snímok za sekundu (rýchlosť behu)
- **WINDOWWIDTH = 640, WINDOWHEIGHT = 480**: Rozlíšenie okna
- **BOXSIZE = 40**: Veľkosť jedného políčka (40×40 px)
- **GAPSIZE = 10**: Medzera medzi políčkami
- **BOARDWIDTH = 10, BOARDHEIGHT = 7**: Rozmer dosky = 70 políčok (35 párov)
- **REVEALSPEED = 8**: Rýchlosť animácií otváraní/zatvárania
- **XMARGIN, YMARGIN**: Odsadenie dosky od okrajov okna

### Farby a Tvary

**7 dostupných farieb**: Červená, zelená, modrá, žltá, oranžová, fialová, azúrová
**5 dostupných tvarov**: Donut, štvorec, diamant, čiary, ovál

- **Spolu 35 unikátnych kombinácií** (viac ako potrebných 35 párov)

## 3. Hlavná funkcia - Game Loop (main())

Jadro hry, ktoré sa neustále opakuje:

### Fázy

1. **Inicializácia Pygame** - vytvorenie okna a hernej dosky
2. **Herný cyklus** (while True):
   - Vyčistenie a prekreslenie obrazovky
   - **Spracovanie udalostí**:
     - Kľúč ESC = zatvorenie hry
     - Pohyb myši = sledovanie pozície
     - Kliknutie = výber políčka
   - **Logika hry**:
     - Prvé kliknutie na zatvorené políčko → otvorenie + uloženie pozície
     - Druhé kliknutie → porovnanie s prvým
       - **Zhoda**: Ikony zostanú otvorené
       - **Nezhoda**: Čakanie 1 sekúndu + zatvorenie oboch
     - **Víťazstvo**: Všetky 35 párov otvorených → blikajúca animácia → reset dosky

---

## 4. Generovanie hernej dosky

### generateRevealedBoxesData(val)

- Vytvorí 2D pole revealedBoxes[10][7]
- Všetky políčka inicializované na rovnakú hodnotu (True = otvorené, False = zatvorené)
- Sleduje stav jednotlivých políčok počas hry

### getRandomizedBoard()

- Vytvorí všetky možné kombinácie farieb a tvarov
- Z dostupných kombinácií vyber 35 unikátnych párov
- Každú kombináciu zduplikuje (aby existoval pár)
- Zamiešajú sa náhodne
- Vráti 2D pole dosky s (tvar, farba) na každej pozícii

---

## 5. Konverzia súradníc

### leftTopCoordsOfBox(boxx, boxy)

- Premení súradnice dosky (0-9, 0-6) na **pixelové súradnice** na obrazovke
- Zohľadňuje XMARGIN, YMARGIN, BOXSIZE a GAPSIZE
- 
- Vyskúšaj na malom programe

### getBoxAtPixel(x, y)

- **Opačný proces**: Zistí, na ktoré políčko dosky hráč klikol
- Prejde všetky políčka (10×7) a skontroluje, či sa myš nachádza v ich oblasti
- Vráti (boxx, boxy) alebo (None, None)
---
Moje poznámky:  
*V podtate sa snímajú súradnice myši o pracovnej ploche*

---

## 6. Vykresľovanie grafiky

### drawIcon(shape, color, boxx, boxy)

Nakreslí ikonu podľa tvaru a farby:

- **DONUT**: Dva kruhy (vonkajší + vnútorný)
- **SQUARE**: Štvorec
- **DIAMOND**: Diamant (4-uholník)
- **LINES**: Šikmé čiary
- **OVAL**: Oválny tvar

### *drawBoxCovers(board, boxes, coverage)*

- Nakreslí políčka s pokrytím (pre animácie)
- coverage: Počet pixelov pokrytia (0 = otvorené, BOXSIZE = zatvorené)
- Aktualizuje obrazovku a spustí FPS hodiny

### *drawBoard(board, revealed)*

- Nakreslí **celú dosku**
- Pre každé políčko:
  - Zatvorené (revealed[x][y] = False) → Biele políčko
  - Otvorené (revealed[x][y] = True) → Nakreslí ikonu

### *drawHighlightBox(boxx, boxy)*

- Nakreslí **modrý okvás** okolo políčka pod myšou
- Vizuálna spätná väzba pre hráča

---

## 7. Animácie

### revealBoxesAnimation(board, boxesToReveal)

- Animácia **otváraní políčka**
- Postupne zmenšuje pokrytie z BOXSIZE na 0 (v krokoch po REVEALSPEED)
- Vytvorí efekt "skĺzavajúcej" vrstvy

### coverBoxesAnimation(board, boxesToCover)

- Opačný efekt - animácia **zatvárania**
- Postupne zväčšuje pokrytie z 0 na BOXSIZE

### startGameAnimation(board)

- **Úvodná animácia** - postupne otvorí a zatvára všetky políčka
- Rozdelí 70 políčok na skupiny po 8 a animuje ich po poriadku
- Vytvorí vizuálny efekt "prehliadky" dosky

### gameWonAnimation(board)

- **Blikajúca animácia** pri víťazstve
- Pozadie bliká medzi LIGHTBGCOLOR a BGCOLOR 13-krát
- Čakanie 300ms medzi každou zmenou

---

## 8. Pomocné funkcie

|Funkcia|Účel|
|---------|------|
|splitIntoGroupsOf(groupSize, list)|Rozdelí zoznam na menšie skupiny (používa sa v startGameAnimation)|
|getShapeAndColor(board, x, y)|Vráti (tvar, farba) ikony na pozícii|
|hasWon(revealedBoxes)|Skontroluje, či sú **všetky** políčka otvorené (príspevá na víťazstvo)|

---

## 9. Tok hry - Detailný popis

SPUSTENIE PROGRAMU                
          
1. INICIALIZÁCIA         
- Pygame inicializácia
- Generovanie náhodnej dosky
- Všetky políčka zatvorené

2. ÚVODNÁ ANIMÁCIA
- Postupné otvorenie/zatvorenie
- Vizuálny efekt "prehliadky"


3. HLAVNÝ HERNÝ CYKLUS                                 
A) Hráč pohne myšou nad políčko    
→ Modrý okvás (highlight)       
                                  
B) Hráč klikne na zatvorené políčko
- REVEAL ANIMÁCIA               
- - výber uložený              
                                  
C. Hráč klikne na ďalšie políčko
- REVEAL ANIMÁCIA               
- POROVNANIE
                                         
   ZHODA: Ikony sa rovnajú      
   → Políčka zostanú otvorené   
   → Pokračuj s krokom B        
                                
   NEZHODA: Ikony sa nerovnajú  
   → Čakanie 1000ms             
   → COVER ANIMÁCIA             
   → Pokračuj s krokom B

4. SKONTROLUJ VÍŤAZSTVO                               
Sú všetky politička otvorené?           
- NIE: Pokračuj s krokom 3                        
- ÁNO: VYHRAL!              

5. ANIMÁCIA VÍŤAZSTVA
- Blikajúce pozadie (13x)
- Čakanie 2 sekundy  

│ 6. RESET HRY                        │
│ - Nová náhodná doska                │
│ - Všetky políčka zatvorené          │
│ - Návrat na úvodnú animáciu (krok 2)│

(CYKLUS SA OPAKUJE)

---

## 10. Klíčové koncepty

### Dátové štruktúry

- **mainBoard**: 2D pole [10][7] obsahujúce (tvar, farba) pre každé políčko
- **revealedBoxes**: 2D pole [10][7] s hodnotami True (otvorené) / False (zatvorené)
- **icons**: Zoznam všetkých dostupných kombinácií (tvar, farba)

### Stav hry

- **firstSelection**: Uložená pozícia prvého kliknutého políčka
- Slúži na porovnanie s druhým kliknutím

### Ľudský zážitok

- **Highlight** pri pohybe myši → pozná hráč, na čo sa chystá kliknúť
- **Animácie** otváraní/zatvárania → vizuálne spätná väzba
- **Čakanie 1s** pri nezhode → hráč stihne memorovať pozície
- **Blikajúce** pozadie → slávnostný efekt pri víťazstve

---

## Záver

Memory Puzzle je elegantný príklad hry s jednoduchými pravidlami:

- **Cieľ**: Nájsť všetky páry
- **Mechanika**: Klikaj, pamätaj si, porovnávaj
- **Komplexnosť**: Vytvára sa vizuálny zážitok cez animácie a spracovanie udalostí

Program demonštruje kľúčové koncepty objektovo orientovaného programovania a herného development:
✅ Herný cyklus (game loop)  
✅ Spracovanie udalostí (event handling)  
✅ Grafické vykresľovanie (rendering)  
✅ Animácie a časovanie (timing)  
✅ Logika hry (game logic)

