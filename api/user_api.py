from api.base_api import BaseAPI
from constants import Endpoint


class User(BaseAPI):

    @staticmethod
    def create_user(payload):
        return User()._post(Endpoint.USER_CREATE, json=payload)

    @staticmethod
    def login(payload):
        return User()._post(Endpoint.LOGIN, json=payload)
