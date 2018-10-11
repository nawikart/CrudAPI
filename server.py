import json
from flask import Response
from pprint import pprint

from flask import Flask, request
from db.data_layer import create_data, read_data, update_data, delete_data

app = Flask(__name__)

@app.route('/create-data-api/<table>/', methods=['POST'])
def create_data_api(table):
    result = create_data(table, request.form)

    if result != None:
        data = { 'status' : 'success' }
    else:
        data = { 'status' : 'error' }

    return Response(json.dumps(data), status=200, mimetype='application/json')


@app.route('/read-data-api/<table>/<id>', methods=['GET'])
def read_data_api(table, id):
    result = read_data(table, id)

    if result != None:
        data = { 'status' : 'success', 'data': result }
    else:
        data = { 'status' : 'error' }

    return Response(json.dumps(data), status=200, mimetype='application/json')


@app.route('/update-data-api/<table>', methods=['POST'])
def update_data_api(table):
    result = update_data(table, request.form['id'], request.form)

    if result != None:
        data = { 'status' : 'success' }
    else:
        data = { 'status' : 'error' }

    return Response(json.dumps(data), status=200, mimetype='application/json')    


@app.route('/delete-data-api/<table>', methods=['POST'])
def delete_data_api(table):
    result = delete_data(table, request.form['id'])

    if result:
        data = { 'status' : 'success' }
    else:
        data = { 'status' : 'error' }

    return Response(json.dumps(data), status=200, mimetype='application/json') 


app.run(debug=True)