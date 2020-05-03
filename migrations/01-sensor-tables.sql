CREATE TABLE sensor (
  sensor_id TEXT PRIMARY KEY,
  sensor_type TEXT NOT NULL,
  name TEXT NOT NULL
);

CREATE TABLE sensor_parameter (
  sensor_parameter_id TEXT PRIMARY KEY,
  sensor_id TEXT,
  name TEXT, -- Must be the same as the "sensor_type-option", mapping is done by the application.
  value TEXT, -- Might be an integer, string, or even JSON, validation is done by the application.

  FOREIGN KEY (sensor_id)
    REFERENCES sensor (sensor_id)
);
