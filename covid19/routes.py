from flask import jsonify
from covid19 import app
import requests
import csv
import json

#Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return convert_write_json(csv_rows, json_file)

#Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        return json.dumps(data)

@app.route('/hello', methods=['GET'])
def hello():
    url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
    response = requests.get(url)
    with open("covid_data.csv", 'wb') as f:
        f.write(response.content)
    file = 'covid_data.csv'
    json_file = 'output_covid_data.json'
    return jsonify(read_CSV(file, json_file))