class Unit:
    def get_name(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError

    def get_symbol(self):
        raise NotImplementedError

    def get_precision(self):
        raise NotImplementedError

    def to_dict(self):
        return {
            'name': self.get_name(),
            'description': self.get_description(),
            'symbol': self.get_symbol()
        }