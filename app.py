from databaseFolder import models, functionModels
from flask import Flask, jsonify
from flask_migrate import Migrate
from ml import tf_idf as t
from datetime import datetime
app = Flask(__name__) #create a flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Cristina@localhost:5432/salando'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

models.db.init_app(app)
migrate = Migrate(app, models.db)

@app.route('/')
def main_page():
    return t.method()

@app.route('/products', methods = ['GET'])
def products():
    return functionModels.getAllProducts('route')

@app.route('/categories', methods = ['GET'])
def categories():
    return functionModels.getCategories('route')

@app.route('/products/<id_category>', methods = ['GET'])
def getProductByCategory(id_category):
    return functionModels.getProductsByCategory(id_category,'route')
    