#A model class, also referred to simply as a model, is a Python class that (1) defines a new Python data type, and (2) defines database metadata to describe an SQL table. We can treat a model class like any other Python class, meaning we can create instances, invoke methods, etc. Additionally, Flask-SQLAlchemy performs object-relational mapping between the model class and an associated database table, while Flask-Migrate uses changes to the model class to evolve a database schema.

#Defining a model with Flask-SQLAlchemy requires a Python class with four key traits:
    #Inheritance from the db.Model class.
    #A __tablename__ class attribute.
    #One or more class attributes assigned to the type db.Column.
    #One class attribute specified to be the table's primary key.

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
