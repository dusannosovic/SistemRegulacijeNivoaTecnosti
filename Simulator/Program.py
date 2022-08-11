from multiprocessing.sharedctypes import Value
import threading
import time
import random
from flask import Flask
from flask_restful import Api
from ApiResources.ApiFlowSensor import ApiFlowSensor
from ApiResources.ApiLevelSensor import ApiLevelSensor
from ApiResources.ApiOutflowSensor import ApiOutflowSensor
from ApiResources.ApiServoValve import ApiServoValve
from ApiResources.ApiValve1 import ApiValve1
from ApiResources.ApiValve2 import ApiValve2
from ApiResources.ApiValve3 import ApiValve3
from ApiResources.ApiWaterPump import ApiWaterPump
from ApiResources.ApiSimulator import ApiSimulator
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
    water_tank = 4500
    water_tank_capacity = 8000
    outflow_tank_capacity = 12000
    outflow_water_tank = 6300
    outflow_water =0
    #tank = 0
    while(True):
        
        water_flow= water_pump.read_water_per_second()*water_pump.read_pump_operation_simulation()*valve3.read_valve_status_simulation()*servo_valve.read_valve_status_simulation()/100
        
        if not flow_sensor.read_sensor_status():
            flow_sensor.set_sensor_value(water_flow)
        pump_outflow_tank = 0
        #water_tank += water_flow
        outflow = 0
        if water_tank>0 and valve1.read_water_per_second()*valve1.read_valve_status_simulation() + valve2.read_water_per_second()*valve2.read_valve_status_simulation()<water_tank:
            outflow = valve1.read_water_per_second()*valve1.read_valve_status_simulation() + valve2.read_water_per_second()*valve2.read_valve_status_simulation()
            if outflow_tank_capacity-outflow_water_tank < outflow:
                outflow = outflow_tank_capacity-outflow_water_tank
        elif valve1.read_water_per_second()*valve1.read_valve_status_simulation() + valve2.read_water_per_second()*valve2.read_valve_status_simulation()>water_tank:
            outflow = water_tank
            if outflow_tank_capacity-outflow_water_tank < outflow:
                outflow = outflow_tank_capacity-outflow_water_tank


        if outflow_water_tank>0 and water_pump.read_pump_operation_simulation() and water_flow<=outflow_water_tank+outflow and water_tank_capacity-water_tank>=water_flow:
            pump_outflow_tank = water_flow
            if water_tank_capacity-water_tank<pump_outflow_tank:
                pump_outflow_tank = water_tank_capacity-water_tank
        elif outflow_water_tank>0 and water_pump.read_pump_operation_simulation() and water_flow>outflow_water_tank+outflow:
            pump_outflow_tank = outflow_water_tank+outflow
            if water_tank_capacity-water_tank<pump_outflow_tank:
                pump_outflow_tank = water_tank_capacity-water_tank
            
        water_tank = water_tank + pump_outflow_tank-outflow
        outflow_water_tank += outflow - pump_outflow_tank
        if not level_sensor.read_sensor_status():
            level_sensor.set_sensor_value(water_tank)
        if not outflow_sensor.read_sensor_status():
            outflow_sensor.set_sensor_value(outflow_water_tank)
        
        print("-------------------------------------------------------")
        print("Level sensor",level_sensor.read_sensor_value(), "cm")
        print("Outflow sensor",outflow_sensor.read_sensor_value(),"cm")
        print("Flow sensor", flow_sensor.read_sensor_value(),"cm")
        level_sensor.step()
        flow_sensor.step()
        outflow_sensor.step()
        valve1.step()
        valve2.step()
        valve3.step()
        water_pump.step()
        servo_valve.step()

        #print("Outflow sensor")
        #print(outflow_water_tank)
        time.sleep(1)

if __name__ == "__main__":
    level_sensor = LevelSensor()
    flow_sensor = FlowSensor()
    valve1 = Valve1()
    valve1.water_per_second = 10
    valve2 = Valve2()
    valve2.water_per_second = 7
    valve3 = Valve3()
    servo_valve = ServoValve()
    servo_valve.set_valve_status(4)
    water_pump = WaterPump()
    water_pump.set_pump_capacity(15)
    outflow_sensor = OutflowSensor()
    
    app = Flask(__name__)
    api = Api(app)
    
    #sensor resources
    api.add_resource(ApiFlowSensor, "/flowsensor/<string:parameter>")
    api.add_resource(ApiLevelSensor, "/levelsensor/<string:parameter>")
    api.add_resource(ApiOutflowSensor,"/outflowsensor/<string:parameter>")
    
    #actuator resources
    api.add_resource(ApiServoValve, "/servovalve/<string:parameter>")
    api.add_resource(ApiValve1, "/valve1/<string:parameter>")
    api.add_resource(ApiValve2, "/valve2/<string:parameter>")
    api.add_resource(ApiValve3, "/valve3/<string:parameter>")
    api.add_resource(ApiWaterPump, "/waterpump/<string:parameter>")
    
    #data resource (all necessary data for InView)
    api.add_resource(ApiSimulator, "/data")
    
    
    
    app.config['flow_sensor'] = flow_sensor
    app.config['level_sensor'] = level_sensor
    app.config['outflow_sensor'] = outflow_sensor
    app.config['servo_valve'] = servo_valve
    app.config['valve1'] = valve1
    app.config['valve2'] = valve2
    app.config['valve3'] = valve3
    app.config['water_pump'] = water_pump

    x = threading.Thread(target=thread_function, args=(level_sensor,flow_sensor,valve1,valve2,valve3,water_pump,servo_valve,outflow_sensor,))
    x.start()
    
    app.run(host="0.0.0.0",port=5000)