
from expression_module.expression import Expression
from expression_module.angle import Angle
from expressionMatrix import ExpressionMatrix


if __name__ == '__main__':

    matrix_1 = ExpressionMatrix.from_joinTransform(
        a=Expression(0),
        alpha=Angle.from_degree(0),
        d=Expression('h'),
        theta=Expression('\\theta_1')
    )

    matrix_2 = ExpressionMatrix.from_joinTransform(
        a=Expression('L_1'),
        alpha=Angle.from_degree(0),
        d=Expression('d_2'),
        theta=Angle.from_degree(0)
    )

    matrix_3 = ExpressionMatrix.from_joinTransform(
        a=Expression(0),
        alpha=Angle.from_degree(90),
        d=Expression(0),
        theta=Expression('\\theta_3')
    )

    matrix_4 = ExpressionMatrix.from_joinTransform(
        a=Expression('L_2'),
        alpha=Angle.from_degree(0),
        d=Expression(0),
        theta=Angle.from_degree(0)
    )

    print(matrix_1, end='\n\n')

    print(matrix_2, end='\n\n')

    print(matrix_3, end='\n\n')

    print(matrix_4, end='\n\n')

    result = ((matrix_1 * matrix_2) * matrix_3) * matrix_4

    print(result)
