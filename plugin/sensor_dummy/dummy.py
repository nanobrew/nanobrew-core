import asyncio

from nanobrew.domain.sensor_type import SensorType
from nanobrew.domain.config.parameter import Parameter
from nanobrew.domain.config.option import Option
from nanobrew.domain.config.option_list import OptionList
from nanobrew.domain.config.parameter_list import ParameterList

class DummySensorType(SensorType):
    last: float = 0
    step: float = 0.25

    async def read(self, parameters: ParameterList):
        self.last = self.last + self.step
        return self.last

    async def options(self) -> OptionList:
        return OptionList()
