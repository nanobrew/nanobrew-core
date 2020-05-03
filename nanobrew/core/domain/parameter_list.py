from .parameter import Parameter

class ParameterList:
    _parameters: dict = {}

    @classmethod
    def from_dict(list, parameters: dict):
        return ParameterList(parameters)

    def __init__(self, parameters: dict = {}):
        for key, value in parameters.items():
            self._add_parameter(key, value)

    def get_parameter(self, name: str):
        if name not in self._parameters:
            return None

        return self._parameters[name]

    def _add_parameter(self, name: str, parameter):
        self._parameters[name] = Parameter(parameter)