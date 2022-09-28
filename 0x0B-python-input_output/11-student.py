#!/usr/bin/python3
""" Student to disk and reload """


class Student:
    """ class Student that defines a student by: (based on 10-student.py) """
    def __init__(self, first_name, last_name, age):
        """ student instance  initialization  """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student Instance.
            Args:
                json (dictionary): reload data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
