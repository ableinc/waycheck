try:
    from .main import Waycheck
    from .errors import WaycheckTypeError, WaycheckIndexError
except ImportError:
    from waycheck.main import Waycheck
    from waycheck.errors import WaycheckTypeError, WaycheckIndexError

__all__ = [Waycheck, WaycheckTypeError, WaycheckIndexError]
