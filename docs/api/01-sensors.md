# Sensors endpoint

The sensors endpoint gives the opportunity to retrieve information about the
sensors configured on the system.

## GET /sensors

```json
{
    "eec7f6f0-b5a7-47a5-b7b0-fb5b155f2716": {
        "name": "HLT temp sensor",
        "sensor_id": "eec7f6f0-b5a7-47a5-b7b0-fb5b155f2716",
        "sensor_type": "dummy",
        "value": "70",
        "unit": "°C"
    },
    "956edc23-0fd3-4e0c-9a84-d0d89711c56d": {
        "name": "HLT pressure sensor",
        "sensor_id": "956edc23-0fd3-4e0c-9a84-d0d89711c56d",
        "sensor_type": "pressure",
        "value": "200",
        "unit": "kPa"
    }
}
````
