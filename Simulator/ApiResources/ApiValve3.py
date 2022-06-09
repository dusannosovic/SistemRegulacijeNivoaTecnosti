from flask import current_app, request
from flask_restful import Resource
import json

class ApiValve3(Resource):
    
    def get(self,parameter):
        
        valve3 = current_app.config['valve3']

        if parameter == "status":
            ret_val = {"status": valve3.read_valve_status()}
            return json.dumps(ret_val), 200
        else:
            return json.dumps({"Message": "Invalid request"}), 400
    
    def put(self, parameter):
        
        valve3 = current_app.config['valve3']
        
        if parameter == "reset":
            
            temp = valve3.reset_valve()

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
                new_value = round(float(new_value))
                                
                if new_value < 0 or new_value > 1:
                    return json.dumps({"Message": "Invalid value for valve3 status"}), 400
                
                valve3.set_valve_status(new_value)
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