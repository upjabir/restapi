from flask_restful import Resource,reqparse
from mypackage.models.stores import StoreModel

class StoreResource(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name',type=str,required=True)

    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()

    def post(self,name):
        data=StoreResource.parser.parse_args()
        if StoreModel.find_by_name(name):
            return{"message":"Store already exist!"}

        store=StoreModel(**data)
        StoreModel.save_to_stores(store)

        return{"Message":"new Store created"}






class StoreList(Resource):

     def get(self):
        return {"stores":list(map(lambda x: x.json(), StoreModel.query.all()))}



