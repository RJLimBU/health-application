from flask import Flask
from flask_restful import Resource, Api
from deviceAPI import readData

app = Flask(__name__)
api = Api(app)

class ReadData(Resource):
    def get(self):
        return readData("deviceinfo.json","903810847")

api.add_resource(ReadData, '/')

if __name__ == '__main__':
    app.run(debug=True)