from sqlalchemy.orm import exc
from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with, fields
from pizzashare import db
from pizzashare.models import User

parser = reqparse.RequestParser()
parser.add_argument('uuid', type=str, help='uuid=device UUID', required=True)
parser.add_argument('name', type=str, help='name=name of user')

user_fields = {
    'uuid': fields.String,
    'name': fields.String,
}


class UserResource(restful.Resource):
    @marshal_with(user_fields)
    def get(self):
        args = parser.parse_args()
        uuid = args['uuid']
        if not uuid:
            return None

        session = db.Session()
        query = session.query(User).filter(User.uuid == uuid)
        try:
            return query.one()
        except exc.NoResultFound:
            return None

    @marshal_with(user_fields)
    def put(self):
        args = parser.parse_args()
        uuid, name = args['uuid'], args['name']
        if not all([uuid, name]):
            return None

        session = db.Session()
        user = User(uuid=uuid, name=name)
        user = session.merge(user)
        session.commit()

        return user
