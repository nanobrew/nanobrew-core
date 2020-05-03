from .parameter import Parameter


class Option:
    def validate(self, parameter: Parameter) -> bool:
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError