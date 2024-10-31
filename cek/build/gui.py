from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Documents/Conveyor/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_page2():
    # Menjalankan file `page2.py` sebagai proses baru
    subprocess.Popen(["python3", "/home/pi/Documents/Conveyor/page2/build/gui.py"])

window = Tk()
window.geometry("1024x600")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x = 0, y = 0)

# Tombol untuk pindah ke Page 2
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_page2,
    relief="flat"
)
button_1.place(
    x=936.0,
    y=13.0,
    width=78.0,
    height=78.0
)

# Element lain di Page 1

window.resizable(False, False)
window.mainloop()
