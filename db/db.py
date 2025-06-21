import sqlite3
import click
from flask import current_app, g

def init_app(app):
    app.teardown_appcontext(close_connection)
    app.cli.add_command(init_db_command)

# runs schema.sql script to repopulate database
def init_db(app):
    with current_app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# sets up CLI command 'init-db'
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# gets database connection
def get_db():
    db = getattr(g, '_database', None)
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# runs a db query
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return ([rv[0]] if rv else None) if one else rv

# execute sql command
def execute_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    cur.close()

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()