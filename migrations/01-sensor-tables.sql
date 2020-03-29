CREATE TABLE sensor_type (
  sensor_type_id TEXT PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE sensor_type_option (
  sensor_type_option_id TEXT PRIMARY KEY,
  sensor_type_id TEXT NOT NULL,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  description TEXT NOT NULL,

  FOREIGN KEY (sensor_type_id) 
    REFERENCES sensor_type (sensor_type_id) 
);

CREATE TABLE sensor (
  sensor_id TEXT PRIMARY KEY,
  sensor_type TEXT NOT NULL,
  name TEXT NOT NULL,

  FOREIGN KEY (sensor_type)
    REFERENCES sensor_type (type_id)
);

CREATE TABLE sensor_parameter (
  sensor_parameter_id TEXT PRIMARY KEY,
  sensor_id TEXT,
  name TEXT, -- Must be the same as the "sensor_type-option", mapping is done by the application.
  value TEXT, -- Might be an integer, string, or even JSON, validation is done by the application.

  FOREIGN KEY (sensor_id)
    REFERENCES sensor (sensor_id)
);
