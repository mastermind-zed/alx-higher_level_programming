#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
