from .function_expression import FunctionExpression
from .angle import Angle
import numpy as np


class Cos(FunctionExpression):

    def __init__(self, theta: Angle) -> None:

        if theta.is_variable:
            super().__init__(theta, 'cos')
        else:
            super().__init__(theta.to_rads(), np.cos)
