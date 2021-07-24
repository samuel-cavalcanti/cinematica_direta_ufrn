from numpy import exp
import numpy as np


class Expression:

    __slots__ = ['is_variable', '_value']

    def __init__(self, value) -> None:
        if isinstance(value, Expression):
            exp_value = value._value
            self.is_variable = value.is_variable
        else:
            self.is_variable = type(value) == str
            exp_value = value

        if exp_value == 0.0:
            self._value = 0
        else:
            self._value = exp_value

    def result_or_exception(self) -> float:
        if self.is_variable:
            raise Exception('Variable not result in number')

        return self._value

    def __str__(self) -> str:

        if self.is_variable:
            return self._value
        else:
            return str(self._value)

    def __eq__(self, o: object) -> bool:

        if isinstance(o, Expression):
            return self._value == o._value

        elif isinstance(0, (int, float, np.float64)):
            return self._value == o

        raise Exception(f'eq expression error Type, type: {type(o)} ')

    def __mul__(self, other):

        if other == 0.0 or self == 0.0:
            return Expression(0)
        elif other == 1.0:
            return Expression(self)
        elif self == 1.0:
            return Expression(other)

        if self.is_variable:
            return Expression(f'({self}*{other})')
        else:
            return Expression(self._value*other)

    def __rmul__(self, other):

        if other == 0.0 or self == 0.0:
            return Expression(0)
        elif other == 1.0:
            return Expression(self)
        elif self == 1.0:
            return Expression(other)

        if self.is_variable:
            return Expression(f'({other}*{self})')
        else:
            return Expression(other*self._value)

    def __neg__(self):

        if self.is_variable:
            return Expression(f'(-{self})')
        else:
            return Expression(-self._value)

    def __add__(self, other):

        if other is None:
            return self

        if self == 0.0 and other == 0.0:
            return Expression(0)

        if other == 0:
            return self

        if self == 0:
            return other

        if isinstance(other, Expression):
            if other.is_variable or self.is_variable:
                return Expression(f'({self}+{other})')

        else:
            if self.is_variable:
                return Expression(f'({self}+{other})')

            else:
                return Expression(self._value + other)

    def __iadd__(self, other):

        self = self + other
