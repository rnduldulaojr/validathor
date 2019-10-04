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
