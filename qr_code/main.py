import PySimpleGUI as sg
import qrcode
from io import BytesIO

RES = WIDTH, HEIGHT = 400, 500


class MyQR:
    def __init__(self, box_size: int, border: int, fill_color: str, back_color: str):
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color

    def create_qr(self, data):
        qr = qrcode.QRCode(box_size=self.box_size, border=self.border)

        try:
            qr.add_data(data)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
            qr_image.thumbnail((WIDTH, WIDTH))

            img_bytesio = BytesIO()
            qr_image.save(img_bytesio)
            img_bytes = img_bytesio.getvalue()

            return img_bytes

        except Exception as e:
            print(f"Error: {e}")


def main():
    img_bytes: None | bytes = None
    qr = MyQR(10, 2, "#202020", "#DFDFDF")

    layout = [
        [sg.Text()],
        [sg.Text("QR Code Text:", font="Sans 14"), sg.InputText(key="data", size=(30, 1), font="Sans 12")],
        [sg.Button("Generate QR Code", font="Sans 12"), sg.Button("Exit", font="Sans 12"), sg.Button("Download QR Code", visible=False, font="Sans 12")],
        [sg.Image(key="image")]
    ]

    window = sg.Window("QR Code Generator", layout, size=RES, element_justification="center")

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        elif event == "Generate QR Code":
            data = values["data"]
            if data:
                img_bytes = qr.create_qr(data)
                window["image"].update(data=img_bytes)

                window["Download QR Code"].update(visible=True)

        elif event == "Download QR Code" and img_bytes:
            filename = sg.popup_get_file('Save Image', save_as=True, default_extension=".png")

            if filename:
                with open(filename, "wb") as file:
                    file.write(img_bytes)

    window.close()


if __name__ == '__main__':
    main()
