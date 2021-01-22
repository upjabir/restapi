from flask_restful import Resource,reqparse
from mypackage.models.user import UserModel

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True)
    parser.add_argument('password',type=str,required=True)

    def post(self):
        data=UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"User already exists"}, 400

        user=UserModel(**data)
        user.save_to_db()

        return {"message":"User created"} ,201



