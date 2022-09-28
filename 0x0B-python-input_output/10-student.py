#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ class Student that defines a student by: (based on 9-student.py) """
     def __init__(self, first_name, last_name, age):
         """ student instance  initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """ retrieves a dictionary representation of Student. """
        
        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
