#!/bin/bash
# sends a request to a URL passed as an argument
curl -o /dev/null -w '%{http_code}' -sLI "$1"
