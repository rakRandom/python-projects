from PIL import Image


def run():
    resolution = 300

    image = Image.open(input("file path: ")).convert('L')
    w, h = image.size

    if resolution != 0:
        image = image.resize((int(resolution * w / h) * 2, resolution))
        w, h = image.size

    text = ""

    for y in range(h):
        for x in range(w):
            pixel_value = image.getpixel((x, y))

            if pixel_value < 20:
                text += " "
            elif pixel_value < 40:
                text += "."
            elif pixel_value < 60:
                text += ","
            elif pixel_value < 80:
                text += "-"
            elif pixel_value < 100:
                text += "~"
            elif pixel_value < 120:
                text += ":"
            elif pixel_value < 140:
                text += ";"
            elif pixel_value < 160:
                text += "="
            elif pixel_value < 180:
                text += "!"
            elif pixel_value < 200:
                text += "*"
            elif pixel_value < 220:
                text += "#"
            elif pixel_value < 240:
                text += "$"
            else:
                text += "@"
        text += "\n"

    with open('output.txt', 'w') as file:
        file.write(text)


if __name__ == '__main__':
    run()
