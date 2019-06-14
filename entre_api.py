#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)


### Connector to data base (I think this function can be reused even for kafka !)

''' 
def insert_2_database(file):
    DATABASE = '/var/www/FlaskApp/FlaskApp/weather.db'
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO weather_readings (windspeed) VALUES (?)", (windspeed))
        con.commit()

def insert_2_kafka(file):
    DATABASE = '/var/www/FlaskApp/FlaskApp/weather.db'
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO weather_readings (windspeed) VALUES (?)", (windspeed))
        con.commit()        
'''


files = [] 

### insert a string of data, fetch it to a database and to kafka... and return 201 if it succeed.
@app.route('/IKIM/api/v1.0/files', methods=['POST'])
def create_task():
    if not request.json:               
        abort(400)

    
    if len(files) == 0:
        id_number  = 0
    else:    
        id_number = files[-1]['id'] + 1  

    file = {
        'id': id_number,
        'filename': request.json['filename'],
        'data': request.json.get('data', "")
    }
    files.append(file)

    return jsonify({'file': file}), 201


### get the data of <int:file_id> 
'''
@app.route('/IKIM/api/v1.0/files/<int:file_id>', methods=['GET'])
def get_task(file_id):
    file = [file for file in files if file['id'] == file_id]
    if len(file) == 0:
        abort(404)
    return jsonify({'file': file[0]})
'''


### catch error is method unknown
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

