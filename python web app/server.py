from flask import Flask,jsonify,request
import mysql.connector
import products
import orders
import json
from sql_connection import get_sql_connection

app= Flask(__name__)
connection= get_sql_connection()
@app.route("/getproduct",methods=["GET"])
def get_products():
    product=products.get_all_results(connection)
    response=jsonify(product)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products.add_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products.del_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":

    app.run(debug=True)