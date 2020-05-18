from .option import Option


class Text(Option):
    required: bool
    label: str

    def __init__(self, required: bool, label: str):
        self.required = required
        self.label = label

    def to_dict(self):
        return {
            'type': 'text',
            'required': self.required,
            'label': self.label
        }