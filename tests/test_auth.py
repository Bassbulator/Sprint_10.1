import allure

from api.user_api import User
from models import AuthResponse, UserAuth
from test_data import TestData


class TestPositiveUserAuthorization:

    @allure.title("Успешная авторизация ранее зарегистрированного пользователя")
    def test_user_authorization_success(self):
        with allure.step(
            "Подготовить данные существующего пользователя из test_data.py"
        ):
            payload = UserAuth(email=TestData.EMAIL, password=TestData.PASSWORD)

        with allure.step("Отправить запрос на авторизацию"):
            response = User.login(payload.model_dump())

        with allure.step("Преобразовать ответ в модель AuthResponse"):
            auth_data = AuthResponse(**response.json())

        with allure.step("Проверить статус-код ответа"):
            assert response.status_code == 201

        with allure.step("Проверить email авторизованного пользователя"):
            assert auth_data.user.email == TestData.EMAIL

        with allure.step("Проверить, что access token не пустой"):
            assert auth_data.token.access_token
