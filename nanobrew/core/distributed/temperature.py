from .unit import Unit

class Temperature(Unit):
    def get_unit_type(self):
        return 'temperature'