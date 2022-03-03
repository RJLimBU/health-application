from flask import Flask
from flask_restful import Resource, Api, reqparse
from restAPI import restWeb
from chatAPI import readMessage

app = Flask(__name__)
api = Api(app)

api.add_resource(restWeb, '/')

if __name__ == '__main__':
    app.run(debug=True)
