from flask import Flask, jsonify

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return jsonify(companies)

if __name__ == '__main__':
    api.run()