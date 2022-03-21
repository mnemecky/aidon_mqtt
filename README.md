# aidon_mqtt.py

A simple python application to interpret Hafslund AIDON smartmeter output and push to MQTT for further processing.

Based on skagmo's Aidon/Hafslund AMS data parser, found at https://github.com/skagmo/meter_reading

Supports the following environment variables for configuration:

- `MQTT_HOST` (required)
- `MQTT_TOPIC` (optional, defaults to /aidon)
- `SERIAL` (optional, defaults to /dev/ttyUSB0)

## Device support

Supports AIDON meters provided by Norwegian Hafslund (Elvia).

## Building the container

`docker build ./ -t aidon_mqtt`

## Running the container

`docker run -v /dev:/dev --privileged -e MQTT_HOST=<IP> aidon_mqtt`
