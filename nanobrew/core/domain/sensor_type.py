from .option_list import OptionList
from .parameter_list import ParameterList
from .unit import Unit


class SensorType:
    async def read(self, parameters: ParameterList):
        raise NotImplementedError

    def get_unit(self) -> Unit:
        raise NotImplementedError

    def get_options(self) -> OptionList:
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    async def to_dict(self):
        raise NotImplementedError