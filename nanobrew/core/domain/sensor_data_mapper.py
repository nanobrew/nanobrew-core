class SensorDataMapper:
    async def fetch_all(self):
        raise NotImplementedError

    async def persist(self, sensor):
        raise NotImplementedError
