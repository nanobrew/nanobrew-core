from .option import Option
from .parameter_list import ParameterList


class OptionList:
    _options: dict = {}

    def __init__(self, options: dict):
        self._options = {}
        for name, option in options.items():
            self.add_option(name, option)

    def add_option(self, name, option: Option):
        self._options[name] = option

    def validate(self, parameter_list: ParameterList):
        error_list = {}
        for name, option in self._options.items():
            success, errors = option.validate(parameter_list.get_parameter(name))
            if not success:
                error_list[name] = errors

        return len(error_list) == 0, error_list

    def to_dict(self):
        return {key: option.to_dict() for key, option in self._options.items()}
