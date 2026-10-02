# Sprint 10.1 — API-тесты QA Desk

Автотесты для REST API сервиса [QA Desk](https://qa-desk.education-services.ru).  
Проект покрывает регистрацию пользователей, авторизацию и работу с объявлениями.

## Стек

| Инструмент | Назначение |
|---|---|
| **Python 3** | Язык проекта |
| **pytest** | Запуск и организация тестов |
| **requests** | HTTP-запросы к API |
| **pydantic** | Валидация моделей запросов и ответов |
| **Faker** | Генерация тестовых данных |
| **Allure** | Отчёты о прогоне тестов |

## Структура проекта

```
Sprint_10.1/
├── api/
│   ├── base_api.py      # Базовый HTTP-клиент
│   ├── user_api.py      # Регистрация и авторизация (User)
│   └── ad_api.py        # CRUD объявлений (Ad)
├── tests/
│   ├── test_registration.py   # Тесты регистрации
│   ├── test_auth.py           # Тесты авторизации
│   └── test_ad.py             # Тесты объявлений
├── conftest.py          # Фикстуры pytest и очистка данных
├── constants.py         # URL и эндпоинты API
├── models.py            # Pydantic-модели
├── test_data.py         # Тестовый пользователь (TestData)
├── helpers.py           # Генератор данных (UsedDataGenerator)
├── storage.py           # Хранилище объявлений для teardown
├── requirements.txt
└── pytest.ini
```

## Покрытие тестами

| Модуль | Сценарии |
|---|---|
| **Регистрация** | Успешная регистрация, повторная регистрация с тем же email |
| **Авторизация** | Успешный вход существующего пользователя |
| **Объявления** | Создание, удаление, запрет редактирования чужого объявления |

## Быстрый старт

### 1. Клонировать репозиторий и перейти в папку проекта

```bash
cd Sprint_10.1
```

### 2. Создать и активировать виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

## Запуск тестов

### Все тесты

```bash
pytest
```

### Конкретный файл или тест

```bash
pytest tests/test_auth.py
pytest tests/test_ad.py::TestPositiveCreateAd::test_create_ad_success
```

### Подробный вывод

```bash
pytest -v
```

### С генерацией Allure-отчёта

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

> Для `allure serve` нужен установленный [Allure CLI](https://allurereport.org/docs/install/).

## Фикстуры

| Фикстура | Описание |
|---|---|
| `auth_token` | Токен авторизованного пользователя из `TestData` |
| `created_user` | Новый зарегистрированный пользователь с токеном |
| `cleanup_after_test` | Автоочистка созданных объявлений после каждого теста |

## Тестовые данные

Учётные данные существующего пользователя задаются в `test_data.py`:

```python
class TestData:
    EMAIL = "test666@mail.ru"
    PASSWORD = "test666"
```

Для уникальных пользователей в тестах используется `UsedDataGenerator` из `helpers.py`.

## API

Базовый URL: `https://qa-desk.education-services.ru`

| Метод | Эндпоинт | Описание |
|---|---|---|
| `POST` | `/api/signup` | Регистрация |
| `POST` | `/api/signin` | Авторизация |
| `POST` | `/api/create-listing` | Создание объявления |
| `PATCH` | `/api/update-offer/{id}` | Редактирование объявления |
| `DELETE` | `/api/listings/{id}` | Удаление объявления |
