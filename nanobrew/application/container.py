import nanoinject

class Container:
    """An incredibly simple Façade over the functionality of nanoinject"""
    def __init__(self, container: nanoinject.Container):
        self._container = container

    def get_service(self, service_name: str):
        return self._container.get(service_name)