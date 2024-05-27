#!/bin/bash
echo "BUILD START"
# Install Python dependencies
python3 -m pip install -r requirements.txt --verbose
python3 manage.py collectstatic --noinput --clear 

echo "BUILD END"
