from .option import Option
from .parameter_list import ParameterList


class Options:
    _options: dict = {}

    def __init__(self, options: dict):
        self._options = options

    @classmethod
    def from_dict(cls, options: dict):
        # Make Option objects here.
        self = Options(options)
        return self

    def to_dict(self):
        return self._options
