import datetime
import socketserver
import threading
import time
from enum import IntEnum, Enum
from random import random


    
class ValveStatus(IntEnum):
    ON = 1 # valve on
    OFF = 0 # valve off
    
#Otocni ventil 2
    
class Valve2():
    def __init__(self, pump_ip = "localhost", pump_port = 10102, sensor_fail_rate = 0, water_per_second = 1):
        
        self.network_ip = pump_ip
        self.network_port = pump_port

        self.water_per_second = water_per_second
        self.valve_status = ValveStatus.OFF
        
    
            
    def read_valve_status(self):
        return int(self.valve_status)
    
    def set_valve_status(self, number):
        self.valve_status = number
    
    def read_water_per_second(self):
        return int(self.water_per_second)

    def reset_sensor(self):
        self.valve_status = ValveStatus.OFF # TODO: implement a more elaborate reset logic
        return 0
        
    def read_network_ip(self):
        return self.network_ip
    
    def read_network_port(self):
        return self.network_port

    
    def step(self,temp_level,max_level):
        if ((0 < self.fail_rate) and (self.fail_rate<=100)):
            if (self.has_fault is False):
                if (random() <= (self.fail_rate / 100)): 
                    self.has_fault = True
                    self.error_counter = 2 # count 2x10 seconds with a 10-second step
                    #self.sensor_status = SensorStatus.FAILED
            else:
                if (self.error_counter <= 0):
                    self.has_fault = False # reset fault after fault duration countdown expires
                    self.error_counter = 0
                    #self.sensor_status = SensorStatus.OK
                else:
                    self.error_counter = self.error_counter - 1
        else:
            val = 1 # do nothing
    