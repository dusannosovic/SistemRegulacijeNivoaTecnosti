from flask import current_app, request
from flask_restful import Resource
import json

class ApiWaterPump(Resource):
    
    def get(self,parameter):
        
        water_pump = current_app.config['water_pump']

        if parameter == "status":
            ret_val = {"status": water_pump.read_pump_operation()}
            return json.dumps(ret_val), 200
        else:
            return json.dumps({"Message": "Invalid request"}), 400
    
    def put(self, parameter):
        
        water_pump = current_app.config['water_pump']
        
        if parameter == "reset":
            
            temp = water_pump.reset_pump()

            if temp == 0:
                ret_val = json.dumps({"Message": "The Water pump is restarted"})
                status_code = 200
            else:
                ret_val = json.dumps({"Message": "Something went wrong. Water pump could not be restarted."})
                status_code = 400

            return ret_val, status_code
        
        elif parameter == "status":
            try:
                body_params = request.get_json(force=True)
                new_value = body_params['value']
                new_value = int(new_value)
                water_pump.set_pump_operation(new_value)
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