import asyncio

from nanobrew.core.domain.option_list import OptionList
from nanobrew.core.domain.parameter_list import ParameterList
from nanobrew.core.domain.sensor_type import SensorType
from nanobrew.core.domain.temperature import Temperature
from nanobrew.core.domain.unit import Unit


class DummySensorType(SensorType):
    last: float = 0
    step: float = 0.25

    async def read(self, parameters: ParameterList):
        self.last = self.last + self.step
        return self.last

    def get_unit(self) -> Unit:
        return Temperature()

    async def options(self) -> OptionList:
        return OptionList()
