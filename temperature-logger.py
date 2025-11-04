import configparser
import datetime
import logging
import logging.config
import serial
import paho.mqtt.publish


# setup logging
logging.config.fileConfig("logging.ini")
logger = logging.getLogger()
logger.info("starting up")

# read settings from config file
logger.info("reading config settings")
config = configparser.ConfigParser()
config.read("settings.ini")

# global settings
settings = config["settings"]
port = settings.get("port", '/dev/ttyUSB0')
logger.info(f"port = {port}")
interval = settings.getint("interval", 60)
logger.info(f"interval = {interval}")

# MQTT settings
mqtt_settings = config["mqtt"]
mqtt_host = mqtt_settings.get("host", "localhost")
logger.info(f"mqtt_host = {mqtt_host}")
mqtt_topic = mqtt_settings.get("topic", "temperature")
logger.info(f"mqtt_topic = {mqtt_topic}")
mqtt_qos = mqtt_settings.getint("qos", 0)
if mqtt_qos < 0 or mqtt_qos > 2:
    raise Exception("MQTT QoS must be in the range 0 to 2")
logger.info(f"mqtt_qos = {mqtt_qos}")


serial = serial.Serial(port)
serial.reset_input_buffer()

line: bytes
time_to_read = datetime.datetime.now() + datetime.timedelta(seconds=1)
while True:
    logger.debug(f'waiting until {time_to_read}')
    while datetime.datetime.now() < time_to_read:
        line = serial.readline()
    try:
        line_str = line.decode()
        temperature = float(line_str)
        logger.debug(f'temperature is {temperature}')
        try:
            logger.debug(f"sending {mqtt_topic} to {mqtt_host}")
            paho.mqtt.publish.single(mqtt_topic, temperature, hostname=mqtt_host, qos=mqtt_qos)
        except Exception as ex:
            logger.error(f'failed to publish {mqtt_topic} message: {ex}')
    except:
        logger.error(f'invalid temperature: {line_str}')
    time_to_read = datetime.datetime.now() + datetime.timedelta(seconds=interval)
