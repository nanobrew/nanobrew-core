from nanobrew.app import App
from nanobrew.domain.sensor import Sensor
from nanobrew.domain.sensor_list import SensorList
from nanobrew.domain.sensor_repository import SensorRepository
from nanobrew.domain.parameter_list import ParameterList

class StubSensorRepository(SensorRepository):
    _app: App

    def __init__(self, app: App):
        self._app = app

    async def findAll(self) -> SensorList:
        sensor_type = await self._app.get_sensor_type("dummy")

        sensor_list = SensorList()
        await sensor_list.add_sensor("X", Sensor(sensor_type, ParameterList({})))

        return sensor_list