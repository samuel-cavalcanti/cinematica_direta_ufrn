from .expression import Expression


class FunctionExpression(Expression):

    def __init__(self, expression: Expression, function) -> None:

        if expression.is_variable:
            value = f'{function}({expression})'
        else:
            value = function(expression.result_or_exception())
            value = round(value, 15) #precision of system
            if value == 0.0:
                value = 0.0

        super().__init__(value)
