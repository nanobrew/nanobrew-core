from ..option import Option
from ..parameter import Parameter


class Text(Option):
    def __init__(self, required: bool, label, description):
        self._required = required
        self._label = label
        self._description = description

    def validate(self, parameter: Parameter) -> bool:
        errors = []

        if self._required and parameter is None:
            errors.append('Value can not be empty')

        if (parameter is not None) and (not str(parameter.get_value()).isdigit()):
            errors.append('Value is not numeric')

        return len(errors) == 0, errors

    def to_dict(self) -> dict:
        return {
            'option_type': 'text',
            'label': self._label,
            'description': self._description
        }