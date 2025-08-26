from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

manager = FlaskGroup(app)

if __name__ == "__main__":
    manager.run()