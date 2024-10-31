import serial
import time
import os

os.system("sudo usermod -a -G dialout pi")
os.system("sudo chmod 660 /dev/serial1")

# Inisialisasi serial komunikasi untuk TMC2209
uart = serial.Serial(
    port='/dev/serial1',  # UART port on Raspberry Pi (using /dev/serial0)
    baudrate=115200,      # Baudrate untuk TMC2209
    timeout=1
)

# Fungsi untuk mengirim perintah melalui UART
def send_command(command):
    uart.write(command.encode())  # Encode ke bentuk byte dan kirim
    time.sleep(0.1)               # Beri sedikit delay

# Fungsi untuk menerima respon dari TMC2209
def read_response():
    response = uart.read(100)     # Baca data dari UART
    print(f"Response: {response}")
    return response

# Fungsi untuk memulai gerakan motor (CW / CCW)
def move_motor(steps, direction):
    if direction == 'CW':
        command = 'DIR:0\n'  # Set arah ke CW (clockwise)
    else:
        command = 'DIR:1\n'  # Set arah ke CCW (counterclockwise)
    
    send_command(command)      # Kirim perintah arah
    command = f'STEP:{steps}\n'  # Set jumlah langkah
    send_command(command)      # Kirim perintah langkah
    read_response()            # Baca respon dari driver

# Set konfigurasi awal TMC2209 melalui UART
def configure_tmc2209():
    send_command('CURRENT:800\n')    # Set arus motor
    send_command('MICROSTEP:16\n')   # Set resolusi microstepping
    send_command('INTERPOLATE:1\n')  # Aktifkan interpolasi
    send_command('ENABLE:1\n')       # Aktifkan motor
    read_response()                  # Baca respon konfigurasi

# Main program untuk menjalankan motor
try:
    configure_tmc2209()  # Konfigurasi TMC2209
    
    while True:
        # Rotasi motor CW 200 langkah
        move_motor(200, 'CW')
        time.sleep(1)  # Tunggu 1 detik

        # Rotasi motor CCW 200 langkah
        move_motor(200, 'CCW')
        time.sleep(1)  # Tunggu 1 detik

except KeyboardInterrupt:
    # Matikan motor ketika ada KeyboardInterrupt (Ctrl+C)
    send_command('ENABLE:0\n')  # Nonaktifkan motor
    uart.close()
    print("Motor dimatikan dan koneksi UART ditutup.")
