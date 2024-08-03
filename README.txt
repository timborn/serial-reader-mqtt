Sat Aug  3 07:46:55 MST 2024
----------------------------

I have the temp/humidity sensor on the Arduino, but no wifi or ethernet
to post the measurements to MQTT.  This will read from the serial port, 
gathering the measurements, adding a timestamp and posting to MQTT.

NB we are using Python virtual environments:
create new venv:
$ python -m venv /path/to/new/virtual/environment

activate:
$ source <venv>/bin/activate
$ .      <venv>/bin/activate

deactivate:
$ deactivate

https://mqtt.org/
https://docs.python.org/3/library/venv.html
