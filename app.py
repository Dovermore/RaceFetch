# scaffolding code from https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mydbs import Race


app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

engine = create_engine('sqlite:///foo.db', echo=True)
Session = sessionmaker(bind=engine)


@api.resource("/")
class Inex(Resource):
    def get(self):
        return r"<h1>This is the index page.</h1>"


@api.resource("/race/all")
class AllRace(Resource):
    def get(self):
        with Session() as sess:
            results = []
            for race in sess.query(Race).order_by(Race.rstart):
                results.append({race.id: {
                    "type": race.rtype,
                    "number": race.rnumber,
                    "name": race.rname,
                    "start": race.rstart
                }})
        return jsonify(results)


app.run()
