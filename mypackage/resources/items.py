from flask_restful import Resource,reqparse
from mypackage.models.items import ItemModel

class ItemResource(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name',type=str,required=True)
    parser.add_argument('price',type=float,required=True)
    parser.add_argument('store_id',type=int,required=True)

    def post(self,name):
        data=ItemResource.parser.parse_args()
        if ItemModel.find_by_name(data['name']):
            return{"message":"Item already exist!"}

        item=ItemModel(**data)
        ItemModel.save(item)

        return{"Message":"Item created"}

    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404


            


