#!/usr/bin/env python3

import fanRPi3ctrl
import settings as params


if __name__ == "__main__":
    try:
        fanRPi3ctrl.setup()
        while True:
            fanRPi3ctrl.control_temp()
            fanRPi3ctrl.delay(params.delay_ms)
    except KeyboardInterrupt:
        fanRPi3ctrl.cleanup()
