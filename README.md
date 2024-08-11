# Serial temperature logger

Reads a USB serial temperature sensor and logs the data.

The temperature sensor consists of an Arduino running "some code" (where?) and a DS18B20 digital temperature sensor.

## Configuration

Settings are stored in the file `settings.ini`. An example looks like:

```
[settings]
port = /dev/ttyUSB0
interval = 60
```

**port**: The port that the temperature is connected to.

**interval**: The number of seconds to wait between readings.

## To do

Add link to the Arduino code