class TestStorage:
    # Хранилище для данных между тестами и фикстурами
    _ads = []

    @classmethod
    def add_ad(cls, token, ad_id):
        # Добавить объявление для удаления после теста
        cls._ads.append((token, ad_id))

    @classmethod
    def get_ads(cls):
        # Получить все объявления
        return cls._ads.copy()

    @classmethod
    def clear_ads(cls):
        # Очистить список объявлений
        cls._ads.clear()
