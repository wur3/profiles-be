import os
from flask import Flask, make_response, request
from uuid import uuid4
from db.db import init_app, query_db, execute_db
import json

FIRST_NAME_KEY='firstName'
LAST_NAME_KEY='lastName'
AGE_KEY='age'

def create_app(config_filename = None):
    app = Flask(__name__)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    app.config["DATABASE"] = current_dir + '/db/database.db'
    init_app(app)

    # runs a db query, returns result as json
    def query_db_to_json(query, args=(), one=False):
        r = query_db(query, args, one)
        return json.dumps( [dict(ix) for ix in r] )

    @app.get("/profiles")
    def get_all_profiles():
        all_profiles = query_db_to_json('SELECT * FROM profile')
        return make_response(all_profiles, 200)
        
    @app.get("/profile/<id>")
    def get_profile_by_id(id):
        profile = query_db_to_json('SELECT * FROM profile WHERE id = ?', [id], one = True)
        return make_response(profile, 200)

    @app.post("/profile")
    def add_profile_by_id():
        rb = request.json
        args = [str(uuid4()), str(rb[FIRST_NAME_KEY]), str(rb[LAST_NAME_KEY]), str(rb[AGE_KEY])]
        execute_db('INSERT INTO profile (id, first_name, last_name, age) VALUES (?, ?, ?, ?)', 
                        args)
        return make_response("Successfully inserted", 200)

    @app.put("/profile/<id>")
    def edit_profile_with_id(id):
        rb = request.json
        args = [rb[FIRST_NAME_KEY], rb[LAST_NAME_KEY], rb[AGE_KEY], id] 
        execute_db('UPDATE profile SET first_name = ?, last_name = ?, age = ? WHERE id = ?', 
                        args)
        return make_response("Successfully updated", 200)

    @app.delete("/profile/<id>")
    def delete_profile_with_id(id):
        execute_db('DELETE FROM profile WHERE id = ?', [id])
        return make_response("Successfully deleted", 200)

    return app

create_app()