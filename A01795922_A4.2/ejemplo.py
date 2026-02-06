""""
Pylint
"""

#pylint: disable=too-few-public-methods
class Car:
    """Example class"""
    def _init_(self,color):
        self.color = color


MY_CAR = Car('blue')

def crash(car1, car2) : #pylint: disable=unused-arguments
    """An example function"""
    car1.color = 'burnt'

crash(Car('red'), MY_CAR)
