from abc import ABC, abstractmethod
from lab_python_oop.color import FigureColor
import math


class GeomFig(ABC):
    # конструктор
    def __init__(self):
        pass

    @abstractmethod
    def estimatesquare(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Rect(GeomFig):

    def __init__(self, ln, w, color_param):
        super().__init__()
        self.lenth = ln
        self.wide = w
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def estimatesquare(self):
        return self.lenth * self.wide

    def __repr__(self):
        return 'Площаь: {}   Длина: {}   Ширина: {} Цвет: {} '.format(self.estimatesquare(), self.lenth, self.wide, self.fc.colorproperty)


class Square(Rect):

    def __init__(self, ln, color_param):
        self.lenth = ln
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def estimatesquare(self):
        return self.lenth * self.lenth

    def __repr__(self):
        return 'Площаь: {}   Длина: {}   Цвет: {}'.format(self.estimatesquare(), self.lenth, self.fc.colorproperty)


class Circle(GeomFig):
    def __init__(self, rad, color_param):
        super().__init__()
        self.radius = rad
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def estimatesquare(self):
        return self.radius * self.radius * math.pi

    def __repr__(self):
        return 'Площаь: {}   Радиус: {}     Цвет: {}'.format(self.estimatesquare(), self.radius, self.fc.colorproperty)
