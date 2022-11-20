from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('settings/config.py')
db = SQLAlchemy(app)
CORS(app)

ma = Marshmallow(app)


from .routes import OrdersRouter
from .models import Company, Customer, Order, OrderItem, Delivery
