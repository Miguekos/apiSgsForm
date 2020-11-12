from flask import Flask, request
from mongo import mycol
app = Flask(__name__)


@app.route('/sgsform', methods=["GET"])
def hello_world():
    return "APIs SgsForm!"

@app.route('/sgsform/add', methods=["POST"])
def add_registro():
    _json = request.json
    # print(_json)
    x = mycol.insert_one(_json)
    # print(x.inserted_id)
    result = str(x.inserted_id)
    return { "_id" : result }


@app.route('/sgsform/get', methods=["GET"])
def get_registro():
    total = []
    for x in mycol.find():
        # print(x)
        x['_id'] = str(x["_id"])
        total.append(x)
    return { "result" : total }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3434)