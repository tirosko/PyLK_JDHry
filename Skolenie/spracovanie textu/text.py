# Hlavolam - Text-based Puzzle Game
# Educational puzzle game for text processing training

import random
import sys

class TextPuzzle:
    """Simple word puzzle game"""
    
    def __init__(self):
        self.puzzles = [
            {
                "question": "Aké slovo sa číta rovnako zľava doprava aj sprava doľava?",
                "answer": "palindrom",
                "hint": "Začína písmenom 'p'"
            },
            {
                "question": "Koľko samohások je v slove 'python'?",
                "answer": "1",
                "hint": "Len jedna: 'o'"
            },
            {
                "question": "Ktoré slovo obsahuje všetky samohlásky (a,e,i,o,u)?",
                "answer": "objednávka",
                "hint": "Skúsiť so slovom s viacerými rôznymi samohláskami"
            },
            {
                "question": "Koľko písmen má slovo 'spracovanie'?",
                "answer": "11",
                "hint": "Počítaj pozorne"
            },
            {
                "question": "Ktoré slovo je opačné ke slovu 'začiatok'?",
                "answer": "koniec",
                "hint": "Koniec vety"
            }
        ]
        self.score = 0
        self.current = 0
    
    def play(self):
        """Main game loop"""
        print("=" * 50)
        print("HLAVOLAM - Textový Puzzle")
        print("=" * 50)
        print(f"Máš {len(self.puzzles)} otázok.\n")
        
        while self.current < len(self.puzzles):
            puzzle = self.puzzles[self.current]
            self.ask_question(puzzle)
            self.current += 1
        
        self.show_results()
    
    def ask_question(self, puzzle):
        """Ask a single question"""
        print(f"\nOtázka {self.current + 1}/{len(self.puzzles)}:")
        print(puzzle["question"])
        
        while True:
            answer = input("Odpoveď: ").strip().lower()
            
            if answer == "hint":
                print(f"Hint: {puzzle['hint']}")
                continue
            elif answer == "skip":
                print(f"Správna odpoveď bola: {puzzle['answer']}")
                break
            elif answer == puzzle["answer"].lower():
                print("✓ Správne!")
                self.score += 1
                break
            else:
                print("✗ Nesprávne. Skúsi znova? (alebo 'hint', 'skip')")
    
    def show_results(self):
        """Display final score"""
        print("\n" + "=" * 50)
        print("Koniec hry!")
        print(f"Tvoj výsledok: {self.score}/{len(self.puzzles)}")
        percentage = (self.score / len(self.puzzles)) * 100
        print(f"Úspešnosť: {percentage:.1f}%")
        
        if percentage == 100:
            print("🎉 Perfektne!")
        elif percentage >= 80:
            print("🎯 Výborný výkon!")
        elif percentage >= 60:
            print("👍 Dobré!")
        else:
            print("💪 Pokús sa znova!")
        print("=" * 50)


def main():
    """Run the game"""
    try:
        game = TextPuzzle()
        game.play()
    except KeyboardInterrupt:
        print("\n\nHra bola prerušená.")
        sys.exit(0)


if __name__ == "__main__":
    main()
