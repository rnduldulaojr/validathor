from abc import ABC, abstractmethod

class AbstractValidator(ABC):
    def willOverrideAnd(self):
        return False

    @abstractmethod
    def validate(self, obj, prop):
        raise ValueError()

class AndPropertyValidator(AbstractValidator):
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2

    def validate(self, obj, prop):
        return self._v1.validate(obj, prop) and self._v2.validate(obj, prop)

class OrPropertyValidator(AbstractValidator):
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
    
    def validate(self, obj, prop):
        return self._v1.validate(obj, prop) or self._v2.validate(obj, prop)

class PropertyValidator(AbstractValidator):
    @abstractmethod
    def validate(self, obj, prop):
        raise ValueError()


    def __or__(self, other):
        if self.willOverrideAnd() or other.willOverrideAnd():
            return OrPropertyValidator(self, other)
        return AndPropertyValidator(self, other)

    def __and__(self, other):
        if self.willOverrideAnd() or other.willOverrideAnd():
            return OrPropertyValidator(self, other)
        return AndPropertyValidator(self, other)


