from .config import app

from datetime import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.utcnow)
