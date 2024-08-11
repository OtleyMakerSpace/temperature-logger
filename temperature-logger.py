import configparser
import datetime
import logging
import logging.config
import serial

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
    except:
        logger.debug(f'invalid temperature: {str}')
    time_to_read = datetime.datetime.now() + datetime.timedelta(seconds=interval)
