from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from mongo import mycol
from woocomerce import wcapi

app = Flask(__name__)


@app.route('/sgsform', methods=["GET"])
def hello_world():
    return "APIs SgsForm!"


@app.route('/sgsform/add', methods=["POST"])
def add_registro():
    _json = request.json
    print(_json)
    x = mycol.insert_one(_json)
    # print(x.inserted_id)
    result = str(x.inserted_id)
    return {"_id": result}


@app.route('/sgsform/get', methods=["GET"])
def get_registro():
    total = []
    for x in mycol.find():
        # print(x)
        x['_id'] = str(x["_id"])
        total.append(x)
    return {"result": total}


@app.route('/sgsform/ordenes/<limit>', methods=['GET'])
def woocommerce_ordenes(limit):
    # asd = wcapi.options("orders").json()
    # asd = wcapi.get("search").json()
    ordenes = wcapi.get("orders", params={"per_page": limit}).json()
    print(ordenes)
    print(len(ordenes))
    print(type(ordenes))
    return jsonify(ordenes)
    # return "{}".format(asd)


@app.route('/sgsform/ordenes/id/<id>', methods=['GET'])
def woocommerce_orden_id(id):
    asd = wcapi.get("orders/{}".format(id)).json()
    return jsonify(asd)


@app.route('/sgsform/customers/<limit>', methods=['GET'])
def woocommerce_customers(limit):
    # asd = wcapi.options("orders").json()
    # asd = wcapi.get("search").json()
    ordenes = wcapi.get("customers", params={"per_page": limit}).json()
    print(ordenes)
    print(len(ordenes))
    print(type(ordenes))
    return jsonify(ordenes)
    # return "{}".format(asd)


@app.route('/sgsform/customers/id/<id>', methods=['GET'])
def woocommerce_customers_id(id):
    asd = wcapi.get("customers/{}".format(id), params={"per_page": 100}).json()
    return jsonify(asd)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3434)
