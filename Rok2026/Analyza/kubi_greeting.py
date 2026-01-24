from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import os


def create_greeting_image(path="kubi_je_doma.png"):
    w, h = 800, 400
    bg = (180, 220, 255)
    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)

    # simple house
    house_x0, house_y0 = 150, 150
    house_x1, house_y1 = 450, 320
    draw.rectangle([house_x0, house_y0, house_x1, house_y1], fill=(230, 180, 120), outline=(80, 40, 10))
    # roof
    roof = [(house_x0 - 20, house_y0), ((house_x0 + house_x1) // 2, 80), (house_x1 + 20, house_y0)]
    draw.polygon(roof, fill=(150, 50, 40), outline=(80, 30, 20))
    # door
    door_x0, door_y0 = 310, 230
    draw.rectangle([door_x0, door_y0, door_x0 + 40, house_y1], fill=(100, 50, 30))

    # Text: Kubi je doma
    try:
        # try to load a TTF font from system, fallback to default
        font_path = None
        for candidate in ["arial.ttf", "DejaVuSans.ttf"]:
            try:
                ImageFont.truetype(candidate, 48)
                font_path = candidate
                break
            except Exception:
                continue
        if font_path:
            font = ImageFont.truetype(font_path, 64)
        else:
            font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()

    text = "Kubi je doma"
    text_w, text_h = draw.textsize(text, font=font)
    tx = (w - text_w) // 2
    ty = 40
    draw.text((tx, ty), text, fill=(10, 10, 10), font=font)

    img.save(path)
    return path


def show_image_in_window(image_path):
    root = tk.Tk()
    root.title("Pozdrav: Kubi je doma")

    img = Image.open(image_path)
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=tk_img)
    label.pack()

    root.mainloop()


def main():
    out = "kubi_je_doma.png"
    try:
        path = create_greeting_image(out)
    except Exception as e:
        print("Chyba pri vytváraní obrázka. Skontrolujte, či máte nainštalovaný Pillow.")
        print(e)
        return

    print(f"Vytvorený obrázok: {os.path.abspath(path)}")
    try:
        show_image_in_window(path)
    except Exception as e:
        print("Nepodarilo sa zobraziť obrázok v GUI. Skúste otvoriť súbor manuálne.")
        print(e)


if __name__ == "__main__":
    main()
