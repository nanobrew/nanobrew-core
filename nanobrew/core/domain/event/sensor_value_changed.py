from ..domain_event import DomainEvent


class SensorValueChanged(DomainEvent):
    def __init__(self, sensor_id, value, unit):
        self._sensor_id = sensor_id
        self._value = value
        self._unit = unit

    def get_name(self):
        return 'sensor_value_changed'

    def to_dict(self):
        return {
            'sensor_id': self._sensor_id,
            'value': self._value,
            'unit': self._unit.to_dict()
        }