#!/usr/bin/python3
""" my int """


class MyInt(int):
    """ class MyInt that inherits from int """ 
    def __init__(self, value):
        self.num = value

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other

    def __str__(self):
        return (str(self.num))
