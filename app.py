from flask import Flask, make_response, request

from db.db import init_app, query_db

FIRST_NAME_KEY='firstName'
LAST_NAME_KEY='lastName'
AGE_KEY='age'

app = Flask(__name__)
init_app(app)

@app.get("/profiles")
def get_all_profiles():
    all_profiles = query_db('SELECT * FROM profile')
    return make_response(all_profiles, 200)
    
@app.get("/profile/<int:id>")
def get_profile_by_id(id):
    profile = query_db('SELECT * FROM profile WHERE id = ?', [id], one = True)
    return make_response(profile, 200)

@app.post("/profile/<int:id>")
def add_profile_by_id(id):
    rb = request.form
    args = [id, rb[FIRST_NAME_KEY], rb[LAST_NAME_KEY], rb[AGE_KEY]]
    insert = query_db('INSERT INTO profile (id, first_name, last_name, age) VALUES (?, ?, ?, ?)', 
                      args, one = True)
    return make_response(insert, 200)

@app.put("/profile/<int:id>")
def edit_profile_with_id(id):
    rb = request.form
    args = [rb[FIRST_NAME_KEY], rb[LAST_NAME_KEY], rb[AGE_KEY], id] 
    update = query_db('UPDATE profile SET first_name = ?, last_name = ?, age = ? WHERE id = ?', 
                      args, one = True)
    return make_response(update, 200)

@app.delete("/profile/<int:id>")
def delete_profile_with_id(id):
    remove = query_db('DELETE FROM profile WHERE id = ?', [id], one = True)
    return make_response(remove, 200)
