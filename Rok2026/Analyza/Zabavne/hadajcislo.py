import random


def hadanie_cisla():
    print("🎲 Vitaj v hre Hádaj číslo!")
    tajne_cislo = random.randint(1, 20)
    pokusy = 0

    while True:
        try:
            tip = int(input("Zadaj číslo od 1 do 20: "))
        except ValueError:
            print("❌ Zadaj prosím celé číslo.")
            continue

        pokusy += 1

        if tip < tajne_cislo:
            print("🔼 Skús väčšie číslo.")
        elif tip > tajne_cislo:
            print("🔽 Skús menšie číslo.")
        else:
            print(
                f"🎉 Uhádol si! Číslo bolo {tajne_cislo}. Počet pokusov: {pokusy}")
            break


if __name__ == "__main__":
    hadanie_cisla()
