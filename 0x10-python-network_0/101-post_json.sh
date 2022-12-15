#!/bin/bash
# script that sends a JSON post request to a URL passed as the first arg
curl -s -X POST $1 -H 'Content-Type: application/json' -d @$2
