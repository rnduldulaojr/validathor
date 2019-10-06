import validathor as value
import pytest

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

@pytest.mark.parametrize(
    "input_obj,expected", 
    [(True, True), (False, True), (1, True), (0, True), ("true", True), ("false", True)]
)
def test_boolean_type(input_obj, expected):
    schema = {
        "flag": value.boolean
    }

    validator = value.Validator(schema)

    test_data = {
        "flag": input_obj
    }

    assert validator.validate(test_data) == expected

def test_boolean_or_nullable_type():
    schema = {
        "flag": value.boolean | value.nullable
    }

    validator = value.Validator(schema)
    test_data = {
        "flag": None
    }

    assert validator.validate(test_data)


