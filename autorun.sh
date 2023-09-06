#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/

python3 capture.py

echo programs saved
