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

@pytest.mark.parametrize(
    "input_value,expected",
    [(10.00, True), (10, True), ("10.00", True)]
)
def test_decimal_type(input_value, expected):
    schema = {
        "price": value.decimal 
    }
    validator = value.Validator(schema)
    test_data = {
        "price": input_value
    }
    assert validator.validate(test_data) == expected

@pytest.mark.parametrize(
    "input_value,expected",
    [([1,2,3], True), ([], True)]
)
def test_array_type(input_value, expected):
    schema = {
        "items": value.array
    }
    validator = value.Validator(schema)
    test_data = {
        "items": input_value
    }
    assert validator.validate(test_data) == expected


@pytest.mark.parametrize(
    "input_value,expected",
    [({'a':1}, True),
     ({}, True)]
)
def test_map_type(input_value, expected):
    schema = {
        "mapping": value.dictionary
    }
    validator = value.Validator(schema)
    test_data = {
        "mapping": input_value
    }

    assert validator.validate(test_data) == expected
    