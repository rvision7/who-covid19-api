[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# who-covid19-api
Python REST API for WHO covid19 data

## Implementation details
WHO official covid19 data table (csv) is parsed and provided as REST api

## Project structure
```
who-covid19-api/
├── LICENSE
├── README.md
├── covid19
│   ├── __init__.py
│   └── routes.py
├── main.py
└── requirements.txt
```
- covid19 package holds the model and controller layer.
- main.py is the entry point for running the application.

## Running the application
Execute the below commands from the root of the project directory. 
```
 python3 -m venv venv
 ./venv/bin/pip3 install -r requirements.txt
 ./venv/bin/python3 main.py 
 
```
