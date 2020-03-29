#!/bin/bash
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
sudo pip install -r requirements.txt
deactivate