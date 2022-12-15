#!/bin/bash
# script that takes URL, sends GET request to URL displays the body of response
curl -sfL "$1" -X GET
