import json
from flask import current_app, jsonify, make_response
from flask_restful import Resource
from EnumClasses import ValveStatus, PumpOperation, ServoValveStatus


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
                    "status": servo_valve.read_valve_status(),
                    "alarm": 1 if servo_valve.read_valve_status() == -1 else 0
                },
                "valve1":{
                    "status": valve1.read_valve_status(),
                    "status_text": ValveStatus(valve1.read_valve_status()).name,
                    "alarm": 1 if ValveStatus(valve1.read_valve_status()).name == ValveStatus.FAILED.name else 0
                },
                "valve2":{
                    "status": valve2.read_valve_status(),
                    "status_text": ValveStatus(valve2.read_valve_status()).name,
                    "alarm": 1 if ValveStatus(valve2.read_valve_status()).name == ValveStatus.FAILED.name else 0
                },
                "valve3":{
                    "status": valve3.read_valve_status(),
                    "status_text": ValveStatus(valve3.read_valve_status()).name,
                    "alarm": 1 if ValveStatus(valve3.read_valve_status()).name == ValveStatus.FAILED.name else 0
                },
                "water_pump":{
                    "status": water_pump.read_pump_operation(),
                    "status_text": PumpOperation(water_pump.read_pump_operation()).name,
                    "alarm": 1 if PumpOperation(water_pump.read_pump_operation()).name == PumpOperation.FAILED.name else 0
                },
            }   
            return make_response(jsonify(ret_val) , 200)
        
        except Exception as exception:
            print(exception)
            return json.dumps({"Message": "Invalid request"}), 400
        
        