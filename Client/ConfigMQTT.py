
BROKER = 'test.mosquitto.org'
PORT = 1883
# generate client ID with pub prefix randomly
CLIENT_ID = "Python1"

TOPICS = {
    "ventil1_value": ("ibis_2022/NivoRegTecnosti/Ventil1/Value", 0),
    "ventil2_value": ("ibis_2022/NivoRegTecnosti/Ventil2/Value", 0),
    "ventil3_value": ("ibis_2022/NivoRegTecnosti/Ventil3/Value", 0),
    "servoventil_value": ("ibis_2022/NivoRegTecnosti/ServoVentil/Value", 0),
    "waterpump_value": ("ibis_2022/NivoRegTecnosti/Waterpump/Value", 0),

    "ventil1_reset": ("ibis_2022/NivoRegTecnosti/Ventil1/Reset", 0),
    "ventil2_reset": ("ibis_2022/NivoRegTecnosti/Ventil2/Reset", 0),
    "ventil3_reset": ("ibis_2022/NivoRegTecnosti/Ventil3/Reset", 0),
    "servoventil_reset": ("ibis_2022/NivoRegTecnosti/ServoVentil/Reset", 0),
    "waterpump_reset": ("ibis_2022/NivoRegTecnosti/Waterpump/Reset", 0),

    "flowsensor_reset": ("ibis_2022/NivoRegTecnosti/FlowSensor/Reset", 0),
    "levelsensor_reset": ("ibis_2022/NivoRegTecnosti/LevelSensor/Reset", 0),
    "outflowsensor_reset": ("ibis_2022/NivoRegTecnosti/OutflowSensor/Reset", 0),
}

ALL_DATA_TOPIC = "ibis_2022/alldata"
