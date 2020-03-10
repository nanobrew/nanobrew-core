from nanobrew.domain.option_list import OptionList
from nanobrew.domain.parameter_list import ParameterList

class SensorType:
    async def read(self, parameters: ParameterList):
        raise NotImplementedError

    async def options(self) -> OptionList:
        raise NotImplementedError
