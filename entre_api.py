#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)


files = [] 


@app.route('/IKIM/api/v1.0/files', methods=['POST'])
def create_task():
    if not request.json:                ### or not 'filename' in request.json:
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

@app.route('/IKIM/api/v1.0/files/<int:file_id>', methods=['GET'])
def get_task(file_id):
    file = [file for file in files if file['id'] == file_id]
    if len(file) == 0:
        abort(404)
    return jsonify({'file': file[0]})


@app.route('/IKIM/api/v1.0/files/<int:file_id>', methods=['DELETE'])
def delete_task(file_id):
    file = [file for file in files if file['id'] == file_id]
    if len(file) == 0:
        abort(404)
    files.remove(file[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

