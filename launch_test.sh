#!/bin/bash
# set -x

# delete old venv
cd test_project
rm -rf venv
cd ..
# installing a new one
bash init_test_project.sh
cd test_project
# getting introspect models from current repo
pip uninstall -y django-introspectmodels
ln -s ../introspectmodels
# launching test, coverage and linting
coverage run --source="./introspectmodels" manage.py test introspectmodels
flake8 --output-file=../flake8.txt introspectmodels
# getting output files
coverage xml
mv coverage.xml ../
coverage report  # for printing
# reinstall the introspectmodels package with pip
rm introspectmodels
pip install ../dist/django-introspectmodels-0.2.tar.gz
cd ..
