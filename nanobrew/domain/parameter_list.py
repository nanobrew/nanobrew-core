from nanobrew.domain.parameter import Parameter

class ParameterList:
    def __init__(self):
        self._parameters = {}

    async def getParameter(self, name: str):
        return self._parameters[name]