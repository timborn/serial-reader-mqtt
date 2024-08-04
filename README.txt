Sun Aug  4 06:54:36 MST 2024
----------------------------

I have the temp/humidity sensor on the Arduino, but no wifi or ethernet
to post the measurements to MQTT.  This will read from the serial port, 
gathering the measurements, adding a timestamp and posting to MQTT.

VENV
----
NB we are using Python virtual environments:
NB it is CRITIAL to use python3 to create the env; when in env python == python3
NB even more critical: venv does not xfer between machines, therefore use
git to move code and recreate the venv on each machine you use.
Use "pip freeze > requirements.txt" and "pip install -r requirements.txt"
INSIDE the venv to capture and recreate the dependencies.
Time for a Makefile.

create new venv:
$ python3 -m venv /path/to/new/virtual/environment

activate:
$ source <venv>/bin/activate
$ .      <venv>/bin/activate

deactivate:
$ deactivate

Design
------
TODO: figure out which device the Arduino is on
TODO: accept device path as an argument in case we guess wrong

I run on a mac.  Figuring out the device for the USB serial port would be nice,
but need to accept an answer from command line if I guess wrong.

/dev/*usb* seems to match the USB devices
// we always seem to get pairs for tty & cu.  Can't recall the difference.
/dev/cu.usbserial-*	<-- I see these when Arduino is plugged in
/dev/tty.usbserial-*
/dev/[cu|tty].usbmodem*  <-- I see these when IC-705 is plugged in

I observe that the Arduino resets when I connect to the serial port.
Apparently this is a feature, but we can "fix" this with a 120 Ohm
pull up resistor between RESET and +5V.  Not sure we need it for the 
temp/humidity sketch.

See Also
--------
https://mqtt.org/
https://docs.python.org/3/library/venv.html
