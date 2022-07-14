from multiprocessing.sharedctypes import Value
import requests
import random
import json
#import PumpValue

from paho.mqtt import client as mqtt_client
from ConfigMQTT import *

'''def PumpSendValue(new_value):
    #new_value = input(valve_pump_status_values)
    ret_val = requests.put(baseURL+"waterpump/status", json={"value": new_value})
    print(ret_val.json())
'''


def OnConnect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.connected_flag = True
        #client.subscribe(ALL_DATA_TOPIC)
        
        initial_topcis = list(TOPIC_FOR_INVIEW.values())
        
        for topic in initial_topcis:
            client.subscribe(topic+"/Value")
            client.subscribe(topic+"/Status")
                
        #client.subscribe(TOPIC_FOR_INVIEW["valve1"][0] + "/Status")

    else:
        print("Failed to connect, return code %d\n", rc)


def OnMessage(client, userdata, message):
    print("STIGLA PORUKA:")
    try:
        msg = json.loads(message.payload)
        print(msg)
        print()
    except ValueError as e:
        print(message.payload.decode())
        print()


def main():

    client = mqtt_client.Client(SCADA_ID)
    client.username_pw_set(SCADA_USERNAME, SCADA_PASSWORD)
    client.connected_flag = False
    client.on_connect = OnConnect
    client.connect(BROKER, PORT)
    client.on_message = OnMessage
    client.loop_start()

    sensor_operation = "Choose operation:\n 1. Read value\n 2. Read status\n 3. Reset sensor\n"
    servo_valve_operation = "Choose operation:\n 1. Read value\n 2. Set value\n 3. Reset\n"
    valve_pump_operation = "Choose operation:\n 1. Read status\n 2. Set status\n 3. Reset\n"
    valve_pump_status_values = "Choose value:\n 0. OFF\n 1. ON\n"

    while True:

        if client.connected_flag == False:
            continue

        try:
            print()
            simulator_element = int(input(
                "Choose element:\n 1. Flow sensor\n 2. Level sensor\n 3. Outflow sensor\n 4. Servo valve\n 5. Valve 1\n 6. Valve 2\n 7. Valve 3\n 8. Water pump\n "))

            if simulator_element == 1:

                operation = int(input(sensor_operation))

                if operation == 1:
                    #ret_val = requests.get(baseURL+"flowsensor/value")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    #ret_val = requests.get(baseURL+"flowsensor/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"flowsensor/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["flowsensor_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 2:

                operation = int(input(sensor_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"levelsensor/value")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    # ret_val = requests.get(baseURL+"levelsensor/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"levelsensor/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["levelsensor_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 3:

                operation = int(input(sensor_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"outflowsensor/value")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    # ret_val = requests.get(baseURL+"outflowsensor/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"outflowsensor/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["outflowsensor_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 4:

                operation = int(input(servo_valve_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"servovalve/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    new_value = input("Input new value:  ")
                    # ret_val = requests.put(baseURL+"servovalve/status", json={"value": new_value})
                    # print(ret_val.json())
                    client.publish(TOPICS["servoventil_value"][0], new_value)

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"servovalve/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["servoventil_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 5:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"valve1/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    # ret_val = requests.put(baseURL+"valve1/status", json={"value": new_value})
                    # print(ret_val.json())
                    client.publish(TOPICS["ventil1_value"][0], new_value)

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"valve1/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["ventil1_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 6:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"valve2/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    # ret_val = requests.put(baseURL+"valve2/status", json={"value": new_value})
                    # print(ret_val.json())
                    client.publish(TOPICS["ventil2_value"][0], new_value)

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"valve2/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["ventil2_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 7:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"valve3/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    # ret_val = requests.put(baseURL+"valve3/status", json={"value": new_value})
                    # print(ret_val.json())
                    client.publish(TOPICS["ventil3_value"][0], new_value)

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"valve3/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["ventil3_reset"][0], 0)
                else:
                    continue

            elif simulator_element == 8:

                operation = int(input(valve_pump_operation))

                if operation == 1:
                    # ret_val = requests.get(baseURL+"waterpump/status")
                    # print(ret_val.json())
                    print("to be implemented...")

                elif operation == 2:
                    new_value = input(valve_pump_status_values)
                    # ret_val = requests.put(baseURL+"waterpump/status", json={"value": new_value})
                    # print(ret_val.json())
                    client.publish(TOPICS["waterpump_value"][0], new_value)

                elif operation == 3:
                    # ret_val = requests.put(baseURL+"waterpump/reset")
                    # print(ret_val.json())
                    client.publish(TOPICS["waterpump_reset"][0], 0)
                else:
                    continue

            # elif simulator_element == 9:
            #     ret_val = requests.get(baseURL+"data")
            #     print(ret_val.json())

        except Exception as some_error:
            print(some_error)
            continue


if __name__ == "__main__":
    main()
