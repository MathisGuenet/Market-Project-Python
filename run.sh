#!/bin/bash
echo "Creating the virtual environment..."
python3 -m venv .venv
. .venv/bin/activate
pip3 install --no-cache-dir -r requirements.txt
echo "Creation done."
echo "Run python script..."
python3 main.py
