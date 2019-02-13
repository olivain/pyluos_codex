# PROJECT MAILLAGE

This project aim to manipulate a Robot based on [Pyluos] (https://www.luos-robotics.com/fr/) Technologies.
The project is running under Python3.

We assembled differents modules together: 
- One [raspberry Zero] (https://www.kubii.fr/pi-zero-v13/1401-raspberry-pi-zero-v13-kubii-3272496006973.html)
- One Wifi module
- Two [Controlled-motors modules] (https://www.luos-robotics.com/en/documentation/controlled-motor/)
- Two [Distance modules] (https://www.luos-robotics.com/en/documentation/distance/)
- One battery

### Creating virtualenv

#### Install virtualenv package:


sudo apt-get install python3 python3-pip virtualenvwrapper


#### Create your virtualenv:

mkvirtualenv -p /usr/bin/python3 <venv-name>


##### Activate your virtualenv:

Workon <venv-name>

### Quickstart

#### Install requirements

pip3 install -r requirements.txt

#### Wifi Settings

To connect your raspberrypi zero to a network, you need the followings parts:
- A micro SD and SD Card adapter, commonly provides with your raspberrypi.
- A computer. We recommand to use free operating system but it's not mandatory.

Create a new file called wpa_supplicant.conf in the directory boot and fill it with it:

```

country=fr
update_config=1
ctrl_interface=/var/run/wpa_supplicant
 
network={
 scan_ssid=1
 ssid="SSID-Internet-box"
 psk="Secured-key"
}

```

#### Connecting the raspy zero
In your file.py or [Junpyter] (https://jupyter.org/) or on your python3 console

```
from pyluos import Robot
robot = Robot("raspberrypi.local")
robot.modules

```
If the address raspberrypi.local doesn't work, try to connect directly to the ip address.


