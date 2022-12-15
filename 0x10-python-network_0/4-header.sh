#!/bin/bash
# script that takes URL as argument, sends GET request to URL, displays response
curl -sH "X-School-User-Id: 98" "$1"
