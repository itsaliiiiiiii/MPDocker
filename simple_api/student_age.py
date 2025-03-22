#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
import json
import os

auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True

# Authentication setup
@auth.get_password
def get_password(username):
    if username == 'root':
        return 'root'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

# Load student age data
student_age_file_path = os.getenv('STUDENT_AGE_FILE', '/data/student_age.json')

try:
    with open(student_age_file_path, "r") as file:
        student_age = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    student_age = {}

@app.route('/supmit/api/v1.0/get_student_ages', methods=['GET'])
@auth.login_required
def get_student_ages():
    return jsonify({'student_ages': student_age})

@app.route('/supmit/api/v1.0/get_student_ages/<student_name>', methods=['GET'])
@auth.login_required
def get_student_age(student_name):
    if student_name not in student_age:
        abort(404, description="Student not found")
    
    return jsonify({student_name: student_age[student_name]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
