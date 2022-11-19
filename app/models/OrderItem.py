from app import db, ma
from marshmallow import fields

from app.models.Delivery import DeliverySchema

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    product = db.Column('product', db.String(255), nullable=False)
    price_per_unit = db.Column('price_per_unit', db.Float, nullable=True)
    quantity = db.Column('quantity', db.Integer, nullable=False)
    order_id = db.Column('order_id', db.ForeignKey("orders.id"))
    
    deliveries = db.relationship("Delivery", single_parent=True, backref=db.backref('order_items', lazy='joined'))


    def __init__(self, product, price_per_unit, quantity):
        if not(product and quantity):
            raise Exception('Missing parameters.')
        self.product = product
        self.price_per_unit = price_per_unit
        self.quantity = quantity

    def __repr__(self):
        return f'< OrderItem : {self.product} >'
    

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    deliveries = fields.Nested(DeliverySchema, many=True)
    class Meta:
        model = OrderItem

order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)