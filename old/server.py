from flask import Flask
from flask_restplus import Api, Resource
from flask import jsonify


# Create the application instanice we used flask in lab0 lets stay true to that # we will introduce connexion later and discuss differences. 

#app = connexion.App(__name__, specification_dir="./")

flask_app = Flask(__name__)

app = Api(app = flask_app)

name_space = app.namespace('engr-222', description='Main APIs')

# Read the yaml file to configure the endpoints this portion will be introduced # next week
#app.add_api("cpu.yaml")

# create a URL route in our application for "/"
@name_space.route("/engr-222")
class main(Resource):
    def home():
        msg = {"msg": "It's working!"}
        return jsonify(msg)

    def get(self):
        msg ={"status": "Got data!"}
        return jsonify(msg)

    def post(self):
        msg = {"status": " Posted data"}
        return jsonify(msg)

@name_space.route('/engr-222/api/sum/<arg1>/<arg2>')
class math1(Resource):
    def sum(arg1,arg2):
        arg1 = float(arg1)
        arg2 = float(arg2)
        out = arg1 + arg2
        return str(out)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=8080, debug=True)
