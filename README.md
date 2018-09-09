___
# fanRPi3ctrl

Fan control script for raspberry pi.
___
## **fanRPi3ctrl v0.1.1**

**Date of Release**
* *09.09.2018*

**Requirements**
* *- Python 3.5.2*
* *- RPi.GPIO 0.6.3*

**New Features**
* *Turn off the fan after lowering the temperature to the specified value.*
* *Store log messages in the specified file [Optional]*

**Installation**

*Go to "path/to/fanRPi3ctrl/requirements/":*
````
cd path/to/fanRPi3ctrl/requirements/
````

*Install dependences from "requirements.txt":*
````
pip install -r requirements.txt
````

*Install outputredirect-0.1.tar.gz:*
````
pip install outputredirect-0.1.tar.gz
````

*Change setting in file "path/to/fanRPi3ctrl/requirements/settings.py"*
*Now you can run fanRPi3ctrl:*
````
cd path/to/fanRPi3ctrl/
./run.py
````

*You can demonize your fanRPi3ctrl and add it in autostart.*

*For example you can add crone job:*
````
@reboot /path/to/fanRPi3ctrl/run.py >/path/to/cronlog 2>&1
````
___
### Release History

#### **fanRPi3ctrl v0.1.1**

**Date of Release**
* *09.09.2018*

**Requirements**
* *- Python 3.5.2*
* *- RPi.GPIO 0.6.3*

**New Features**
* *Turn off the fan after lowering the temperature to the specified value.*
* *Store log messages in the specified file [Optional]*

#### *fanRPi3ctrl v0.1*

**Date of Release**
* *30.08.2018*

**Requirements**
* *- Python 3.5.2*
* *- RPi.GPIO 0.6.3*

**Features**
* *Checking CPU temperature after the specified time*
* *If CPU temperature is higher then permissible temperature, turn on the fan*
