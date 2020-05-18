from ..option import Option


class Decimal(Option):
    def __init__(self, required: bool, label, description):
        self._required = required
        self._label = label
        self._description = description

    @classmethod
    def from_dict(cls, option):
        return Decimal(
            option['required'],
            option['label'],
            option['description']
        )

    def validate(self, value) -> bool:
        errors = []

        if self._required and value is None:
            errors.append('Value can not be empty')

        if (value is not None) and (not str(value).isdigit()):
            errors.append('Value is not numeric')

        return len(errors) == 0, errors

    def to_dict(self) -> dict:
        return {
            'option_type': 'decimal',
            'label': self._label,
            'description': self._description
        }