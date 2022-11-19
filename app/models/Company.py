from app import db, ma

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False)

    def __init__(self, name):
        if not(name):
            raise Exception('Missing parameters.')
        self.name = name

    def __repr__(self):
        return f'< Company : {self.name} >'
    

class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)