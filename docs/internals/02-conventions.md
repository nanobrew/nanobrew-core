# Conventions

## Measurements

* Measurements are always communicated in the following units;
    * Volume in liters;
    * Temperature in degrees Celcius;
    * Pressure in kilo Pascal

## Database naming

* Database table names are singular.
* IDs always use the table name.
* IDs are always text, because they're always UUIDs.
* References always use the table name, too.
* Field definition order is identifier, then references, then other fields.
