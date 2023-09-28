#!/bin/bash
# Get the byte size of the HTTP body of the response header for a given URL.

curl -s "$1" | wc -c
