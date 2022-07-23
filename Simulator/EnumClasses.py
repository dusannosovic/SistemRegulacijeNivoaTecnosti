from enum import IntEnum

class SensorStatus(IntEnum):
    OK = 0 # when sensor in operation
    FAILED = 1 # turned off

class ValveStatus(IntEnum):
    ON = 1 # valve on
    OFF = 0 # valve off


class PumpOperation(IntEnum):
    ON = 1 # when pump in operation
    OFF = 0 # turned off
    

class ServoValveStatus(IntEnum):
    Level0percent = 0
    Level10percent = 10
    Level20percent = 20
    Level30percent = 30
    Level40percent = 40
    Level50percent = 50
    Level60percent = 60
    Level70percent = 70
    Level80percent = 80
    Level90percent = 90
    Level100percent= 100