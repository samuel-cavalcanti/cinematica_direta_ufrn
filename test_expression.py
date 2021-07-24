from numpy import sin
from expression_module.expression import Expression
from expression_module.angle import Angle
from expression_module.cos import Cos
from expression_module.sin import Sin

import unittest


class TestExpression(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.__variable = '\\theta_1'
        self.__const_value = 45
        self.__theta_1 = Expression(self.__variable)
        self.__const_theta =  Angle.from_degree(self.__const_value)

    def test_angle(self):
       

        self.assertEqual(self.__theta_1.__str__(), self.__variable)
        self.assertEqual(self.__const_theta.__str__(), str(self.__const_value))

    def test_cos(self):
      

        cos_45 = Cos(self.__const_theta)
        cos_theta = Cos(self.__theta_1)

        self.assertEqual(f'cos({self.__variable})', cos_theta.__str__())

        self.assertEqual('0.707106781186548', cos_45.__str__())

    def test_sin(self):

      
        sin_theta = Sin(self.__theta_1)
        sin_45 = Sin(self.__const_theta)

        self.assertEqual('0.707106781186548', sin_45.__str__())
        self.assertEqual(f'sin({self.__variable})', sin_theta.__str__())

    def test_multiplication(self):

     

        sin_theta = Sin(self.__theta_1)
        sin_45 = Sin(self.__const_theta)
        cos_45 = Cos(self.__const_theta)
        cos_theta = Cos(self.__theta_1)

        self.assertEqual((5*sin_theta).__str__(), f'(5*sin({self.__variable}))')
        self.assertEqual((5*cos_theta).__str__(), f'(5*cos({self.__variable}))')

        self.assertEqual((2*cos_45).__str__(), (2*sin_45).__str__())

        self.assertEqual(str(10), str(2 * Expression(5)))

    def test_expresion_equal(self):

        self.assertEqual(Expression(5) == 5, True)
        self.assertEqual(Expression(5) == 5.0, True)
        self.assertEqual(Expression(5) == Expression(5), True)




if __name__ == "__main__":

    unittest.main()
