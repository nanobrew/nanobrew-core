import logging

from nanobrew.core.distributed.sensor_reader import SensorReader


class DummySensorReader(SensorReader):
    _start: float
    _step: float
    _current: float

    def __init__(self, start: float, step: float):
        self._start = float(start)
        self._current = float(start)
        self._step = float(step)

    async def read(self) -> float:
        self._current = self._current + self._step
        logging.info('DummySensorReader(%.2f, %.2f)::read() -> %.2f' % (self._start, self._step, self._current))
        return self._current
