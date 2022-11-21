import sqlite3


"""
Создаём функцию для превращения кортежи в список словарей.
"""


def convert_tuple_to_list_of_dicts(result_all, keys):
    result = []

    """
    С помощью циклов for добавляем необходимые значения к списку ключей
    и добавляем это в список result.
    """

    for result_row in result_all:
        result.append({keys[i]: result_row[i] for i in range(len(keys))})

    return result


"""
Создаём функцию с SQL-запросом и выводим название, страну, год релиза, жанр
и описание фильма.
"""


def search_by_name(movie_name):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """SELECT title, country, release_year, listed_in, description
                 FROM netflix
                 WHERE title LIKE :title
                 AND country !=''
                 LIMIT 1
        """

        # Выполняем запрос
        cursor.execute(query, {"title": movie_name})
        result_all = cursor.fetchall()

        # Прописываем список ключей, которые нам нужны.
        keys = ["title", "country", "release_year", "listed_in", "description"]

        # Превращаем кортежи в список словарей
        return convert_tuple_to_list_of_dicts(result_all, keys)[0]


"""
Создаём функцию с SQL-запросом и выводим только название и год выпуска.
"""


def search_by_release_year(old_year, new_year):

    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = """
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN @old_year AND @new_year
                LIMIT 100
                """

        cursor.execute(query, (old_year, new_year))
        sql_result = cursor.fetchall()

        """
        Создаём пустой список, который будет содержать в себе словари.
        """

        sql_year_dict = []

        """
        С помощью циклов for задаём и добавляем необходимые значения к списку ключей
        и добавляем это в список sql_year_dict.
        """

        for i in sql_result:
            title = i["title"]
            release_year = i["release_year"]

            sql_year_dict.append(
                {
                    "title": title,
                    "release_year": release_year
                }
            )

    return sql_year_dict


"""
Создаём функцию детского рейтинга с SQL-запросом и выводим название, рейтинг и описание фильма.
"""


def movie_rating_children():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
            SELECT title, rating, description
            FROM netflix
            WHERE "type" = 'Movie'
            AND rating = 'G'
            ORDER BY rating
        """

        cursor.execute(query)
        result_all = cursor.fetchall()

        """
        Создаём пустой список, который будет содержать в себе словари.
        """

        result = []

        """
        С помощью циклов for добавляем необходимые значения к списку ключей
        и добавляем это в список result.
        """

        for row in result_all:
            rating = {
                'title': row[0],
                'rating': row[1],
                'description': row[2]
            }
            result.append(rating)

        return result


"""
Создаём функцию семейного рейтинга с SQL-запросом и выводим название, рейтинг и описание фильма.
"""


def movie_rating_family():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
            SELECT title, rating, description
            FROM netflix
            WHERE "type" = 'Movie'
            AND rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
            ORDER BY rating
        """

        cursor.execute(query)
        result_all = cursor.fetchall()

        """
        Создаём пустой список, который будет содержать в себе словари.
        """

        result = []

        """
        С помощью циклов for добавляем необходимые значения к списку ключей
        и добавляем это в список result.
        """

        for row in result_all:
            rating = {
                'title': row[0],
                'rating': row[1],
                'description': row[2]
            }
            result.append(rating)

        return result


"""
Создаём функцию взрослого рейтинга с SQL-запросом и выводим название, рейтинг и описание фильма.
"""


def movie_rating_adult():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = """
            SELECT title, rating, description
            FROM netflix
            WHERE "type" = 'Movie'
            AND rating = 'R' OR rating = 'NC-17'
            ORDER BY rating
        """

        cursor.execute(query)
        result_all = cursor.fetchall()

        """
        Создаём пустой список, который будет содержать в себе словари.
        """

        result = []

        """
        С помощью циклов for добавляем необходимые значения к списку ключей
        и добавляем это в список result.
        """

        for row in result_all:
            rating = {
                'title': row[0],
                'rating': row[1],
                'description': row[2]
            }
            result.append(rating)

        return result


"""
Создаём функцию поиска по жанрам с SQL-запросом и выводим название и описание фильма.
"""


def title_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            AND "type" = 'Movie'
            ORDER BY release_year DESC
            LIMIT 10
            """

        cursor.execute(query)
        result_all = cursor.fetchall()

        """
        Создаём пустой список, который будет содержать в себе словари.
        """

        result = []

        """
        С помощью циклов for добавляем необходимые значения к списку ключей
        и добавляем это в список result.
        """

        for row in result_all:
            listed_in = {
                'title': row[0],
                'description': row[1]
            }
            result.append(listed_in)

        return result


"""
Создаём функцию поиска по паре актёров с SQL-запросом и выводим результат.
"""


def get_two_cast(cast_1, cast_2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
            SELECT COUNT(netflix.cast), netflix.cast
            FROM netflix
            WHERE netflix.cast LIKE '%{cast_1}%' AND '%{cast_2}%'
            AND "type" = 'Movie'
            GROUP BY netflix.cast
            """

        cursor.execute(query)
        result_all = cursor.fetchall()

        return result_all


"""
Создаём функцию поиска названия по разным критериям с SQL-запросом 
и выводим название.
"""


def search_title_by_criteria(type_movie, release_date, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
            SELECT title, description
            FROM netflix
            WHERE "type" = '%{type_movie}%'
            AND release_year = '%{release_date}%'
            AND listed_in LIKE '%{genre}%'
            """

        cursor.execute(query)
        result_all = cursor.fetchall()

        return result_all