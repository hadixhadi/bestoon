#!/bin/bash
curl --data "token=$1&amount=$2&text=$3" http://127.0.0.1:8000/submit/expense/

