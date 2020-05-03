from ..option import Option
from ..parameter import Parameter


class Enum(Option):
    def __init__(self, label, options, description):
        self._label = label
        self._options = options
        self._description = description

    def validate(self, property: Parameter) -> bool:
        return False

    def to_dict(self) -> dict:
        return {
            'option_type': 'enum',
            'label': self._label,
            'options': self._options,
            'description': self._description
        }
