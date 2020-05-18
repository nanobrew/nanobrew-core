from ..option import Option
from ..parameter import Parameter


class Text(Option):
    def __init__(self, required: bool, label, description):
        self._required = required
        self._label = label
        self._description = description

    @classmethod
    def from_dict(cls, option):
        return Text(
            option['required'],
            option['label'],
            option['description']
        )

    def validate(self, value: Parameter) -> bool:
        errors = []
        if self._required and value is None:
            errors.append('Value can not be empty')

        return len(errors) == 0, errors

    def to_dict(self) -> dict:
        return {
            'option_type': 'text',
            'label': self._label,
            'description': self._description
        }