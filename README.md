# Serial temperature logger

Reads a USB serial temperature sensor and logs the data.

The temperature sensor consists of an Arduino and a DS18B20 digital temperature sensor.

Arduino code is available [here](https://github.com/DavidFrankland/arduino-serial-ds18b20-fan-control)

## Configuration

Settings are stored in the file `settings.ini`. An example looks like:

```ini
[settings]
port = /dev/ttyUSB0
interval = 60
```

**port**: The port that the temperature is connected to.

**interval**: The number of seconds to wait between readings.
