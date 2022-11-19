from app import app
from flask import jsonify, request
from ..controllers import OrdersController

@app.route('/orders', methods=['GET'])
def list():
    response, httpCode = OrdersController.list(request)

    return jsonify(response), httpCode