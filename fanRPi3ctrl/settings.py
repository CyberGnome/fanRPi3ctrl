
# Hardware settings
pin = 18         # control pin


# Fan settings
temp_on = 48.5   # fan start temperature
temp_off = 40.0  # fan stop temperature

delay_ms = 15000  # interval between CPU temperature checks


# Debug Mode
debug = 3       # input number [0..3] where:
                #     0 - disable debug messages
                #     1 - enable debug messages as start/stop fan
                #     2 - print CPU temperature
                #     3 - print all messages

output_file = False  # if it is True logs output to file
logs_file = "/home/.fanRPi3ctrl.logs"  # path to logs file
                                       # if "output_file" is False
                                       # this parameter is ignored
