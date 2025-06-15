#!/usr/bin/env bash
# Set Python version explicitly
pyenv install -s 3.10.12
pyenv global 3.10.12

# Create a virtual environment using correct Python version
python -m venv venv
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt
