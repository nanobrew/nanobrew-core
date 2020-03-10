class KettleList:
    _kettles: dict = {}

    def __init__(self, kettles: dict = {}):
        self._kettles = kettles
