from ..option import Option
from ..parameter import Parameter


class Enum(Option):
    def __init__(self, required: bool, label, options, description):
        self._required = required
        self._label = label
        self._options = options
        self._description = description

    def validate(self, parameter: Parameter):
        errors = []

        if parameter is None:
            errors.append('Value can not be empty')

        if (parameter is not None) and (parameter.get_value() not in self._options.values()):
            errors.append('Value is not in list of possible values')

        return len(errors) == 0, errors

    def to_dict(self) -> dict:
        return {
            'option_type': 'enum',
            'label': self._label,
            'options': self._options,
            'description': self._description
        }
