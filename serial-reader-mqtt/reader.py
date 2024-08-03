# 240803 TDB
# read temp/humidity from Arduino Serial port (USB), 
# add timestamp and post to MQTT
# indentation is four spaces for each level
# TODO: finding the correct COM port will be a pain.  How?
import serial

# TODO: look in /dev/*usb* and pick first one
# TODO: accept device path as an arg
COM = "/dev/tty.usbserial-A700fjTa"

# Set up the serial connection
# ser = serial.Serial('COM3', 9600)  
ser = serial.Serial(COM, 115200)  

# Read data from the serial port
while True:
    data = ser.readline().decode().strip()  # Read a line and decode it
    print(data)
