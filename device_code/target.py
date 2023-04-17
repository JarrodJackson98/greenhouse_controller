#!/usr/bin/python3

## The main file called to run perpetually on your target device.

## These 2 lines add the current directory to the path, so any dependencies in this folder can be accessed
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import time

from doover_ui_iface import (
    doover_ui_variable,
    # doover_ui_element,
    # doover_ui_submodule,
    # doover_ui_text_parameter,
    # doover_ui_datetime_parameter,
    # doover_ui_warning_indicator,
    # doover_ui_state_command,
    # doover_ui_float_parameter,
    # doover_ui_alert_stream,
    # doover_ui_multiplot,
)


class program:

    # doover_iface=doover_iface, plt_iface=plt_iface, mb_iface=mb_iface
    def __init__(self, doover_iface, plt_iface, mb_iface):
        self.doover_iface = doover_iface
        self.plt_iface = plt_iface
        self.mb_iface = mb_iface


    ## Use this function to do any setup or instantiation of your program
    def setup(self):
        
        ## You can retrieve settings from the "Deployment Config" section
        # in your devices profile in the Doover console like so
        example_parameter = self.doover_iface.get_setting('example_parameter')


    ## This function is called before any shutdown or program stop
    def close(self):
        pass


    ## This function is called recursively as long as the program should run
    def main_loop(self):

        anyone_watching = self.doover_iface.is_being_observed()

        self.doover_iface.set_children([
            doover_ui_variable(
                name="anyoneWatching",
                display_str="Did anybody see that?",
                var_type="bool",
                curr_val=anyone_watching,
                graphic="fireworks_gif",
            )
        ])

        self.doover_iface.record_critical_value(
            name="anyone_watching",
            value=anyone_watching
        )
        
        self.doover_iface.set_display_str( "Hello World" )

        self.doover_iface.set_display_str( "Hello World" )

        self.doover_iface.handle_comms()

        time.sleep(1)

