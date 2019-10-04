import validathor as value
import pytest

@pytest.fixture
def simple():
    return {
        "name": value.required
    }

def test_required_simple(simple):

    test_data = {
        "name": "John"
    }

    validator = value.Validator( simple )
    assert validator.validate(test_data)

def test_required_simple_2( simple ):
    test_data = {
        "name": None
    }

    validator = value.Validator( simple )
    result = validator.validate( test_data ) 
    assert isinstance( result, list )
    
def test_nullable_simple_1():
    schema = {
        "name": value.nullable
    }

    test_data = {
        "name": None
    }

    validator = value.Validator( schema )
    assert validator.validate( test_data )

def test_required_and_nullable():
    schema = {
        "name": value.required | value.nullable
    }

    test_data = {
        "name": None
    }

    validator = value.Validator( schema )
    assert validator.validate( test_data )

def test_required_and_nullable_on_empty():
    schema = {
        "name": value.required | value.nullable
    }

    test_data = {
    }

    validator = value.Validator( schema )
    result = validator.validate( test_data )
    assert isinstance( result, list )

