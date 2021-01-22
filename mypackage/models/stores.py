from mypackage import db

class StoreModel(db.Model):
    __tablename__= 'stores'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    #one_to_many
    items=db.relationship('ItemModel',backref='stores',lazy='dynamic')


    def __init__(self,name):
        self.name=name

    def json(self):
        return {"stores":self.name,"items":list(map(lambda x: x.json(), self.items.all()))}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_stores(self):
        db.session.add(self)
        db.session.commit()

    


