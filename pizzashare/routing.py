from pizzashare.resources import UserResource


def route(api):
    api.add_resource(UserResource, '/user')
