from deep_translator import GoogleTranslator


def translate(text, target="sk"):
    return GoogleTranslator(source="auto", target=target).translate(text)


print(translate("Click the Start button to open the menu.", "sk"))
