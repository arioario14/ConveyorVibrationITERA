
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Documents/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    14.0,
    13.0,
    465.0,
    198.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    14.0,
    208.0,
    465.0,
    393.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    14.0,
    403.0,
    465.0,
    588.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    475.0,
    13.0,
    926.0,
    198.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    475.0,
    208.0,
    926.0,
    393.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=936.0,
    y=13.0,
    width=78.0,
    height=78.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=936.0,
    y=105.0,
    width=78.0,
    height=78.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=475.0,
    y=401.0,
    width=220.0,
    height=80.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=715.8571166992188,
    y=401.0,
    width=213.1428680419922,
    height=80.0
)

canvas.create_text(
    14.0,
    51.0,
    anchor="nw",
    text="0 RPM",
    fill="#000000",
    font=("IstokWeb Regular", 50 * -1)
)

canvas.create_text(
    15.0,
    246.0,
    anchor="nw",
    text="0*C",
    fill="#000000",
    font=("IstokWeb Regular", 50 * -1)
)

canvas.create_text(
    15.0,
    441.0,
    anchor="nw",
    text="x, y, z",
    fill="#000000",
    font=("IstokWeb Regular", 50 * -1)
)

canvas.create_text(
    477.0,
    45.0,
    anchor="nw",
    text="x, y, z",
    fill="#000000",
    font=("IstokWeb Regular", 50 * -1)
)

canvas.create_text(
    475.0,
    232.0,
    anchor="nw",
    text="x, y, z",
    fill="#000000",
    font=("IstokWeb Regular", 50 * -1)
)
window.resizable(False, False)
window.mainloop()
