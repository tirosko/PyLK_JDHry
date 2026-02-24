# Dokumentácia

## KockaVisualizer geometria

KockaVisualizer je nástroj na vizualizáciu geometrie kociek.  
Popis:
- Zobrazuje 3D kocku v izometrickom pohľade.
- Používa súradnice a transformácie pre otočenie a posun.
- Vstupy majú rozmery, farby a pozície, ktoré sa prepočítavajú do 2D projekcie.
- Podporuje interaktívne otáčanie a zoom.

Tento dokument poskytuje základnú orientáciu v použitých princípoch geometrie a algoritmov.

### Stena kocky (STENY)

Premenná `STENY` v kóde uchováva definíciu každej z šiestich stien kocky.
Každá stena je popísaná zoznamom štyroch indexov, ktoré odkazujú na
zoznam `VRCHOLY` (vrcholy kocky). indexy 0–7 zodpovedajú konkrétnym
vrcholom jednotkovej kocky. Poradie stien v poli je:

1. horná
2. dolná
3. predná
4. zadná
5. ľavá
6. pravá

Napríklad `[0, 1, 5, 4]` je spodná stena; čísla označujú vrcholy
zo `VRCHOLY`, ktoré tvoria rohy tejto steny. Takéto mapovanie sa používa
pri kreslení polygonov a pri určení poradia zobrazovania (painterov
algoritmus).

