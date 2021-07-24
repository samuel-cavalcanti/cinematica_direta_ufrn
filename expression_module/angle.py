from .expression import Expression
import numpy as np


class Angle(Expression):

    __slots__ = ['__is_degree']

    def from_degree(degree_value: float):
        angle = Angle(degree_value)
        angle.__is_degree = True

        return angle

    @staticmethod
    def from_rads(rads_value: float):
        angle = Angle(rads_value)
        angle.__is_degree = False

        return angle

    def __init__(self, value) -> None:
        self.__is_degree = None
        super().__init__(value)

    def to_rads(self):

        if self.is_variable:
            raise Exception('to_rads not implemented for variable')

        if not self.__is_degree:
            return self
        
        new_angle = Angle(self._value / 180 * np.pi)
        new_angle.__is_degree = False
        return new_angle

    def to_degree(self):
        if self.is_variable:
            raise Exception('to_degree not implemented for variable')

        if self.__is_degree:
            return self

        new_angle = Angle(self._value*180/np.pi)
        new_angle.__is_degree = True

        return new_angle
