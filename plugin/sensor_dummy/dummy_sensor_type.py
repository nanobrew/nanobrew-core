import asyncio

from nanobrew.core.domain.option_type.enum import Enum
from nanobrew.core.domain.option_type.number import Number
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

    def get_options(self) -> OptionList:
        return OptionList({
            'step': Enum(
                True,
                'Step size',
                {
                    '0.1': 0.1,
                    '0.25': 0.25,
                    '1.0': 1.0,
                    '2.0': 2.0,
                    '3.0': 3.0
                },
                'The step the dummy should be increased with on every tick'
            ),
            'start': Number(
                True,
                'Start',
                'The value the sensor should start with'
            )
        })

    def get_name(self):
        return 'dummy'

    async def to_dict(self):
        return {
            'name': self.get_name(),
            'options': self.get_options().to_dict()
        }
