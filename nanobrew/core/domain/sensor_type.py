from .option_list import OptionList
from .parameter_list import ParameterList
from .unit import Unit


class SensorType:
    async def read(self, parameters: ParameterList):
        raise NotImplementedError

    def get_unit(self) -> Unit:
        raise NotImplementedError

    async def options(self) -> OptionList:
        raise NotImplementedError
