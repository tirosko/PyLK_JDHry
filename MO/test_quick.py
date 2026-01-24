"""Quick test - spustenie programu bez interakcie"""
import sys
sys.path.insert(0, r'c:\Users\tibor\Documents\ProgramovanieHPZBG9\PyLK_JDHry\MO')

from kocky_zafarby_copy_test import KockaVisualizer # type: ignore

# Test vytvorenia visualizeru
kocka = ('R', 'G', 'B', 'N', 'N', 'N')
viz = KockaVisualizer(kocka)

print("KockaVisualizer vytvorený OK")
print(f"Počet vrcholov: {len(viz.VRCHOLY)}")
print(f"Počet stien: {len(viz.STENY)}")
print(f"Stav kocky: {viz.stav_kocky}")

# Test rotácie
print("\nTest rotácie:")
bod = [1, 1, 1]
rotacia = viz.rotuj_bod(bod, 0.5, 0.5, 0)
print(f"Rotovaný bod: {rotacia}")

# Test projekcie
print("\nTest projekcie:")
proj = viz.projekt_3d_na_2d(rotacia, 800, 600)
print(f"Projektovaný bod: {proj}")
