from .parameter import Parameter

class ParameterList:
    def __init__(self, parameters: dict = {}):
        self._parameters = parameters

    async def getParameter(self, name: str):
        return self._parameters[name]