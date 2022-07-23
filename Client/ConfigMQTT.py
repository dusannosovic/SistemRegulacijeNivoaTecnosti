
#BROKER = "localhost"
#BROKER = 'test.mosquitto.org'
BROKER = 'broker.hivemq.com'
#BROKER = 'mqtt.fluux.io'
#BROKER = 'broker.emqx.io'

PORT = 1883
# generate client ID with pub prefix randomly
CLIENT_ID = "ibis_client"
CLIENT_USERNAME = "client"
CLIENT_PASSWORD = "client123"

SCADA_ID = "ibis_scadaClient"
SCADA_USERNAME = "scadaClient"
SCADA_PASSWORD = "scadaClient123"

# ove topic-e koristi InView (clientScadaSimulator) kako bi mogao da menja vrednosti elemenata
# na ove topic-e se subscribe-uje client, i prosledjuje vrednosti rest api-ju
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



# na ove topic-e se subscribe-je InView (clientScadaSimulator)
# client nakon dobavljanja podataka od rest api-ja parsira podatke i za svaki element publish-uje
# na odgovarajuci topic

TOPIC_FOR_INVIEW = {
    # Ovo je za 0/1 vrednosti i servo koji ide od 0-100
    "valve1_status": "ibis_2022/NivoRegTecnosti/InView/Ventil1/Status",
    "valve2_status": "ibis_2022/NivoRegTecnosti/InView/Ventil2/Status",
    "valve3_status": "ibis_2022/NivoRegTecnosti/InView/Ventil3/Status",
    "servo_valve_status": "ibis_2022/NivoRegTecnosti/InView/ServoVentil/Status",
    "water_pump_status": "ibis_2022/NivoRegTecnosti/InView/Waterpump/Status",
    
    # Ovo je za ON/OFF vrednosti (servo ovde ne treba jer mu je status uvek brojcana vrednost 0-100 )
    "valve1_status_text": "ibis_2022/NivoRegTecnosti/InView/Ventil1/StatusText",
    "valve2_status_text": "ibis_2022/NivoRegTecnosti/InView/Ventil2/StatusText",
    "valve3_status_text": "ibis_2022/NivoRegTecnosti/InView/Ventil3/StatusText",
    "water_pump_status_text": "ibis_2022/NivoRegTecnosti/InView/Waterpump/StatusText",

    "flow_sensor_status": "ibis_2022/NivoRegTecnosti/InView/FlowSensor/Status",
    "level_sensor_status": "ibis_2022/NivoRegTecnosti/InView/LevelSensor/Status",
    "outflow_sensor_status": "ibis_2022/NivoRegTecnosti/InView/OutflowSensor/Status",
    
    "flow_sensor_value": "ibis_2022/NivoRegTecnosti/InView/FlowSensor/Value",
    "level_sensor_value": "ibis_2022/NivoRegTecnosti/InView/LevelSensor/Value",
    "outflow_sensor_value": "ibis_2022/NivoRegTecnosti/InView/OutflowSensor/Value",
}



ALL_DATA_TOPIC = "ibis_2022/alldata"
