from .option_type.enum import Enum
from .option_type.decimal import Decimal
from .option_type.text import Text


class Options:
    '''This class is a facade over options.'''
    _options: dict = {}

    def add_enum_option(self, required: bool, name: str, label: str, options: dict):
        self._options[name] = Enum(required, label, options)

    def add_decimal_option(self, required: bool, name: str, label: str):
        self._options[name] = Decimal(required, label)

    def add_text_option(self, required: bool, name: str, label: str):
        self._options[name] = Text(required, label)

    def to_dict(self):
        options = {}
        for (name, option) in self._options.items():
            options[name] = option.to_dict()

        return options
