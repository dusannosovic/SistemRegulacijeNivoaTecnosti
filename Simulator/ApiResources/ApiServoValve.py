from cmath import e
from flask import current_app, request
from flask_restful import Resource
import json


class ApiServoValve(Resource):

    def get(self, parameter):

        servo_valve = current_app.config['servo_valve']

        if parameter == "status":
            ret_val = {"status": servo_valve.read_valve_status()}
            return json.dumps(ret_val), 200
        else:
            return json.dumps({"Message": "Invalid request"}), 400

    def put(self, parameter):

        servo_valve = current_app.config['servo_valve']
        
        if parameter == "reset":
            
            temp = servo_valve.reset_valve()

            if temp == 0:
                ret_val = json.dumps({"Message": "The valve is restarted"})
                status_code = 200
            else:
                ret_val = json.dumps({"Message": "Something went wrong. Valve could not be restarted."})
                status_code = 400

            return ret_val, status_code
        
        elif parameter == "status":
            try:
                body_params = request.get_json(force=True)
                new_value = body_params['value']
                new_value = float(new_value)
                servo_valve.set_valve_status(new_value)
                return json.dumps({"Message": "Success"}) , 200
            
            except KeyError as exception:
                return json.dumps({f"Message": "Error. Expected json format: { 'value' : [your number here] }."}), 400
            
            except ValueError as exception:
                return json.dumps({f"Message": str(exception)})
            
            except BaseException as exception:
                print(str(exception))
                return json.dumps({"Message": "Invalid request"}), 400
            
        else:
            return json.dumps({"Message": "Invalid request"}), 400
