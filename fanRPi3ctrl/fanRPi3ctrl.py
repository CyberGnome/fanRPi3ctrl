import os
from time import sleep
import datetime
import RPi.GPIO as GPIO

import settings as params


def print_log(msg, lvl=3):
    if lvl < 1:
        return

    if lvl <= params.debug:
        print("LOG: %s [%s]" % (msg, str(datetime.datetime.now())))


def cleanup():
    GPIO.cleanup()
    print_log("GPIO cleanup")


def setup():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(params.pin, GPIO.OUT)
    GPIO.setwarnings(False)
    print_log("GPIO setup")


def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    temp = (res.replace("temp=", "").replace("'C\n", ""))
    print_log("CPU temperature is %s" % temp, 2)
    return float(temp)


def set_pin(mode):
    GPIO.output(params.pin, mode)
    if mode is True:
        print_log("Fan ON", 1)
    else:
        print_log("Fan OFF", 1)


def fan_on():
    set_pin(True)


def fan_off():
    set_pin(False)


def control_temp():
    cpu_temp = get_cpu_temp()
    if cpu_temp >= params.temp_on:
        fan_on()
    else:
        fan_off()


def delay(ms):
    s = float(ms) / 1000.0
    print_log("Wait %f seconds..." % s)
    sleep(s)


