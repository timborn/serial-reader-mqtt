# 240803 TDB
# read temp/humidity from Arduino Serial port (USB), 
# add timestamp and post to MQTT
# indentation is four spaces for each level
# TODO: finding the correct COM port will be a pain.  How?
import serial

# Set up the serial connection
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port and 9600 with the baud rate

# Read data from the serial port
while True:
    data = ser.readline().decode().strip()  # Read a line and decode it
    print(data)
