from __future__ import annotations

import yaml

class Config:
    def __init__(self, config: dict):
        self._config = config

    @classmethod
    def from_yaml_file(cls, file_name) -> Config:
        with open(file_name, 'r') as file_handle:
            config = yaml.load(file_handle,Loader=yaml.FullLoader)
            return cls(config)

    def get(self, path: str, default=None):
        try:
            return self._getNode(path.split('.'), self._config)
        except KeyError as e:
            if default is None:
                raise e
            return default

    def _getNode(self, segments: list, nodes: dict):
        current = segments.pop(0)
        if current not in nodes:
            raise KeyError('Unknown config key "%s"' % current)
        
        nodes = nodes[current]
        if len(segments) > 0:
            return self._getNode(segments, nodes)

        return nodes
