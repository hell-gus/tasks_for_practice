from tasks.task2.HashTable import HashTable

if __name__ == "__main__":
    # Создаем экземпляр ассоциативного массива
    aa = HashTable()

    # Добавляем элементы
    aa.insert("name", "Alice")
    aa.insert("age", 30)

    # Получаем значение по ключу
    print(aa.get("name"))  # Output: Alice

    # Проверяем наличие ключа
    print(aa.contains("age"))  # Output: True

    # Обновляем значение по ключу
    aa.update("age", 31)
    print(aa.get("age"))  # Output: 31

    # Удаляем элемент по ключу
    aa.remove("age")
    print(aa.contains("age"))  # Output: False

    # Выводим все элементы
    aa.display() # Output: name: Alice