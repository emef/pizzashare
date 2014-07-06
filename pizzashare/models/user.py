from sqlalchemy import Column, String
from pizzashare import db


class User(db.Base):
    __tablename__ = 'users'

    uuid = Column(String(36), primary_key=True)
    name = Column(String(100))

    def __str__(self):
        return '<User: %s>' % self.name

    def __repr__(self):
        return "<User(uuid='%s', name='%s')>" % (
            self.uuid, self.name)
