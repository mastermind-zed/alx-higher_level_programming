#!/usr/bin/python3
"""  Integer validator """


class BaseGeometry:
    """ BaseGeometry = __import__('7-base_geometry').BaseGeometry """
     def area(self):
         """ class BaseGeometry (based on 6-base_geometry.py ) """
         raise Exception("area() is not implemented")
     def integer_validator(self, name, value):
         """ Integer validator  """  
         if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
