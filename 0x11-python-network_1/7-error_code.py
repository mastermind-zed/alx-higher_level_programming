#!/usr/bin/python3
"""
    Entry Point
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
