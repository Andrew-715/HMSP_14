import sqlite3

"""
Создаём функцию с SQL-запросом и выводим название, страну, год релиза, жанр
и описание фильма.
"""


def convert_tuple_to_list_of_dicts(result_all, keys):
    """
    С помощью циклов for добавляем необходимые значения к списку ключей
    и добавляем это в список result.
    """
    result = []

    for result_row in result_all:
        result.append({keys[i]: result_row[i] for i in range(len(keys))})

    return result


def search_by_name(movie_name):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """SELECT title, country, release_year, listed_in, description
                 FROM netflix
                 WHERE title LIKE :title
                 AND type = 'Movie'
                 LIMIT 1
        """

        # Выполняем запрос
        cursor.execute(query, {"title": movie_name})
        result_all = cursor.fetchall()

        # Прописываем список ключей, которые нам нужны.
        keys = ["title",  "country", "release_year", "listed_in", "description" ]

        # Превращаем кортежи в список словарей
        return convert_tuple_to_list_of_dicts(result_all, keys)[0]


"""
Создаём функцию с SQL-запросом и выводим только название и год выпуска.
"""


def search_by_release_year():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        querly = """
            SELECT title, release_year
            FROM netflix
            WHERE "type" = 'Movie'
            LIMIT 100
        """

        result_all = cursor.execute(querly)
        """
        Прописываем список ключей, которые нам нужны.
        """
        keys = [
            "title",
            "release_year"
        ]
        """
        Создаём пустой список, который будет в себе содержать ключи и значения.
        """
        result = []
        """
        С помощью циклов for добавляем необходимые значения к списку ключей
        и добавляем это в список result.
        """
        for result_row in result_all:
            result.append({keys[i]: result_row[i] for i in range(len(keys))})

        return result


"""
Создаём функцию с SQL-запросом и выводим название, рейтинг и описание фильма.
"""


def movies_rating():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        querly = """
            SELECT title, rating, description
            FROM netflix
            WHERE "type" = 'Movie'
            AND rating != ''
            AND rating IS NOT NULL
            ORDER BY rating
        """

        result_all = cursor.execute(querly)
        """
        Прописываем список ключей, которые нам нужны.
        """
        keys = [
            "title",
            "rating",
            "description"
        ]
        """
        Создаём пустой список, который будет в себе содержать ключи и значения.
        """
        result = []
        """
        С помощью циклов for добавляем необходимые значения к списку ключей
        и добавляем это в список result.
        """
        for result_row in result_all:
            result.append({keys[i]: result_row[i] for i in range(len(keys))})

        return result


"""
Cоздаём функцию для вывода данных о фильме по его названию.
"""


def title_dict(title):
    """
    :param title: здесь указываем название фильма
    :return: возвращаем данные фильма по названию
    """
    list_dict = search_by_name()
    """
    Создаём пустой словарь который будет содержать необходимые данные конкретного фильма.
    """
    result = {}
    """
    В цикле for проходимся по всем словарям в списке и добавляем в result по 1 словарю для
    сравнения названия (title) со значениями словаря.
    """
    for d in list_dict:
        result.update(d)
        if title in result.values():
            return result


"""
Создаём функцию для вывода списка фильмов по году выпуска.
"""


def title_years(year_1, year_2):
    """
    :param year_1: в этой переменной указываем С какого года будет поиск
    :param year_2: в этой переменной указываем ПО какой год будет поиск
    :return: возвращаем список словарей с названием и датой выхода фильма
    """
    list_dict = search_by_release_year()
    """
    Создаём пустой словарь который будет содержать необходимые данные конкретного фильма.
    """
    result = {}

    for d in list_dict:
        result.update(d)
        if year_1 or year_2 in result.values():
            return result



