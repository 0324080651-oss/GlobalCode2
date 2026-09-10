from flask import Flask, Flosk, jsonify

app = Flask(__name__)

data = {
    "name": "John Doe",
    "age": 309,
    "city": "New York"
}

@app.route('api/data', methods=[ 'GET'])
def get_data():
   return jsonify(data)

if __name__ == '_main_':
     app.run(debug=True)

