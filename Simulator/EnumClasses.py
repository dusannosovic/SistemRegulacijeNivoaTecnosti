from enum import IntEnum

class SensorStatus(IntEnum):
    OK = 0 # when sensor in operation
    FAILED = 1 # turned off

class ValveStatus(IntEnum):
    ON = 1 # valve on
    OFF = 0 # valve off
    FAILED = -1 #failed valve


class PumpOperation(IntEnum):
    ON = 1 # when pump in operation
    OFF = 0 # turned off
    FAILED = -1 #failed pump

class ServoValveStatus(IntEnum):
    FAILED = -1
    OK = 0