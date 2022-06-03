import datetime
import socketserver
import threading
import time
from enum import IntEnum, Enum
from random import random


    
class EngineOperationMode(IntEnum):
    ON = 1 # when pump in operation
    OFF = 0 # turned off
class WaterLever(IntEnum):
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
class SensorType(IntEnum):
    LEVEL = 1
    FLOWSENSOR = 2
    

    
class GenericSensor():
    def __init__(self, pump_ip = "localhost", pump_port = 10101, sensor_fail_rate = 0, sensor_type = SensorType.LEVEL):
        
        self.network_ip = pump_ip
        self.network_port = pump_port

        self.pump_running = EngineOperationMode.OFF
        self.sensor_path = "SENSOR_"
        self.sensor_type = sensor_type
        
    
            
    def read_pump_status(self):
        return int(self.pump_running)
    
    def set_pump_status(self, number):
        self.pump_running = number
    
    def read_sensor_path(self):
        return self.sensor_path
    
    def reset_sensor(self):
        self.sensor_status = SensorStatus.OK # TODO: implement a more elaborate reset logic
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
    
    

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        # self.request is the TCP socket connected to the client
        has_error = False
        self.data = self.request.recv(1024).strip()
        self.data = bytes(self.data)
        #print(datetime.datetime.now(), " - {} wrote:".format(self.client_address[0]))
        #print(' data: ', str(self.data))
        
        try:
            if (sensor is None):
                has_error = True
                raise Exception('ERROR: The sensor not initialized  - ' + sensor.read_sensor_path())

            if (len(self.data) == 1):
                received_operation = self.data[0]
                if (received_operation == 1): # if read sensor status received                    
                    send_data = bytes([sensor.read_sensor_status()])
                    #print(datetime.datetime.now(), '- sensor status response: ', str(send_data.hex()))
                    self.request.sendall(send_data)
                    #print(datetime.datetime.now(), '- status sent')
                elif (received_operation == 2):
                    send_data = bytes([sensor.read_sensor_value()])
                    #print(datetime.datetime.now(), '- sensor value response: ', str(send_data.hex()))
                    self.request.sendall(send_data)
                    #print(datetime.datetime.now(), '- value sent')
                elif (received_operation == 3): # if reset received
                    sensor.reset()
                    #print(datetime.datetime.now(), ' - Sensor reset: ', str(received_value), '...')
                    resp = bytes([0]) # confirm request (0 - response)
                    self.request.sendall(resp)
                else:
                    has_error = True
            else:
                has_error = True
        except:
            print('Exception occurred in handle.')
            has_error = True
            
        if (has_error):
            print(datetime.datetime.now(), ' - Invalid input message received: ')
            #print(' - address: ')
            print(' - message: '+ str(self.data))
            resp = bytes([1])
            self.request.sendall(resp)
        
    
def thread_function(sensor):
    while (True):
        sensor.step()
        time.sleep(10)

    
if __name__ == "__main__":
    HOST, PORT = "192.168.2.103", 10103
    
    # TODO: implement load configuration from JSON
    sensor = GenericSensor(HOST, PORT, sensor_fail_rate = 5, sensor_type = SensorType.DOOR) #TODO: change according to need(s)

    x = threading.Thread(target=thread_function, args=(sensor,))
    x.start()
    
   
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        #server.initialize_controller()
        server.serve_forever()