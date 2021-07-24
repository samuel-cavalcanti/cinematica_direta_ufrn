from expression_module.expression import Expression
from expression_module.angle import Angle
from expression_module.cos import Cos
from expression_module.sin import Sin
import numpy as np



class ExpressionMatrix:

    @staticmethod
    def from_joinTransform(a: Expression, alpha: Angle, d: Expression, theta: Angle):

        cos_theta = Cos(theta)
        sen_theta = Sin(theta)

        cos_alpha = Cos(alpha)
        sen_alpha = Sin(alpha)

        transform = ExpressionMatrix((4, 4))

        matrix = transform.__matrix

        matrix[0][0] = cos_theta

        matrix[0][1] = -sen_theta

        matrix[0, 2] = Expression(0)

        matrix[0][3] = a

        matrix[1][0] = cos_alpha*sen_theta

        matrix[1][1] = cos_alpha*cos_theta

        matrix[1][2] = -sen_alpha

        matrix[1][3] = -sen_alpha * d

        matrix[2][0] = sen_alpha * sen_theta
        matrix[2][1] = sen_alpha * cos_theta
        matrix[2][2] = cos_alpha
        matrix[2][3] = cos_alpha * d

        matrix[3, :] = Expression(0)

        matrix[-1][-1] = Expression(1)

        return transform

    def __init__(self, shape=None) -> None:

        if shape == None:
            self.__matrix = None
        else:
            self.__matrix = np.empty(shape, dtype=object)

    def __max_cell_str_len(self) -> int:
        max_len = 0
        for line in self.__matrix:
            for exp in line:
                string_size = len(str(exp))
                if string_size > max_len:
                    max_len = string_size

        return max_len

    def __str__(self) -> str:
        max_len = self.__max_cell_str_len()

        output_string = ''
        for line in self.__matrix:
            string_line = ' '.join(
                [self.__exp_to_formated_string(exp, max_len) for exp in line])

            output_string += f'|{string_line}|\n'

        return output_string[:-1]

    @staticmethod
    def __exp_to_formated_string(exp: Expression, max_len: int) -> str:
        str_exp = str(exp)
        space = (max_len - len(str_exp))*' '
        return f'{str_exp}{space}'

    def __mul__(self, other):

        new_matrix = ExpressionMatrix()

        if isinstance(other, ExpressionMatrix):
            new_matrix.__matrix = self.__matrix.dot(other.__matrix)

            return new_matrix

        raise Exception(
            'ExpressionMatrix only mult with another ExpressionMatrix')
