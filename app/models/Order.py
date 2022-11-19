from app import db, ma
import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False)
    created_at = db.Column('created_at', db.DateTime, default=datetime.datetime.now)
    customer_id = db.Column('customer_id', db.ForeignKey("customers.id"))
    
    customer = db.relationship("Customer")

    def __init__(self, name, created_at):
        if not(name and created_at):
            raise Exception('Missing parameters.')
        self.name = name
        self.created_at = created_at

    def __repr__(self):
        return f'< Order : {self.name} >'
    

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)