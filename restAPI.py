# from flask import Flask
from flask_restful import Resource, Api, reqparse
from deviceAPI import readData
# from chatAPI import readMessage

# app = Flask(__name__)
# api = Api(app)

class restWeb(Resource):
    def get(self):
        return readData("deviceinfo.json","903810847"), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_arguement('name', require=True, type=str)
        parser.add_arguement('type', require=True, type=str)
        parser.add_arguement('unit', require=True, type=str)
        parser.add_arguement('data', require=True, type=list)
        args = parser.parse_args()
        return{
            'name': args['name'],
            'type': args['type'],
            'unit': args['unit'],
            'data': args['data']
        }, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_arguement('name', require=True, type=str)
        args =parser.parse_args()

        data = readData("deviceinfo.json", "903810847")

        if args['name'] in data['name']:
            data = data[data['name'] != str(args['name'])]
            return {"data": data}, 200
        else:
            return {
                "error": "device does not exist!"
            }, 404

        
# api.add_resource(restWeb, '/')

# if __name__ == '__main__':
#     app.run(debug=True)
