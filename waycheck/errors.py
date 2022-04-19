from xml.dom import NotFoundErr


class WaycheckTypeError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class WaycheckIndexError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
