#!/usr/bin/python3
""" my int """


class MyInt(int):
    """ class MyInt that inherits from int """
    def __init__(self, number):
        self.number = number

    def __ne__(self, value):
        return (self.number == value)

    def __eq__(self, value):
        return (self.number != value)

    def __str__(self):
        return (str(self.number))
