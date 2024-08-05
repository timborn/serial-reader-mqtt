# 240803 TDB
# read temp/humidity from Arduino Serial port (USB), 
# add timestamp and post to MQTT
# indentation is four spaces for each level
# TODO: finding the correct COM port will be a pain.  How?
import serial
import paho.mqtt.client as mqtt
import time

# TODO: look in /dev/*usb* and pick first one
# TODO: accept device path as an arg
COM = "/dev/tty.usbserial-A700fjTa"
broker="R2D2.local"
port=1883

# must define before use
def on_publish(client,userdata,mid,result, props):
    # print("data published \n")
    pass

# by factoring this out I can establish a persistent connection to broker
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish                     
client.connect(broker,port,60)	# 60 seconds keep-alive

def post_msg(str):
    ret= client.publish("/env/tempsensor1", data)            

# Set up the serial connection
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
    # parse the msg we get
    # expecting: "h=44.6	f=80.6"
    # want: { "hostname":"enviro1","timestamp":873873,"humidity":44.6,"f":80.6}
    # seconds since epoch.  really don't care about the fractional bits
    ts = int(time.time())
    print(f"ts = {ts}")
    post_msg(data)

