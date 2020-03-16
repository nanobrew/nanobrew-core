# Terminology

## Sensor

A sensor represents an actual sensor. It contains the name and parameters, but
relies on its sensor type to read the sensor values.

## Sensor type

A sensor type determines how a sensor is read.

## Options and parameters

Sensor types, actor outputs, and heating logics need configuration to do
their jobs. This configuration is handled by two related concepts: options
and parameters.

Options represent the blueprints of the configuration: a DS18B20 temperature
sensor needs an address to function, so it has an option called "address".
The option has possible values, which are the actual addresses found on the
file system.

A *parameter* is the concrete value of an option; Sensor "1" has sensor type 
"DS18B20" and parameter "address" is set to "7863r7yfsiy". The read method 
of the sensor will receive parameters and can then return the value for that
specific address.