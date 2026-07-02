from requests_toolbelt.multipart.encoder import MultipartEncoder

from api.base_api import BaseAPI
from constants import Endpoint


class Ad(BaseAPI):

    CREATE_FIELDS = ("name", "category", "condition", "city", "description", "price")

    @staticmethod
    def _auth_headers(token, content_type=None):
        headers = {"Authorization": f"Bearer {token}"}
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def _send_multipart(self, method, path, token, fields, image_path=None):
        if image_path:
            with open(image_path, "rb") as image_file:
                multipart_data = MultipartEncoder(
                    fields={**fields, "images": ("image.jpg", image_file, "image/jpeg")}
                )
                headers = self._auth_headers(token, multipart_data.content_type)
                request = self._post if method == "post" else self._patch
                return request(path, data=multipart_data, headers=headers)

        multipart_data = MultipartEncoder(fields=fields)
        headers = self._auth_headers(token, multipart_data.content_type)
        request = self._post if method == "post" else self._patch
        return request(path, data=multipart_data, headers=headers)

    @staticmethod
    def create_ad(token, payload, image_path=None):
        fields = {key: str(payload[key]) for key in Ad.CREATE_FIELDS}
        return Ad()._send_multipart(
            "post", Endpoint.CREATE_OFFER, token, fields, image_path
        )

    @staticmethod
    def change_data_ad(token, payload, ad_id, image_path=None):
        fields = {
            key: str(value) for key, value in payload.items() if value is not None
        }
        return Ad()._send_multipart(
            "patch", f"{Endpoint.PATCH_OFFER}/{ad_id}", token, fields, image_path
        )

    @staticmethod
    def delete_ad(token, ad_id):
        client = Ad()
        headers = client._auth_headers(token)
        return client._delete(f"{Endpoint.DELETE_OFFER}/{ad_id}", headers=headers)
