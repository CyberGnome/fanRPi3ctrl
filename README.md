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

You must create file:
````
nano /etc/init.d/fanRPi3ctrl
````

Then you must copy-paste in it the following code
````
#!/bin/sh
### BEGIN INIT INFO
# Provides: dnscheck
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Short-Description: Start fan script at boot time
# Description: Enable service provided by daemon.
### END INIT INFO

python3 /path/to/folder/with/project/run.py [>> /path/to/folder/with/logs]
````

You must write *">> /path/to/folder/with/logs"* if you want to save logs from fanRPi3ctrl.

And create the symbolic links by running:
````
update-rc.d /etc/init.d/dnscheck defaults
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
