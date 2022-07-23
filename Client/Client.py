from concurrent.futures import thread
from threading import Thread
import requests
import OnChange
import json
import time
from ConfigMQTT import *
from paho.mqtt import client as mqtt_client


#baseURL = "http://simulator:5000/"
baseURL = "http://localhost:5000/"

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.connected_flag = True
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(CLIENT_USERNAME, CLIENT_PASSWORD)
    client.connected_flag = False
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        try:
            if "Ventil1/Value" in msg.topic:
                ret_val = requests.put(baseURL+"valve1/status", json={"value": msg.payload.decode()})
                print(ret_val.json())
            elif "Ventil2/Value" in msg.topic:
                ret_val = requests.put(baseURL+"valve2/status", json={"value": msg.payload.decode()})
                print(ret_val.json())
            elif "Ventil3/Value" in msg.topic:
                ret_val = requests.put(baseURL+"valve3/status", json={"value": msg.payload.decode()})
                print(ret_val.json())
            elif "ServoVentil/Value" in msg.topic:
                ret_val = requests.put(baseURL+"servovalve/status", json={"value": msg.payload.decode()})
                print(ret_val.json())
            elif "Waterpump/Value" in msg.topic:
                ret_val = requests.put(baseURL+"waterpump/status", json={"value": msg.payload.decode()})
                print(ret_val.json())
            elif "Ventil1/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"valve1/reset")
                print(ret_val.json())
            elif "Ventil2/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"valve2/reset")
                print(ret_val.json())
            elif "Ventil3/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"valve3/reset")
                print(ret_val.json())
            elif "ServoVentil/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"servovalve/reset")
                print(ret_val.json())
            elif "Waterpump/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"waterpump/reset")
                print(ret_val.json())
            elif "FlowSensor/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"flowsensor/reset")
                print(ret_val.json())        
            elif "LevelSensor/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"levelsensor/reset")
                print(ret_val.json())        
            elif "OutflowSensor/Reset" in msg.topic:
                ret_val = requests.put(baseURL+"outflowsensor/reset")
                print(ret_val.json())                        
        except Exception as some_error:
            print(some_error)

    client.subscribe(list(TOPICS.values()))
    client.on_message = on_message


def run():
    subscribe(client)
    client.loop_forever()
    

#def ParseAndProcessData(data, valve1, valve2, valve3, servo_valve, water_pump, flow_sensor, level_sensor, outflow_sensor):
def ParseAndProcessData(data, client):
    #valve1 props
    #valve1.status = data["valve1"]["status"]
    client.publish(TOPIC_FOR_INVIEW["valve1_status"], data["valve1"]["status"])
    
    #valve2 props
    #valve2.status = data["valve2"]["status"]
    client.publish(TOPIC_FOR_INVIEW["valve2_status"], data["valve2"]["status"])
    
    #valve3 props
    #valve3.status = data["valve3"]["status"]
    client.publish(TOPIC_FOR_INVIEW["valve3_status"], data["valve3"]["status"])
    
    #servo valve props
    #servo_valve.status = data["servo_valve"]["status"]
    client.publish(TOPIC_FOR_INVIEW["servo_valve_status"], data["servo_valve"]["status"])
    
    #waterpump props
    #water_pump.status = data["water_pump"]["status"]
    client.publish(TOPIC_FOR_INVIEW["water_pump_status"], data["water_pump"]["status"])
    
    #flow sensor props
    #flow_sensor.status = data["flow_sensor"]["status"]
    #flow_sensor.value = data["flow_sensor"]["value"]
    client.publish(TOPIC_FOR_INVIEW["flow_sensor_status"], data["flow_sensor"]["status"])
    client.publish(TOPIC_FOR_INVIEW["flow_sensor_value"], data["flow_sensor"]["value"])
    
    
    #level sensor props
    # level_sensor.status = data["level_sensor"]["status"]
    # level_sensor.value = data["level_sensor"]["value"]
    client.publish(TOPIC_FOR_INVIEW["level_sensor_status"], data["level_sensor"]["status"])
    client.publish(TOPIC_FOR_INVIEW["level_sensor_value"], data["level_sensor"]["value"])
    
    #outflow sensor props
    # outflow_sensor.status = data["outflow_sensor"]["status"]
    # outflow_sensor.value = data["outflow_sensor"]["value"]
    client.publish(TOPIC_FOR_INVIEW["outflow_sensor_status"], data["outflow_sensor"]["status"])
    client.publish(TOPIC_FOR_INVIEW["outflow_sensor_value"], data["outflow_sensor"]["value"])

