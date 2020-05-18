class Option:
    def validate(self, value):
        raise NotImplementedError

    @classmethod
    def from_dict(self, option: dict):
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError