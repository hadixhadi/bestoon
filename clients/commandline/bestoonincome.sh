#!/bin/bash
myToken=1234
curl --data "token=$myToken&amount=$1&text=$2" http://127.0.0.1:8000/submit/income/

