import os
from time import sleep
import datetime
import RPi.GPIO as GPIO

import settings as params

# В следующую версию (v0.2) добавить:
# 1. температуру отключения куллера
# 2. логирование в файл
# 3. сделать возможным увеличить время работы куллера
#    за счет увеличения в n раз (по умолчанию в 3) времени
#    проверки температуры, когда куллер уже работает
# 4. Переписать всё в стиле ООП
# 5. Созадать инсталляционный скрипт (можно отдельной версией v0.2.1)


class Logs:
    def __init__(self, debug_lvl):
        self.dbg_lvl = debug_lvl

    def out(self, msg, lvl=3):
        if self.dbg_lvl == 0 or lvl == 0:
            return

        if lvl <= self.dbg_lvl:
            print("LOG: %s [%s]" % (msg, str(datetime.datetime.now())))


class SystemControl:
    def __init__(self):
        self.h_logs = Logs(params.debug)

    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        temp = (res.replace("temp=", "").replace("'C\n", ""))
        self.h_logs.out("CPU temperature is %s" % temp, 2)
        return float(temp)

    def clean_gpio(self):
        GPIO.cleanup()
        self.h_logs.out("GPIO cleanup")

    def setup_gpio(self):
        self.clean_gpio()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(params.pin, GPIO.OUT)
        GPIO.setwarnings(False)

        self.h_logs.out("GPIO setup")

    def set_pin(self, mode):
        GPIO.output(params.pin, mode)
        if mode is True:
            self.h_logs.out("Fan ON", 1)
        else:
            self.h_logs.out("Fan OFF", 1)


class FanRPi3ctrl:
    def __init__(self, t_on, t_off, delay_ms):
        self.fan_on = False
        self.temp_on = t_on
        self.temp_off = t_off
        self.delay_time = delay_ms
        self.sysctl = SystemControl()
        self.time_factor = 3.0

    def fan_on(self):
        self.sysctl.set_pin(True)

    def fan_off(self):
        self.sysctl.set_pin(False)

    def delay(self):
        s = float(self.delay_time) / 1000.0
        self.sysctl.set_pin("Wait %f seconds..." % s)
        sleep(s)

    def fan_control(self):
        cpu_temp = self.sysctl.get_cpu_temp()
        if self.fan_on is False:
            if cpu_temp >= self.temp_on:
                self.fan_on()
                self.fan_on = True
                self.delay_time * self.time_factor
        else:
            if cpu_temp <= self.temp_off:
                self.fan_off()
                self.fan_on = False
                self.delay_time / self.time_factor
