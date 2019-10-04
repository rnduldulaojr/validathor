from validathor.core import PropertyValidator

class _RequiredPropertyValidator(PropertyValidator):
    def validate(self, obj, name):
        if name in obj and obj.get(name) is not None:
            return True
        raise ValueError(f'{name} is required')

required = _RequiredPropertyValidator()

class _NullablePropertyValidator(PropertyValidator):
    def willOverrideAnd(self):
        return True

    def validate(self, obj, name):
        return name in obj and obj.get(name) == None


nullable = _NullablePropertyValidator()