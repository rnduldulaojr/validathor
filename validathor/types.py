from validathor.core import PropertyValidator

class _IntegerTypeValidator(PropertyValidator):
    def validate(self, obj, prop):
        if prop in obj and not isinstance(obj.get(prop), int):
            raise ValueError(f'{prop} is not an integer')
        return True

integer = _IntegerTypeValidator()
