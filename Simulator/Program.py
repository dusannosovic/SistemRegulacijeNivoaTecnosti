from multiprocessing.sharedctypes import Value
import threading
import time
import random
from flask import Flask
from flask_restful import Api
from ApiResources.ApiFlowSensor import ApiFlowSensor
from ApiResources.ApiLevelSensor import ApiLevelSensor
from ApiResources.ApiOutflowSensor import ApiOutflowSensor
from LevelSensor import LevelSensor
from FlowSensor import FlowSensor
from Valve1 import Valve1
from Valve2 import Valve2
from Valve3 import Valve3
from ServoValve import ServoValve
from WaterPump import WaterPump
from OutflowSensor import OutflowSensor

def thread_function(level_sensor, flow_sensor, valve1, valve2, valve3, water_pump,servo_valve, outflow_sensor):
    water_flow = 0
    water_tank = 0
    outflow_water_tank = 0
    outflow_water =0
    #tank = 0
    while(True):
        
        
        water_flow= water_pump.read_water_per_second()*valve3.read_valve_status()*servo_valve.read_valve_status()/100
        flow_sensor.set_sensor_value(water_flow)
        #water_tank += water_flow
        outflow = 0
        if water_tank>0 and valve1.read_water_per_second()*valve1.read_valve_status() + valve2.read_water_per_second()*valve2.read_valve_status()<water_tank:
            outflow = valve1.read_water_per_second()*valve1.read_valve_status() + valve2.read_water_per_second()*valve2.read_valve_status()
            #water_tank-=outflow
        elif valve1.read_water_per_second()*valve1.read_valve_status() + valve2.read_water_per_second()*valve2.read_valve_status()>water_tank:
            outflow = water_tank
            #water_tank-=outflow
        water_tank = water_tank + water_flow-outflow
        outflow_water_tank += outflow
        level_sensor.set_sensor_value(water_tank)
        outflow_sensor.set_sensor_value(outflow_water_tank)
        
        print("-------------------------------------------------------")
        print("Level sensor",level_sensor.read_sensor_value(), "cm")
        print("Outflow sensor",outflow_sensor.read_sensor_value(),"cm")
        print("Flow sensor", flow_sensor.read_sensor_value(),"cm") 
        #print("Outflow sensor")
        #print(outflow_water_tank)
        time.sleep(1)

if __name__ == "__main__":
    level_sensor = LevelSensor()
    flow_sensor = FlowSensor()
    valve1 = Valve1()
    valve1.water_per_second = 5
    valve1.set_valve_status(1)
    valve2 = Valve2()
    valve2.water_per_second = 3
    #valve2.set_valve_status(1)
    valve3 = Valve3()
    valve3.set_valve_status(1)
    servo_valve = ServoValve()
    servo_valve.set_valve_status(53)
    water_pump = WaterPump()
    water_pump.set_pump_operation(1)
    water_pump.set_pump_capacity(15)
    outflow_sensor = OutflowSensor()
    
    app = Flask(__name__)
    api = Api(app)
    
    api.add_resource(ApiFlowSensor, "/flowsensor/<string:parameter>")
    api.add_resource(ApiLevelSensor, "/levelsensor/<string:parameter>")
    api.add_resource(ApiOutflowSensor,"/outflowsensor/<string:parameter>")
    
    app.config['flow_sensor'] = flow_sensor
    app.config['level_sensor'] = level_sensor
    app.config['outflow_sensor'] = outflow_sensor

    x = threading.Thread(target=thread_function, args=(level_sensor,flow_sensor,valve1,valve2,valve3,water_pump,servo_valve,outflow_sensor,))
    x.start()
    
    app.run()