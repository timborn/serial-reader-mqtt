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
try:
    ser = serial.Serial(COM, 115200)  
except:
    print(f"Unable to open {COM}")
    print("did you 'pip install pyserial' inside venv?")
    exit(1)

# Read data from the serial port
while True:
    data = ser.readline().decode().strip()  # Read a line and decode it
    print(data)
    post_msg()

def post_msg():
    print("posting msg")

### TODO: figure out functions in python and structure this mess
## publish something to MQTT broker on R2D2
## assumes mosquitto is running on R2D2 port 1883
## assume MQTT v5 and paho API v2
#
#import paho.mqtt.client as mqtt
#broker="R2D2.local"
#port=1883
#
## https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html#paho.mqtt.client.Client.on_publish
#def on_publish(client,userdata,mid,result, props):
#    print("data published \n")
#    pass
#client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#client.on_publish = on_publish                     # assign function to callback
#client.connect(broker,port)                        # establish connection
#ret= client.publish("house/bulb1","on")            # publish
