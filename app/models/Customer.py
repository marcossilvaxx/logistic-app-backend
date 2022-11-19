from app import db, ma
from marshmallow import fields

from app.models.Company import CompanySchema

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column('id', db.String(255), primary_key=True)
    login = db.Column('login', db.String(255), nullable=False)
    password = db.Column('password', db.String(255), nullable=False)
    name = db.Column('name', db.String(255), nullable=False)
    company_id = db.Column('company_id', db.ForeignKey("companies.id"))
    credit_cards = db.Column('credit_cards', db.String(255), nullable=True)
    
    company = db.relationship("Company", single_parent=True, backref=db.backref('customers', lazy='joined'))

    def __init__(self, id, login, password, name, company_id, credit_cards):
        if not(id and login and password and name):
            raise Exception('Missing parameters.')
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.company_id = company_id
        self.credit_cards = credit_cards

    def __repr__(self):
        return f'< Customer : {self.name} >'
    

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    company = fields.Nested(CompanySchema, many=False)
    class Meta:
        model = Customer

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)