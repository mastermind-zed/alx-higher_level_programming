#!/usr/bin/python3
""" Student to disk and reload """


class Student: 
    """ class Student that defines a student by: (based on 10-student.py) """
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """ student instance  initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Gets a dictionary representation of the Student """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student """
        for k, v in json.items():
            setattr(self, k, v)
