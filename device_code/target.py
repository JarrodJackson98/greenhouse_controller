#!/usr/bin/python3

## The main file called to run perpetually on your target device.

## These 2 lines add the current directory to the path, so any dependencies in this folder can be accessed
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import time

from doover_ui_iface import (
    doover_ui_variable,
    # doover_ui_element,
    doover_ui_submodule,
    doover_ui_text_parameter,
    doover_ui_datetime_parameter,
    doover_ui_warning_indicator,
    doover_ui_state_command,
    doover_ui_float_parameter,
    doover_ui_alert_stream,
    doover_ui_multiplot,
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

        float_input = self.doover_iface.get_command("tree")

        if float_input is None:
            temp = 25.0
        else:
            temp = float_input

        anyone_watching = self.doover_iface.is_being_observed()

        ui_elems = []

        ui_elems.append(
             doover_ui_variable(
                name="anyoneWatching",
                display_str="Did anybody see that?",
                var_type="bool",
                curr_val=anyone_watching,
                graphic="fireworks_gif",
            )
        )
        ui_elems.append(
             doover_ui_variable(
                name="anyoneWatching",
                display_str="Did anybody see that?",
                var_type="bool",
                curr_val=anyone_watching,
                graphic="fireworks_gif",
            )
        )

        new_submodule = doover_ui_submodule( 
            name="submodule",
            display_str="TESTING THE SUBMODULE",
            ).add_children(ui_elems)

        self.doover_iface.set_children([
            doover_ui_warning_indicator(
                name="temp",
                display_str="Temperature",),
            doover_ui_text_parameter(
                name="text_param",
                display_str="the happy variable",),
            doover_ui_datetime_parameter(
                name="datetime_param",
                display_str="Datetime Parameter object",),
            doover_ui_state_command(
                name="state_command",
                display_str="State Command object",),
            doover_ui_float_parameter(
                name="tree",
                display_str="Float Parameter object",), 
            doover_ui_alert_stream(
                name="alert_stream",
                display_str="Alert Stream object",), 
            doover_ui_variable(
                name="gauge_test",
                display_str="Gauge Test",
                var_type="float",
                curr_val=temp,
                dec_precision=1,
                form="radialGauge",
                ranges = [{
                        "label" : "Cool",
                        "min" : 0,
                        "max" : 20,
                        "colour" : 'green',
                        "showOnGraph" : True,
                    },
                    {
                        "label" : "Warm",
                        "min" : 20,
                        "max" : 30,
                        "colour" : 'yellow',
                        "showOnGraph" : True,
                    },
                    {
                        "label" : "Hot",
                        "min" : 30,
                        "max" : 40,
                        "colour" : 'red',
                        "showOnGraph" : True,
                    },],
            ), 
            new_submodule,
        ])

        self.doover_iface.record_critical_value(
            name="anyone_watching",
            value=anyone_watching
        )
        
        self.doover_iface.set_display_str( "Testing UI" )

        

        self.doover_iface.handle_comms()

        time.sleep(1)

