from .config import app

from datetime import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Model:
    def __init__(self, table):
        self.table = table

    def get_table_data(self):
        return db.session.query(self.table).all()

    def insert_table_data(self, data: dict):
        insert_data = self.table(**data)
        db.session.add(insert_data)
        db.session.commit()


class TimeStampedModel:
    created_at = db.Column(db.DateTime, default=dt.utcnow)


class Post(db.Model, TimeStampedModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
