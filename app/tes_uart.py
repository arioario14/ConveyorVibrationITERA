import serial
ser = serial.Serial('/dev/serial0', 115200, timeout=1)
ser.write(b'hello\n')
print(ser.readline())
ser.close()