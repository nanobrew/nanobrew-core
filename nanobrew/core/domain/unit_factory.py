from .temperature import Temperature
from .unit import Unit


class UnitFactory:
    unit_types = {
        'temperature': Temperature
    }

    def __init__(self):
        pass

    def create_unit(self, unit_type: str) -> Unit:
        if unit_type in self.unit_types:
            return self.unit_types[unit_type]()

