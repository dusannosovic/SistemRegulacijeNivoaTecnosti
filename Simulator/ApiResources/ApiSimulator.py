import json
from flask import current_app
from flask_restful import Resource

class ApiSimulator(Resource):
    
    def get(self):
        try:
            flow_sensor = current_app.config['flow_sensor'] 
            level_sensor = current_app.config['level_sensor'] 
            outflow_sensor = current_app.config['outflow_sensor'] 
            servo_valve = current_app.config['servo_valve'] 
            valve1 = current_app.config['valve1']
            valve2 = current_app.config['valve2']
            valve3 = current_app.config['valve3']
            water_pump = current_app.config['water_pump']
        
            ret_val = {
                "flow_sensor": {
                    "status" : flow_sensor.read_sensor_status(),
                    "value" : flow_sensor.read_sensor_value()
                },
                "level_sensor": {
                    "status" : level_sensor.read_sensor_status(),
                    "value" : level_sensor.read_sensor_value()
                },
                "outflow_sensor": {
                    "status" : outflow_sensor.read_sensor_status(),
                    "value" : outflow_sensor.read_sensor_value()
                },
                "servo_valve":{
                    "status": servo_valve.read_valve_status()
                },
                "valve1":{
                    "status": valve1.read_valve_status()
                },
                "valve2":{
                    "status": valve2.read_valve_status()
                },
                "valve3":{
                    "status": valve3.read_valve_status()
                },
                "water_pump":{
                    "status": water_pump.read_pump_operation()
                },
            }   
        
            return json.dumps(ret_val) , 200
        
        except Exception as exception:
            print(exception)
            return json.dumps({"Message": "Invalid request"}), 400
        
        