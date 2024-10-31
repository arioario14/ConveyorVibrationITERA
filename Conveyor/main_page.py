from pathlib import Path
import subprocess
import time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from temperature import TemperatureSensor, TemperaturePlotter
from vibration import MPU6050Plotter
from encoder import Encoder

encoder = Encoder(pin_a=17, pin_b=27)

rpm = 0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pi/Documents/Conveyor/assets1/frame0")

def open_page2():
    subprocess.Popen(["python3", "/home/pi/Documents/Conveyor/second_page.py"])
    time.sleep(0.2)
    window.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')
    

def enable_button3_disable_button4():
    button_3["state"] = "normal"  # Mengaktifkan tombol 3
    button_4["state"] = "disabled"  # Menonaktifkan tombol 4

def enable_button4_disable_button3():
    button_4["state"] = "normal"  # Mengaktifkan tombol 4
    button_3["state"] = "disabled" 


window = Tk()

# window.geometry("1024x600")
center_window(window, 1024, 600)
window.configure(bg = "#FFFFFF")

window.title("Conveyor Dasboard")


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
    fill="#FFFFFF",
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
    command=open_page2,
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

rpm_d = canvas.create_text(
    150.0,
    70.0,
    anchor="nw",
    text=f"{rpm} RPM",
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

def update_rpm():
    
    rpm = encoder.calculate_rpm()
    canvas.itemconfig(rpm_d, text=f"{rpm} RPM")
    window.after(1000, update_rpm)
    
try:    
    
    
    while True:

        sensor_temp = TemperaturePlotter(window)
        sensor_accl = MPU6050Plotter(window)
        update_rpm()
        window.resizable(False, False)
        window.mainloop()
except:
    window.destroy()
    
    pass
finally:
    print("Done.")
    encoder.cleanup()
    
