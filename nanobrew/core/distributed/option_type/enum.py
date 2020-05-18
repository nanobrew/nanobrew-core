from .option import Option


class Enum(Option):
    required: bool
    label: str
    description: str
    options: dict

    def __init__(self, required: bool, label: str, description: str, options: dict):
        self.required = required
        self.label = label
        self.description = description
        self.options = options

    def to_dict(self):
        return {
            'type': 'enum',
            'required': self.required,
            'label': self.label,
            'description': self.description,
            'options': self.options,
        }
