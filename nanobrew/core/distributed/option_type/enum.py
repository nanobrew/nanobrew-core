from .option import Option


class Enum(Option):
    def __init__(self, required: bool, label: str, options: dict):
        self.required = required
        self.label = label
        self.options = options

    def to_dict(self):
        return {
            'type': 'enum',
            'required': self.required,
            'label': self.label,
            'options': self.options
        }
