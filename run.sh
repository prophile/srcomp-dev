#!/bin/bash
source venv/bin/activate
gunicorn --debug \
         --config conf.py \
         app:app

