#!/usr/bin/env python3

import outredirect.core as redirect
import fanRPi3ctrl
import settings as params


if __name__ == "__main__":
    print_redirect = redirect.OutRedirect()
    if params.output_file is True:
        try:
            print_redirect.file(params.logs_file)
        except Exception as error:
            raise

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
        if params.output_file is True:
            print_redirect.standard()
