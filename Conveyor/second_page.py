from pathlib import Path
import subprocess
import time
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from stepper import StepperController

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Documents/Conveyor/assets2/frame0")

def open_page1():
    subprocess.Popen(["python3", "/home/pi/Documents/Conveyor/main_page.py"])
    time.sleep(0.2)
    window.destroy()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
   
window = Tk()

speed = 500
# speed = 0
direction = "CW" # cw = 12, ccw = 13

def increment():
    global speed
    if speed < 3000:
        speed += 100
        entry_1.delete(0, "end")
        entry_1.insert(0, str(speed))
        stepper.set_stepper_speed(speed) 

def decrement():
    global speed
    if speed <= 3000 and speed > 500:
        speed -= 100
        entry_1.delete(0, "end")
        entry_1.insert(0, str(speed))
        stepper.set_stepper_speed(speed) 

def set_direction(val):
    global direction
    
    if val == 12:
        entry_2.delete(0, "end")
        entry_2.insert(0, "CW")
        direction = "CW"
    elif val == 13:        
        entry_2.delete(0, "end")
        entry_2.insert(0, "CCW")
        direction = "CCW"
        


def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')

# window.geometry("1024x600")
window_width = 1024
window_height = 600
window.resizable(False, False)

# Pusatkan jendela di layar
center_window(window, window_width, window_height)
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
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_page1,
    relief="flat"
)
button_1.place(
    x=881.0,
    y=533.0,
    width=135.0,
    height=59.0
)

canvas.create_rectangle(
    17.0,
    13.0,
    472.0,
    391.0,
    fill="#B8B7B7",
    outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:set_direction(12),
    relief="flat"
)
button_2.place(
    x=369.0,
    y=274.0,
    width=88.0,
    height=88.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:set_direction(13),
    relief="flat"
)
button_3.place(
    x=256.0,
    y=277.0,
    width=88.0,
    height=88.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=increment,
    relief="flat"
)
button_4.place(
    x=32.0,
    y=274.0,
    width=88.00000000000001,
    height=88.00000000000003
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=decrement,
    relief="flat"
)
button_5.place(
    x=145.0,
    y=274.0,
    width=88.00000000000003,
    height=88.00000000000003
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    133.0,
    222.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EAEAEA",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=42.0,
    y=187.0,
    width=182.0,
    height=69.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    356.5,
    222.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EAEAEA",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=266.0,
    y=187.0,
    width=181.0,
    height=69.0
)

canvas.create_text(
    54.0,
    13.0,
    anchor="nw",
    text="CONTROL SPEED AND DIRECTION ",
    fill="#000000",
    font=("IstokWeb Bold", 25 * -1)
)

canvas.create_text(
    93.0,
    154.0,
    anchor="nw",
    text="Speed",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

canvas.create_text(
    302.0,
    154.0,
    anchor="nw",
    text="Direction",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

canvas.create_rectangle(
    494.0,
    13.0,
    949.0,
    391.0,
    fill="#B8B7B7",
    outline="")

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=509.0,
    y=274.0,
    width=88.0,
    height=88.00000000000003
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=622.0,
    y=274.0,
    width=88.0,
    height=88.00000000000003
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=733.0,
    y=274.0,
    width=88.0,
    height=88.00000000000003
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=846.0,
    y=274.0,
    width=88.0,
    height=88.00000000000003
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    610.0,
    222.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EAEAEA",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=519.0,
    y=187.0,
    width=182.0,
    height=69.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    833.5,
    222.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EAEAEA",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=743.0,
    y=187.0,
    width=181.0,
    height=69.0
)

canvas.create_text(
    531.0,
    13.0,
    anchor="nw",
    text="CONTROL MIN AND MAX  TEMPERATURE",
    fill="#000000",
    font=("IstokWeb Bold", 25 * -1)
)

canvas.create_text(
    570.0,
    154.0,
    anchor="nw",
    text="Min",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

canvas.create_text(
    779.0,
    154.0,
    anchor="nw",
    text="Max",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

def update_stepper():
#     global stepper
    stepper.set_stepper_speed(speed, direction)
    window.after(100, update_stepper)

# window.after(100, update_stepper)


try:
    entry_1.delete(0, "end")
    entry_1.insert(0, str(speed))

    entry_2.delete(0, "end")
    entry_2.insert(0, "CW")
    
    stepper = StepperController(cw_pin=12, ccw_pin=13, res_pin=24)
    
    while True:   
        update_stepper()
        window.mainloop()        
except:
    window.destroy()
    stepper.set_stepper_speed(0, direction)
finally:
    stepper.cleanup()
    print("Done.")



