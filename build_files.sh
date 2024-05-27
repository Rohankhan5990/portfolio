#!/bin/bash
echo "BUILD START"

# Install system dependencies (if needed)
# Uncomment and modify the following lines if necessary
# apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev

# Update pip and install wheel to ensure we can install precompiled packages
python3 -m pip install --upgrade pip setuptools wheel

# Install Python dependencies
python3 -m pip install -r requirements.txt --verbose

# Collect static files
python3 manage.py collectstatic --noinput --clear --output staticfiles_build

echo "BUILD END"
