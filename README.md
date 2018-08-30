# fanRPi3ctrl

Fan control script for raspberry pi

## Installation

1. Install all requirements for your project version (look it in **Release History** section)
1. Edit file *settings.py*
1. Run file *"run.py"*:
````
\.run.py
````

You can demonize your fanRPi3ctrl and add it in *autostart*.
For example you can add crone job:
````
@reboot /path/to/fanRPi3ctrl/project/run.py >/path/to/cronlog 2>&1
````

## Release History

### *fanRPi3ctrl v0.1*

**Date of Release**
* *30.08.2018*

**Requirements**
* *- Python 3.5.2*
* *- RPi.GPIO 0.6.3*

**Features**
* *Checking CPU temperature after the specified time*
* *If CPU temperature is higher then permissible temperature, turn on the fan*
