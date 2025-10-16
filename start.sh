#!/bin/bash

cd /home/pi/temperature-logger
git pull >git.log 2>&1
source .venv/bin/activate
pip install -r requirements.txt
python temperature-logger.py
