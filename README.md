# Serial temperature logger

Reads a USB serial temperature sensor and sends the reading to an MQTT broker.

The temperature sensor consists of an Arduino and a DS18B20 digital temperature sensor.

Arduino code is available [here](https://github.com/DavidFrankland/arduino-serial-ds18b20-fan-control)

## Configuration

Settings are stored in the file `settings.ini`. An example looks like:

```ini
[settings]
port = /dev/ttyUSB0
interval = 60

[mqtt]
host = 10.1.0.1
topic = temperature/display-pi
qos = 1
```

The `[settings]` section contains global settings:

**port**: The port that the temperature is connected to.

**interval**: The number of seconds to wait between readings.

The `[mqtt]` section contains MQTT-specific settings:

**host**: The MQTT broker to use.

**topic**: MQTT topic for temperature message.

**qos** (0-2): MQTT Quality of Service to use.
