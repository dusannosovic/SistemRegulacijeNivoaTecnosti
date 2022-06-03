import threading
import time
import random
from LevelSensor import LevelSensor
from FlowSensor import FlowSensor

def thread_function(level_sensor, flow_sensor):
    while(True):
        random_value = random.randrange(500)
        level_sensor.set_sensor_value(random_value,500)
        flow_sensor.set_sensor_value(random.randrange(15))
        print("Level sensor")
        print(level_sensor.read_sensor_value())
        print("Flow sensor")
        print(flow_sensor.read_sensor_value()) 
        time.sleep(1)

if __name__ == "__main__":
    level_sensor = LevelSensor()
    flow_sensor = FlowSensor()
    x = threading.Thread(target=thread_function, args=(level_sensor,flow_sensor,))
    x.start()