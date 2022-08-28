#!/usr/bin/python3

def multiple_returns(sentence):
    """ returns a tuple with length of a string """

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
