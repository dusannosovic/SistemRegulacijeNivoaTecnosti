from flask import current_app
from flask_restful import Resource
import json

class ApiOutflowSensor(Resource):
    
    def get(self, parameter):

        outflow_sensor = current_app.config['outflow_sensor']

        if parameter == "status":
            ret_val = {"status": outflow_sensor.read_sensor_status()}
            ret_val = json.dumps(ret_val)
            return ret_val, 200

        elif parameter == "value":
            ret_val = {"value": outflow_sensor.read_sensor_value()}
            ret_val = json.dumps(ret_val)
            return ret_val, 200

        else:
            return json.dumps({"Message": "Invalid request"}), 400

    def put(self, parameter):

        outflow_sensor = current_app.config['outflow_sensor']

        if parameter == "status":
            
            temp = outflow_sensor.reset_sensor()

            if temp == 0:
                ret_val = json.dumps({"Message": "The sensor is restarted"})
                status_code = 200
            else:
                ret_val = json.dumps({"Message": "Something went wrong. Sensor could not be restarted."})
                status_code = 400

            return ret_val, status_code

        else:
            return json.dumps({"Message": "Invalid request"}), 400
