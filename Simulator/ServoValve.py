import datetime
import socketserver
import threading
import time
from random import random
from EnumClasses import ServoValveStatus
    
    
class ServoValve():
    def __init__(self, pump_ip = "localhost", pump_port = 10301, sensor_fail_rate = 1):
        
        self.network_ip = pump_ip
        self.network_port = pump_port
        self.fail_rate = sensor_fail_rate
        self.servo_valve_status = 0
        self.error_counter = 0
    
            
    def read_valve_status(self):
        return int(self.servo_valve_status)

    def read_valve_status_simulation(self):
        if self.servo_valve_status<0:
            return 0
        else :
            return int(self.servo_valve_status)
    
    def set_valve_status(self, current):
        value = ((current-4)/(20-4))*100
        #round_value = round(number/10)*10
        if value >=0 and value <= 100:
            self.servo_valve_status = value
    
    
    def reset_valve(self):
        self.servo_valve_status = 0 # TODO: implement a more elaborate reset logic
        self.error_counter = 0
        return 0
        
    def read_network_ip(self):
        return self.network_ip
    
    def read_network_port(self):
        return self.network_port
    
    def step(self):
        if ((0 < self.fail_rate) and (self.fail_rate<=100)):
            if (self.servo_valve_status >=0):
                if (random() <= (self.fail_rate / 100)): 
                    #self.has_fault = True
                    self.error_counter = 20 # count 2x10 seconds with a 10-second step
                    self.servo_valve_status = -1
            else:
                if (self.error_counter <= 0):
                    #self.has_fault = False # reset fault after fault duration countdown expires
                    self.error_counter = 0
                    self.servo_valve_status = 0
                else:
                    self.error_counter = self.error_counter - 1
        else:
            val = 1 # do nothing
    