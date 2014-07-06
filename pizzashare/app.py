from flask import Flask
from flask.ext import restful
from pizzashare import routing

app = Flask(__name__)
api = restful.Api(app)

routing.route(api)

if __name__ == '__main__':
    app.run(debug=True)
