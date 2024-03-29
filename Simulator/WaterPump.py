import datetime
import socketserver
import threading
import time
from random import random
from EnumClasses import PumpOperation

    
class WaterPump():
    def __init__(self, pump_ip = "localhost", pump_port = 10201, sensor_fail_rate = 1, water_per_second=1):
        
        self.network_ip = pump_ip
        self.network_port = pump_port
        self.fail_rate = sensor_fail_rate
        self.pump_water_per_second = water_per_second
        self.pump_operation = PumpOperation.OFF
        self.error_counter = 0
        
    
            
    def read_pump_operation(self):
        return int(self.pump_operation)
    def read_pump_operation_simulation(self):
        if self.pump_operation<0:
            return 0
        else :
            return int(self.pump_operation)
    
    def set_pump_operation(self, number):
        self.pump_operation = PumpOperation(number)

    def read_water_per_second(self):
        return int(self.pump_water_per_second)
        
    def set_pump_capacity(self, water_per_second):
        self.pump_water_per_second = water_per_second
    
    def reset_pump(self):
        self.pump_operation = PumpOperation.OFF # TODO: implement a more elaborate reset logic
        self.error_counter = 0
        return 0
        
    def read_network_ip(self):
        return self.network_ip
    
    def read_network_port(self):
        return self.network_port
    
    def step(self):
        if ((0 < self.fail_rate) and (self.fail_rate<=100)):
            if (self.pump_operation is not PumpOperation.FAILED):
                if (random() <= (self.fail_rate / 100)): 
                    #self.has_fault = True
                    self.error_counter = 20 # count 2x10 seconds with a 10-second step
                    #self.sensor_status = SensorStatus.FAILED
                    self.pump_operation = PumpOperation.FAILED
            else:
                if (self.error_counter <= 0):
                    #self.has_fault = False # reset fault after fault duration countdown expires
                    self.error_counter = 0
                    self.pump_operation = PumpOperation.OFF
                else:
                    self.error_counter = self.error_counter - 1
        else:
            val = 1 # do nothing
    