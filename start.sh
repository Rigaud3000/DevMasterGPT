#!/bin/bash
cd client
npm install
npm run build
cd ..
pip install -r server/requirements.txt
python server/app.py
