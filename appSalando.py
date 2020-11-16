from databaseFolder import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #create a flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Cristina@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def main():
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == "__main__":
    main()