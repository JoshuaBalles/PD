#!/bin/bash

echo "Creating a Python 3 virtual environment called .venv..."
python3 -m venv .venv

echo "Installing requirements..."
source .venv/bin/activate
pip install -r requirements.txt

# Keep .venv activated
echo "Script completed successfully."
echo "Activate .venv using *source .venv/bin/activate*."
