## Validathor

Validathor is trying to be like Cerberus (https://docs.python-cerberus.org/) but with validation rules declared just like that of Laravel's (PHP).

Sample Usage:
```python

from validathor import Validator, required, nullable, integer, string

schema = {
    "name": required | string,
    "age": required | integer,
    "address": nullable
}

validator = Validator( schema )

input_obj = {
    "name": "Odin",
    "age": 10000,
    "address": "Asgard"
}

validator.validate(input_obj)

```

## WORK IN PROGRESS