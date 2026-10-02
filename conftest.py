import pytest
from test_data import TestData
from api.ad_api import Ad
from api.user_api import User
from helpers import UsedDataGenerator
from storage import TestStorage
from models import UserAuth, AuthResponse, RegistrationUser, RegistrationResponse


@pytest.fixture(autouse=True, scope="function")
def cleanup_after_test():
    # Очистка после каждого теста
    yield

    for token, ad_id in TestStorage.get_ads():
        try:
            Ad.delete_ad(token, ad_id)
        except Exception as e:
            print(f"Не удалось удалить объявление {ad_id}: {e}")
    TestStorage.clear_ads()


@pytest.fixture
def auth_token():
    # Возвращает токен пользователя
    login_payload = UserAuth(email=TestData.EMAIL, password=TestData.PASSWORD)

    login_response = User.login(login_payload.model_dump())

    if login_response.status_code != 201:
        raise AssertionError(
            f"Не удалось получить токен. Статус: {login_response.status_code}, тело: {login_response.text}"
        )

    auth_data = AuthResponse(**login_response.json())
    return auth_data.token.access_token


@pytest.fixture(scope="function")
def created_user():
    # Создает нового пользователя и возвращает его данные
    user_data = UsedDataGenerator.gen_user()
    payload = RegistrationUser(**user_data)

    response = User.create_user(payload.model_dump())

    registration_data = RegistrationResponse(**response.json())
    token = registration_data.access_token.access_token

    return {
        "token": token,
        "email": payload.email,
        "password": payload.password,
        "submitPassword": payload.submitPassword,
        "name": registration_data.user.name,
        "response": response,
    }