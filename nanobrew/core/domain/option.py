from .parameter import Parameter


class Option:
    def validate(self, parameter: Parameter):
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError