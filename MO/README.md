# Dokumentácia

## KockaVisualizer geometria

KockaVisualizer je nástroj na vizualizáciu geometrie kociek.  
Popis:
- Zobrazuje 3D kocku v izometrickom pohľade.
- Používa súradnice a transformácie pre otočenie a posun.
- Vstupy majú rozmery, farby a pozície, ktoré sa prepočítavajú do 2D projekcie.
- Podporuje interaktívne otáčanie a zoom.

Tento dokument poskytuje základnú orientáciu v použitých princípoch geometrie a algoritmov.

### Stena kocky (STENY) a väzba na vrcholy (VRCHOLY)

Premenná `STENY` v kóde uchováva definíciu každej z šiestich stien kocky.
Každá stena je popísaná **zoznamom štyroch indexov**, ktoré odkazujú priamo na
položky v zozname `VRCHOLY` (vrcholy kocky).

**Ako funguje väzba:**

Každý index v `STENY` musí byť číslo medzi 0 a 7 (pretože `VRCHOLY` má 8 prvkov).
Tieto indexy označujú, ktoré štyri vrcholy tvoria konkrétnu stranu kocky.

```
STENY = [
    [3, 2, 6, 7],    # Top (horná stena)
    [0, 1, 5, 4],    # Bottom (dolná stena)
    [0, 1, 2, 3],    # Front (predná stena)
    [4, 5, 6, 7],    # Back (zadná stena)
    [0, 3, 7, 4],    # Left (ľavá stena)
    [1, 2, 6, 5],    # Right (pravá stena)
]
```

**Príklad väzby – dolná stena:**

Položka `[0, 1, 5, 4]` znamená:
- Vezmeme vrchity z `VRCHOLY` na pozíciách **0, 1, 5 a 4**
- Podľa `VRCHOLY`: 
  - Vrchol 0 = `[-1, -1, -1]` (vľavo-vzadu-dole)
  - Vrchol 1 = `[1, -1, -1]` (vpravo-vzadu-dole)
  - Vrchol 5 = `[1, -1, 1]` (vpravo-vzadu-hore)
  - Vrchol 4 = `[-1, -1, 1]` (vľavo-vzadu-hore)
- Tieto štyri body v priestore tvoria dolnú stranu kocky

**Poradie stien v poli `STENY`:**

1. horná (index 0)
2. dolná (index 1)
3. predná (index 2)
4. zadná (index 3)
5. ľavá (index 4)
6. pravá (index 5)

**Použitie pri kreslení:**

Pri renderovaní kódu:
1. Preiterujeme cez zoznam `STENY`
2. Pre každú stranu berieme jej štyri indexy (napr. `[0, 1, 5, 4]`)
3. Nájdeme súradnice týchto vrcholov v `VRCHOLY`
4. Aplikujeme 3D transformácie (rotácia, projekcia)
5. Nakreslíme polygon so správnou farbou

Takéto mapovanie sa používa aj pri **painterovom algoritme** – zoradzovaní stien
podľa ich vzdialenosti od kamery, aby sa správne prekrývali vzájomne.

### Vrcholy kocky (VRCHOLY)

Premenná `VRCHOLY` uchováva súradnice (x, y, z) všetkých ôsmich vrcholov jednotkovej
kocky. Kľúčová vlastnosť je, že každá súradnica má hodnotu **1 alebo -1**:

```
VRCHOLY = [
    [-1, -1, -1],  # 0
    [ 1, -1, -1],  # 1
    [ 1,  1, -1],  # 2
    [-1,  1, -1],  # 3
    [-1, -1,  1],  # 4
    [ 1, -1,  1],  # 5
    [ 1,  1,  1],  # 6
    [-1,  1,  1],  # 7
]
```

**Prečo ±1?**

Hodnoty ±1 spôsobujú, že sa kocka rozloží **symetricky okolo počiatku súradnicovej
sustavy (0, 0, 0)**:

- **X-os**: od −1 do +1 (šírka = 2)
- **Y-os**: od −1 do +1 (hĺbka = 2)
- **Z-os**: od −1 do +1 (výška = 2)

**Výhody symetrického umiestnenia:**

1. Stred kocky je presne v počiatku (0, 0, 0)
2. Rotácie okolo osí x, y, z sú prirodzené a symetrické
3. Matematika transformácií (rotácia bez dodatočného posunu) je jednoduchšia
4. Ľahšie sa aplikujú rôzne transformácie (zväčšenie, zmena pozície, otočenie)

