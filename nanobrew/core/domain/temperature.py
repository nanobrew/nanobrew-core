from .unit import Unit

class Temperature(Unit):
    def get_name(self):
        return 'Celcius'

    def get_description(self):
        return 'Temperature in degrees Celcius'

    def get_symbol(self):
        return u'°C'

    def get_precision(self):
        return 2
