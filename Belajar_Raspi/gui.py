from pathlib import Path
import RPi.GPIO as pin
from time import sleep
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Documents/Belajar_Raspi/assets/frame0")

LED_PIN = [17, 18, 24, 25, 5, 6, 16, 23, 22, 12, 20, 19]
BLINK_DELAY = 0.5

pin.setwarnings(False)
pin.setmode(pin.BCM)
pin.setup(LED_PIN, pin.OUT)

def led(i):
    pin.output(LED_PIN[i], pin.HIGH)  
    sleep(BLINK_DELAY)             
    pin.output(LED_PIN[i], pin.LOW)    
    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("700x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# BUTTON 1
button_image_1 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=5,
    highlightthickness=0,
    command=lambda: led(0),
    relief="flat"
)
button_1.place(
    x=120.0,
    y=120.0,
    width=100.0,
    height=100.0
)

#button2
button_image_2 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(1),
    relief="flat"
)
button_2.place(
    x=240.0,
    y=120.0,
    width=100.0,
    height=100.0
)

# button 3

button_image_3 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(2),
    relief="flat"
)
button_3.place(
    x=360.0,
    y=120.0,
    width=100.0,
    height=100.0
)

# button4
button_image_4 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(3),
    relief="flat"
)
button_4.place(
    x=480.0,
    y=120.0,
    width=100.0,
    height=100.0
)

# button 5
button_image_5 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(4),
    relief="flat"
)
button_5.place(
    x=120.0,
    y=240.0,
    width=100.0,
    height=100.0
)

#button 6
button_image_6 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(5),
    relief="flat"
)
button_6.place(
    x=240.0,
    y=240.0,
    width=100.0,
    height=100.0
)

# button 7
button_image_7 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(6),
    relief="flat"
)
button_7.place(
    x=360.0,
    y=240.0,
    width=100.0,
    height=100.0
)

# button 8
button_image_8 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(7),
    relief="flat"
)
button_8.place(
    x=480.0,
    y=240.0,
    width=100.0,
    height=100.0
)

# button 9
button_image_9 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(8),
    relief="flat"
)
button_9.place(
    x=120.0,
    y=360.0,
    width=100.0,
    height=100.0
)

# button 10
button_image_10 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(9),
    relief="flat"
)
button_10.place(
    x=240.0,
    y=360.0,
    width=100.0,
    height=100.0
)

# button 11
button_image_11 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(10),
    relief="flat"
)
button_11.place(
    x=360.0,
    y=360.0,
    width=100.0,
    height=100.0
)

# button 12
button_image_12 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: led(11),
    relief="flat"
)
button_12.place(
    x=480.0,
    y=360.0,
    width=100.0,
    height=100.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    82.0,
    fill="#3F508A",
    outline="")

canvas.create_text(
    14.0,
    14.0,
    anchor="nw",
    text="LED CONTROLS",
    fill="#FFFFFF",
    font=("Inter SemiBold", 40 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    658.0,
    40.0,
    image=image_image_1
)
try:
    window.resizable(False, False)
    window.mainloop()
except KeyboardInterrupt:
    window.destroy()
    print("Stop program.")
finally:
    pin.cleanup()

