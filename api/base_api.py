import requests

from constants import Url


class BaseAPI:
    # Базовый класс для API клиентов. Хранит базовый URL и общую логику запросов.

    def __init__(self, base_url=Url.BASE_URL):
        self.base_url = base_url

    def _post(self, path, data=None, json=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.post(url, data=data, json=json, headers=headers)

    def _patch(self, path, data=None, json=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.patch(url, data=data, json=json, headers=headers)

    def _get(self, path, params=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.get(url, params=params, headers=headers)

    def _delete(self, path, headers=None):
        url = f"{self.base_url}{path}"
        return requests.delete(url, headers=headers)
