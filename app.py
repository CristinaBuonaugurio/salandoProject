from databaseFolder import models
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__) #create a flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Cristina@localhost:5432/salando'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

models.db.init_app(app)
migrate = Migrate(app, models.db)