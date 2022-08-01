import datetime
import socketserver
import threading
import time
from random import random
from EnumClasses import ServoValveStatus
    
    
class ServoValve():
    def __init__(self, pump_ip = "localhost", pump_port = 10301, sensor_fail_rate = 0):
        
        self.network_ip = pump_ip
        self.network_port = pump_port

        self.servo_valve_status = ServoValveStatus.Level0percent
    
            
    def read_valve_status(self):
        return int(self.servo_valve_status)

    def read_valve_status_simulation(self):
        if self.servo_valve_status<0:
            return 0
        else :
            return int(self.servo_valve_status)
    
    def set_valve_status(self, number):
        round_value = round(number/10)*10
        self.servo_valve_status = ServoValveStatus(round_value)
    
    
    def reset_valve(self):
        self.servo_valve_status = ServoValveStatus.Level0percent # TODO: implement a more elaborate reset logic
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
    