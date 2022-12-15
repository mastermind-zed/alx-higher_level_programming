#!/bin/bash
# script that displays the size of the body of a response from a URL
curl -s "$1" | wc -c
