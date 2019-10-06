
class Validator:
    def __init__(self, schema):
        self._schema = schema

    def validate(self, obj):
        errors = []
        for key, validator in self._schema.items():
            try:
                validator.validate(obj, key)
            except ValueError as err:
                errors.append(err)
        
        return errors or True
