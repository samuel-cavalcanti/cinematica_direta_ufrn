
from .function_expression import FunctionExpression
from .angle import Angle
import numpy as np


class Sin(FunctionExpression):
    __slots__ = ['__sen_theta', '__sen_value']

    def __init__(self, theta: Angle) -> None:

        if theta.is_variable:
            super().__init__(theta, 'sin')
        else:
            super().__init__(theta.to_rads(), np.sin)
