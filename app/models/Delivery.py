from app import db, ma

class Delivery(db.Model):
    __tablename__ = 'deliveries'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    delivered_quantity = db.Column('delivered_quantity', db.Integer, nullable=False)
    order_item_id = db.Column('order_item_id', db.ForeignKey("order_items.id"))
    
    order_item = db.relationship("OrderItem")

    def __init__(self, delivered_quantity):
        if not(delivered_quantity):
            raise Exception('Missing parameters.')
        self.delivered_quantity = delivered_quantity

    def __repr__(self):
        return f'< Delivery : {self.id} >'
    

class DeliverySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Delivery

delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)