#!/bin/bash
# set -x

cd test_project
rm -rf venv
cd ..
bash init_test_project.sh
cd test_project
pip uninstall -y django-introspectmodels
ln -s ../introspectmodels
coverage run --source="./introspectmodels" manage.py test introspectmodels
flake8 --output-file=../flake8.txt introspectmodels
coverage xml
mv coverage.xml ../
coverage report
rm introspectmodels
pip install ../dist/django-introspectmodels-0.1.tar.gz
cd ..
