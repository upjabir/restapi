from mypackage import db

class ItemModel(db.Model):
    __tablename__= 'items'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float())
    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"Item":self.name,"price":self.price}