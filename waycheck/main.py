try:
    from .errors import WaycheckTypeError, WaycheckIndexError
except ImportError:
    from waycheck.errors import WaycheckTypeError, WaycheckIndexError

class Waycheck:
    def __init__(self, default_type=None, *args, **kwargs) -> None:
        self.args = args
        self.typecheck = kwargs
        self.default_type = default_type
    
    def __call__(self, func):
        def __inner__(*args, **kwargs) -> None:
            for index in range(len(args)):
                try:
                    if len(list(self.typecheck.values())) > 0 and list(self.typecheck.values())[index] == '*':
                        continue
                    t = [self.default_type if self.default_type != None else list(self.typecheck.values())[index]][0]
                    if not isinstance(list(args)[index], t):
                        raise WaycheckTypeError("Expected type {} for '{}' at argument position {}, instead got type {}".format(t, list(args)[index], index, type(list(args)[index])))
                except IndexError:
                    raise WaycheckIndexError('IndexError: You must provide a type check value for all arguments.\nWaycheck arguments: {}\nFunciton arguments: {}'.format(self.typecheck, args))
            return func(*args, **kwargs)
        return __inner__
