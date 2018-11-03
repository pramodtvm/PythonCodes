

from flask import Flask ,jsonify,request
from flask_restful import Resource ,Api

app = Flask(__name__)
api = Api(app)

class helloworld(Resource):
    def get(self):
        return {'about':'Hellow World'}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json},201

class multi(Resource):
    def get(self,num):
        return {'result':num*10}

api.add_resource(helloworld, '/')
api.add_resource(multi,"/multi/<int:num>")

if __name__ == '__main__':
    app.run(debug=True)

