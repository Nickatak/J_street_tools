import csv

from flask import Flask, jsonify, redirect, render_template, request

import validations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/', methods=['POST'])
def process():
    json_response = {}
    raw_data = request.get_data().decode('utf-8')

    # I feel like I should be wary of a potential error, but I couldn't get one to trigger, even with a completely invalid CSV.
    reader = csv.reader(raw_data.split('\n'), delimiter=',')
    parsed_data = [row for row in reader if row]

    try:
        validations.ValidateCSV(parsed_data)

        output = []
        for row in parsed_data:
            sf_key = row[1]
            college_name = row[0]

            output.append("{}={}".format(sf_key, college_name))

        json_response['data'] = '\n'.join(output)
    except validations.CSVValidationError as e:
        json_response['error'] = str(e)

    return jsonify(json_response)


if __name__ == '__main__':
    app.run(debug=True)