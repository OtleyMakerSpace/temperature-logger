import configparser
import datetime
import logging
import logging.config
import serial
import paho.mqtt.publish


# setup logging
logging.config.fileConfig("logging.ini")
logger = logging.getLogger()
logger.debug("starting up")

# read settings from config file
logger.debug("reading config settings")
config = configparser.ConfigParser()
config.read("settings.ini")
settings = config["settings"]
port = settings.get("port", '/dev/ttyUSB0')
logger.debug(f"port = {port}")
interval = settings.getint("interval", 60)
logger.debug(f"interval = {interval}")
mqtt_host = settings.get("mqtt-host")
logger.debug(f"mqtt_host = {mqtt_host}")
mqtt_topic = settings.get("mqtt-topic")
logger.debug(f"mqtt_topic = {mqtt_topic}")

serial = serial.Serial(port)
serial.reset_input_buffer()

line = ''
str = ''
time_to_read = datetime.datetime.now() + datetime.timedelta(seconds=1)
while True:
    logger.debug(f'waiting until {time_to_read}')
    while datetime.datetime.now() < time_to_read:
        line = serial.readline()
    try:
        str = line.decode()
        temperature = float(str)
        logger.info(temperature)
        try:
            logger.debug(f"sending {mqtt_topic} to {mqtt_host}")
            paho.mqtt.publish.single(mqtt_topic, temperature, hostname=mqtt_host)
        except:
            logger.debug(f'failed to publish {mqtt_topic} message')
    except:
        logger.debug(f'invalid temperature: {str}')
    time_to_read = datetime.datetime.now() + datetime.timedelta(seconds=interval)
