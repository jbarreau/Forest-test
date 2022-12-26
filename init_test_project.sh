#!/bin/bash
# set -x

cd test_project
python3 -m virtualenv venv
source venv/bin/activate

cd ..
python3 setup.py sdist
cd test_project
pip install -r requirements.txt