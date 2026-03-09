from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from extensions import db

class Notice(db.Model):
    __tablename__ = "notices"

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    issued_by=db.Column(db.String(20),nullable=False)
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)