import datetime
import socketserver
import threading
import time
from enum import IntEnum
from random import random
from EnumClasses import SensorStatus


class WaterLevel(IntEnum):
    Level0percent = 0
    Level10percent = 10
    Level20percent = 20
    Level30percent = 30
    Level40percent = 40
    Level50percent = 50
    Level60percent = 60
    Level70percent = 70
    Level80percent = 80
    Level90percent = 90
    Level100percent= 100

    
class LevelSensor():
    def __init__(self, sensor_ip = "localhost", sensor_port = 10401, sensor_fail_rate = 0):
        
        self.network_ip = sensor_ip
        self.network_port = sensor_port

        self.sensor_status = SensorStatus.OK

        self.sensor_value = 0
        
    
            
    def read_sensor_value(self):
        return float(self.sensor_value)
    def read_sensor_status(self):
        return int(self.sensor_status)
    
    def set_sensor_value(self,temp_value):
        #if temp_value<=max_value:
        #   value_percent = temp_value/max_value*100
        #   round_value = round(value_percent/10)*10
        #   self.sensor_value = round_value
        self.sensor_value = temp_value
            
    
    def reset_sensor(self):
        self.sensor_status = SensorStatus.OK # TODO: implement a more elaborate reset logic
        return 0
        
    def read_network_ip(self):
        return self.network_ip
    
    def read_network_port(self):
        return self.network_port
    
    def step(self):
        if ((0 < self.fail_rate) and (self.fail_rate<=100)):
            if (self.has_fault is False):
                if (random() <= (self.fail_rate / 100)): 
                    self.has_fault = True
                    self.error_counter = 2 # count 2x10 seconds with a 10-second step
                    self.sensor_status = SensorStatus.FAILED
            else:
                if (self.error_counter <= 0):
                    self.has_fault = False # reset fault after fault duration countdown expires
                    self.error_counter = 0
                    self.sensor_status = SensorStatus.OK
                else:
                    self.error_counter = self.error_counter - 1
        else:
            val = 1 # do nothing
