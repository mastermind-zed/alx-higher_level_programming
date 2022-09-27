#!/usr/bin/python3
""" my int """


class MyInt(int):
    def __eq__(self, other):
        """ Override equals, inverting it. """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Override not-equals, inverting it."""
        return int(self) == int(other)
