import datetime
import socketserver
import threading
import time
from random import random
from EnumClasses import ValveStatus

#Otocni ventil 2
    
class Valve2():
    def __init__(self, pump_ip = "localhost", pump_port = 10102, sensor_fail_rate = 1, water_per_second = 1):
        
        self.network_ip = pump_ip
        self.network_port = pump_port
        self.fail_rate = sensor_fail_rate
        self.water_per_second = water_per_second
        self.valve_status = ValveStatus.OFF
        self.error_counter = 0
        
    
            
    def read_valve_status(self):
        return int(self.valve_status)
    def read_valve_status_simulation(self):
        if self.valve_status<0:
            return 0
        else :
            return int(self.valve_status)
    
    def set_valve_status(self, number):
        self.valve_status = ValveStatus(number)
    
    def read_water_per_second(self):
        return int(self.water_per_second)

    def reset_valve(self):
        self.valve_status = ValveStatus.OFF # TODO: implement a more elaborate reset logic
        self.error_counter = 0
        return 0
        
    def read_network_ip(self):
        return self.network_ip
    
    def read_network_port(self):
        return self.network_port

    def step(self):
        if ((0 < self.fail_rate) and (self.fail_rate<=100)):
            if (self.valve_status is not ValveStatus.FAILED):
                if (random() <= (self.fail_rate / 100)): 
                    #self.has_fault = True
                    self.error_counter = 20 # count 2x10 seconds with a 10-second step
                    self.valve_status = ValveStatus.FAILED
            else:
                if (self.error_counter <= 0):
                    #self.has_fault = False # reset fault after fault duration countdown expires
                    self.error_counter = 0
                    self.valve_status = ValveStatus.OFF
                else:
                    self.error_counter = self.error_counter - 1
        else:
            val = 1 # do nothing
    

    