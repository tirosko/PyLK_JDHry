"""
Problém: Václav mal kocky s 3 zafarbený stenami (červená, zelená, modrá).
Koľko rôznych typov kociek mohol vytvoriť, ak dva typy sú rovnaké,
keď sa dá jedna kocka otočiť tak, aby vyzerala ako druhá?

Riešenie: Predstavujeme kocku ako pole 6 stien. Generujeme všetky možné
zafarbenia, potom ich rozdelíme do tried podľa rotácií kocky.
"""

from itertools import combinations, permutations


class Kocka:
    """Reprezentácia zafarbenej kocky."""
    
    # Indexy stien: 0=vrch, 1=spodok, 2=predok, 3=zámer, 4=vľavo, 5=vpravo
    # Všetky 24 rotácií kocky (permutácie stien)
    ROTACIE = [
        # Identita a otáčanie okolo osi Z (vrch-spodok)
        (0, 1, 2, 3, 4, 5),  # identita
        (0, 1, 3, 4, 2, 5),  # 90° okolo Z
        (0, 1, 3, 2, 4, 5),  # 180° okolo Z
        (0, 1, 4, 3, 2, 5),  # 270° okolo Z
        
        # Otáčanie okolo osi X (vľavo-vpravo)
        (2, 3, 1, 0, 4, 5),  # 90° okolo X
        (1, 0, 3, 2, 4, 5),  # 180° okolo X
        (3, 2, 0, 1, 4, 5),  # 270° okolo X
        
        # Otáčanie okolo osi Y (predok-zámer)
        (4, 5, 2, 3, 1, 0),  # 90° okolo Y
        (1, 0, 2, 3, 5, 4),  # 180° okolo Y
        (5, 4, 2, 3, 0, 1),  # 270° okolo Y
        
        # Kombinované rotácie
        (2, 3, 5, 4, 0, 1),
        (2, 3, 0, 1, 5, 4),
        (3, 2, 4, 5, 1, 0),
        (3, 2, 1, 0, 5, 4),
        (4, 5, 0, 1, 3, 2),
        (4, 5, 3, 2, 1, 0),
        (5, 4, 1, 0, 3, 2),
        (5, 4, 3, 2, 0, 1),
        (0, 1, 5, 4, 3, 2),
        (2, 3, 4, 5, 0, 1),
        (1, 0, 4, 5, 2, 3),
        (3, 2, 5, 4, 1, 0),
        (4, 5, 2, 3, 0, 1),
        (5, 4, 2, 3, 1, 0),
    ]
    
    @staticmethod
    def je_validna_rotacia(perm):
        """Skontroluje, či je permutácia validnou rotáciou kocky."""
        # Jednoduchá kontrola - validná rotácia by mala zachovať štruktúru
        return len(perm) == 6 and len(set(perm)) == 6
    
    @staticmethod
    def rotuj(stav_kocky, rotacia_idx):
        """Aplikuje rotáciu na stav kocky.
        
        Args:
            stav_kocky: tuple 6 prvkov reprezentujúcich farby stien
            rotacia_idx: index rotácie
            
        Returns:
            Nový stav kocky po rotácii
        """
        rotacia = Kocka.ROTACIE[rotacia_idx]
        return tuple(stav_kocky[rotacia[i]] for i in range(6))
    
    @staticmethod
    def vsetky_rotacie(stav_kocky):
        """Vráti všetky rotácie daného stavu kocky."""
        rotacie = set()
        for i in range(len(Kocka.ROTACIE)):
            rotacia = Kocka.rotuj(stav_kocky, i)
            rotacie.add(rotacia)
        return rotacie
    
    @staticmethod
    def kanonicky_tvar(stav_kocky):
        """Vráti lexikograficky najmenšiu rotáciu (reprezentanta triedy)."""
        rotacie = Kocka.vsetky_rotacie(stav_kocky)
        return min(rotacie)


def generuj_vsetky_zafarby():
    """Generuje všetky možné zafarbenia kocky.
    
    - Vyberieme 3 steny z 6 na zafarbenie
    - Priradíme im farby R (červená), G (zelená), B (modrá)
    - Zvyšné 3 steny zostanú "N" (nezafarbené)
    
    Returns:
        Zoznam všetkých možných stavov kocky
    """
    zafarby = []
    farby = ['R', 'G', 'B']  # Červená, zelená, modrá
    
    # Vyberieme 3 steny z 6 na zafarbenie
    for farbene_steny in combinations(range(6), 3):
        # Pre vybrané steny generujeme všetky permutácie farieb
        for permutacia_farieb in permutations(farby):
            # Vytvoríme stav kocky
            stav = ['N'] * 6  # N = nezafarbená
            for i, sten_idx in enumerate(farbene_steny):
                stav[sten_idx] = permutacia_farieb[i]
            zafarby.append(tuple(stav))
    
    return zafarby


def pocet_skupin():
    """Spočíta počet různych typov kociek podľa rotácií."""
    vsetky_zafarby = generuj_vsetky_zafarby()
    print(f"Celkový počet možných zafarbení: {len(vsetky_zafarby)}")
    
    # Rozdelíme do tried ekvivalencie
    tripendency = {}
    kanonicky_tvary = set()
    
    for zafarby in vsetky_zafarby:
        kanon = Kocka.kanonicky_tvar(zafarby)
        kanonicky_tvary.add(kanon)
        
        if kanon not in tripendency:
            tripendency[kanon] = []
        tripendency[kanon].append(zafarby)
    
    # Výpis niektorých skupín
    print(f"\nPočet rôznych skupín: {len(kanonicky_tvary)}\n")
    
    # Ukážeme ako vyzerajú niektoré skupiny
    print("Príklady ekvivalenčných tried:")
    for i, (kanon, prvky) in enumerate(list(tripendency.items())[:5]):
        print(f"\nSkupina {i+1} (reprezentant: {kanon}):")
        print(f"  Počet prvkov: {len(prvky)}")
        if len(prvky) <= 3:
            for prvok in prvky:
                print(f"    - {prvok}")
        else:
            print(f"    - {prvky[0]}")
            print(f"    - {prvky[1]}")
            print(f"    ... ešte {len(prvky)-2}")
    
    return len(kanonicky_tvary)


if __name__ == "__main__":
    print("=" * 60)
    print("PROBLÉM: Koľko rôznych typov zafarbených kociek?")
    print("=" * 60)
    print("\nPopis:")
    print("- Kocka má 6 stien")
    print("- 3 steny sú zafarbené: červená (R), zelená (G), modrá (B)")
    print("- 3 steny sú nezafarbené (N)")
    print("- Dva typy kociek sú rovnaké, ak sa dá jedna otočiť na druh.")
    print("\n" + "=" * 60)
    
    odpoved = pocet_skupin()
    
    print("\n" + "=" * 60)
    print(f"ODPOVEĎ: Václav mohol vytvoriť {odpoved} RÔZNYCH SKUPÍN")
    print("=" * 60)
