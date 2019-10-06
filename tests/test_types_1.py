import validathor as value

def test_integer_type():
    schema = {
        "age": value.integer
    }

    validator = value.Validator(schema)

    test_data = {
        "age": 10
    }

    assert validator.validate( test_data )

def test_integer_type_fail():
    schema = {
        "age": value.integer
    }

    validator = value.Validator(schema)

    test_data = {
        "age": "this is a string"
    }

    assert isinstance(validator.validate( test_data ), list)

def test_string_type():
    schema = {
        "name": value.string
    }

    validator = value.Validator(schema)

    test_data = {
        "name": "10"
    }

    assert validator.validate( test_data )

def test_boolean_type():
    schema = {
        "flag": value.boolean
    }

    validator = value.Validator(schema)

    test_data = {
        "flag": True
    }

    assert validator.validate(test_data)

def test_boolean_or_nullable_type():
    schema = {
        "flag": value.boolean | value.nullable
    }

    validator = value.Validator(schema)
    test_data = {
        "flag": None
    }

    assert validator.validate(test_data)
