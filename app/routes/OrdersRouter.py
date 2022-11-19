from app import app
from flask import jsonify, request
from ..controllers import OrdersController

@app.route('/orders', methods=['GET'])
def grt_all():
    response, httpCode = OrdersController.index(request)

    return jsonify(response), httpCode