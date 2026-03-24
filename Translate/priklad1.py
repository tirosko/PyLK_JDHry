from deep_translator import GoogleTranslator


def translate(text, target="sk"):
    return GoogleTranslator(source="auto", target=target).translate(text)


print(translate("Click the Start button to open the menu.", "sk"))


def prelozit(target="sk"):
    text = input("Zadajte text na preloženie: ")
    preklad = GoogleTranslator(source="auto", target=target).translate(text)
    print(f"Preklad: {preklad}")


prelozit()
