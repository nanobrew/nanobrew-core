from .option import Option


class OptionList:
    _options: dict = {}

    def __init__(self, options: dict):
        self._options = {}
        for name, option in options.items():
            self.add_option(name, option)

    def add_option(self, name, option: Option):
        self._options[name] = option

    def to_dict(self):
        return {key: option.to_dict() for key, option in self._options.items()}
