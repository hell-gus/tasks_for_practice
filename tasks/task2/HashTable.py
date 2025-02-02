class HashTable:
    """Класс, реализующий ассоциативный массив (словарь)."""

    def __init__(self):
        """Инициализация пустого словаря."""
        self.data = {}

    def insert(self, key, value):
        """
        Добавляет пару ключ-значение в ассоциативный массив.

        :param key: Ключ для добавления.
        :param value: Значение, связанное с ключом.
        """
        self.data[key] = value

    def get(self, key):
        """
        Возвращает значение по ключу.

        :param key: Ключ для поиска.
        :return: Значение, связанное с ключом, или None, если ключ отсутствует.
        """
        return self.data.get(key, None)

    def remove(self, key):
        """
        Удаляет пару ключ-значение по ключу.

        :param key: Ключ для удаления.
        :raises KeyError: Если ключ отсутствует в массиве.
        """
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"Key '{key}' not found")

    def contains(self, key):
        """
        Проверяет наличие ключа в массиве.

        :param key: Ключ для проверки.
        :return: True, если ключ существует, иначе False.
        """
        return key in self.data

    def update(self, key, value):
        """
        Обновляет значение по ключу.

        :param key: Ключ для обновления.
        :param value: Новое значение.
        :raises KeyError: Если ключ отсутствует в массиве.
        """
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError(f"Key '{key}' not found")

    def display(self):
        """Выводит все пары ключ-значение в массиве."""
        for key, value in self.data.items():
            print(f"{key}: {value}")