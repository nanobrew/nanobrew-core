class ValidationFailed(Exception):
    def __init__(self, errors):
        self._errors = errors

    def __str__(self):
        return 'Validation has failed'

    def get_errors(self):
        return self._errors