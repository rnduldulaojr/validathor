from validathor.core import PropertyValidator
from collections.abc import Mapping

class _IntegerTypeValidator(PropertyValidator):
    def validate(self, obj, prop, *args, **kwargs):
        if prop in obj and not isinstance(obj.get(prop), int):
            raise ValueError(f'{prop} is not an integer')
        return True

integer = _IntegerTypeValidator()

class _StringTypeValidator(PropertyValidator):
    def validate(self, obj, prop, *args, **kwargs):
        if prop in obj and not isinstance(obj.get(prop), str):
            raise ValueError(f'{prop} is not a string')
        return True

string = _StringTypeValidator()

class _BooleanTypeValidator(PropertyValidator):
    BOOLEAN_TYPES = (True, False, 1, 0, "true", "false")

    def validate(self, obj, prop, *args, **kwargs):
        if prop in obj and not obj.get(prop) in self.BOOLEAN_TYPES:
            raise ValueError(f'{prop} is not boolean')
        return True

boolean = _BooleanTypeValidator()

class _DecimalTypeValidator(PropertyValidator):
    def validate(self, obj, prop, *args, **kwargs):
        try:
            _ = float(obj.get(prop))
            return True
        except ValueError:
            raise ValueError(f'{prop} is not a decimal')

decimal = _DecimalTypeValidator()


class _ArrayTypeValidator(PropertyValidator):
    def validate(self, obj, prop, *args, **kwargs):
        if prop in obj and not isinstance(obj.get(prop), list):
            raise ValueError(f'{prop} is not an array/list')
        return True

array = _ArrayTypeValidator()

class _DictTypeValidator(PropertyValidator):
    def validate(self, obj, prop, *args, **kwargs):
        if prop in obj and not isinstance(obj.get(prop), Mapping):
            raise ValueError(f'{prop} is not a dict type')
        return True

dictionary = mapping = _DictTypeValidator()       