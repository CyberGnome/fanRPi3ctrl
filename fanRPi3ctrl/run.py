#!/usr/bin/env python3

import fanRPi3ctrl
import settings as params


if __name__ == "__main__":
    fan_ctrl = fanRPi3ctrl.FanRPi3ctrl(params.temp_on,
                                       params.temp_off,
                                       params.delay_ms)
    try:
        fan_ctrl.sysctl.setup_gpio()
        while True:
            fan_ctrl.fan_control()
            fan_ctrl.delay()
    except KeyboardInterrupt:
        fan_ctrl.sysctl.clean_gpio()
