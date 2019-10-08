#!/bin/bash

# Comments above lines are for the Windows platform.
# Uncommented lines are generally for Debian Linux, and other flavors of Linux as well.

pip install django

# django-admin.exe startproject djtests
django-admin startproject djtests

cd djtests

#python -m venv --copies venv
python3 -m venv --copies venv

#./venv/Scripts/activate
./venv/bin/activate

python -m pip install --upgrade pip
pip install djangorestframework
pip install markdown
pip install django-filter

# python manage.py check
./manage.py check
./manage.py makemigrations
./manage.py migrate
./manage.py runserver

# Create requirements.txt.
# pip freeze > requirements.txt
# Each time you run pip install, you add a package to the virtual environment.
# If you don't use a package it will still be added to requirements.txt using pip freeze.
# It is recommended to uninstall unused packages.
# pip uninstall *

# Install via requirements.txt
# pip install -r requirements.txt