def DataCheck(client):
    
    # valve1 = OnChange.OnChangeClass("valve1", client)
    # valve2 = OnChange.OnChangeClass("valve2", client)
    # valve3 = OnChange.OnChangeClass("valve3", client)
    # servo_valve = OnChange.OnChangeClass("servo_valve", client)
    # water_pump = OnChange.OnChangeClass("water_pump", client)
    # flow_sensor = OnChange.OnChangeClass("flow_sensor", client)
    # level_sensor = OnChange.OnChangeClass("level_sensor", client)
    # outflow_sensor = OnChange.OnChangeClass("outflow_sensor", client)
    
    while True:
        try:
            ret_val = requests.get(baseURL+"data")
            print(ret_val.text + "\n")
        
            json_data = json.loads(ret_val.text)
            
            #ParseAndProcessData(json_data, valve1, valve2, valve3, servo_valve, water_pump, flow_sensor, level_sensor, outflow_sensor)
            ParseAndProcessData(json_data, client)
            
            #valve1.status = json_data["valve1"]["status"]
            
            #client.publish(ALL_DATA_TOPIC, json.dumps(ret_val.json()))
            
            time.sleep(2)
            
        except BaseException as exception:
            print(exception)
            continue

if __name__ == '__main__':
    client = connect_mqtt()
    dataCheck = Thread(target=DataCheck, args=[client] )
    dataCheck.start()
    run()

""" def PumpSendValue(new_value):
    #new_value = input(valve_pump_status_values)
    ret_val = requests.put(baseURL+"waterpump/status", json={"value": new_value})
    print(ret_val.json()) """


""" def main():

    baseURL = "http://simulator:5000/"
    #baseURL = "http://localhost:5000/"

    sensor_operation = "Choose operation:\n 1. Read value\n 2. Read status\n 3. Reset sensor\n"
    servo_valve_operation = "Choose operation:\n 1. Read value\n 2. Set value\n 3. Reset\n"
    valve_pump_operation = "Choose operation:\n 1. Read status\n 2. Set status\n 3. Reset\n"
    valve_pump_status_values = "Choose value:\n 0. OFF\n 1. ON\n"

    while True:
        try:
            print()
            simulator_element = int(input(
            "Choose element:\n 1. Flow sensor\n 2. Level sensor\n 3. Outflow sensor\n 4. Servo valve\n 5. Valve 1\n 6. Valve 2\n 7. Valve 3\n 8. Water pump\n 9. InView data\n"))

            if simulator_element == 1:

                operation = int(input(sensor_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"flowsensor/value")
                    print(ret_val.json())

                elif operation == 2:
                    ret_val = requests.get(baseURL+"flowsensor/status")
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"flowsensor/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 2:

                operation = int(input(sensor_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"levelsensor/value")
                    print(ret_val.json())

                elif operation == 2:
                    ret_val = requests.get(baseURL+"levelsensor/status")
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"levelsensor/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 3:

                operation = int(input(sensor_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"outflowsensor/value")
                    print(ret_val.json())

                elif operation == 2:
                    ret_val = requests.get(baseURL+"outflowsensor/status")
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"outflowsensor/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 4:

                operation = int(input(servo_valve_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"servovalve/status")
                    print(ret_val.json())

                elif operation == 2:
                    new_value = input("Input new value:  ")
                    ret_val = requests.put(baseURL+"servovalve/status", json={"value": new_value})
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"servovalve/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 5:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"valve1/status")
                    print(ret_val.json())

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    ret_val = requests.put(baseURL+"valve1/status", json={"value": new_value})
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"valve1/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 6:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"valve2/status")
                    print(ret_val.json())

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    ret_val = requests.put(baseURL+"valve2/status", json={"value": new_value})
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"valve2/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 7:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"valve3/status")
                    print(ret_val.json())

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    ret_val = requests.put(baseURL+"valve3/status", json={"value": new_value})
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"valve3/reset")
                    print(ret_val.json())
                else:
                    continue

            elif simulator_element == 8:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    ret_val = requests.get(baseURL+"waterpump/status")
                    print(ret_val.json())

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    ret_val = requests.put(baseURL+"waterpump/status", json={"value": new_value})
                    print(ret_val.json())

                elif operation == 3:
                    ret_val = requests.put(baseURL+"waterpump/reset")
                    print(ret_val.json())
                else:
                    continue
            
            elif simulator_element == 9:
                ret_val = requests.get(baseURL+"data")
                print(ret_val.json())

        except Exception as some_error:
            print(some_error)
            continue


if __name__ == "__main__":
    main()
 """