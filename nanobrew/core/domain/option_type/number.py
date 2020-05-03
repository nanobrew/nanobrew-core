from ..option import Option
from ..parameter import Parameter


class Number(Option):
    def __init__(self, label, description):
        self._label = label
        self._description = description

    def validate(self, property: Parameter) -> bool:
        return False

    def to_dict(self) -> dict:
        return {
            'option_type': 'number',
            'label': self._label,
            'description': self._description
        }