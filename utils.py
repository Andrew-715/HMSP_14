import sqlite3


def search_by_name():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        querly = """SELECT title, country, release_year, listed_in, description
                 FROM netflix
                 WHERE release_year = 2021
                 AND type = 'Movie'
                 AND country !=''
        """

        cursor.execute(querly)
        result_all = cursor.fetchall()
        keys = [
            "title",
            "country",
            "release_year",
            "listed_in",
            "description"
        ]

        result = []

        for result_row in result_all:
            result.append({keys[i]: result_row[i] for i in range(len(keys))})

        return result


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
        keys = [
            "title",
            "release_year"
        ]

        result = []

        for result_row in result_all:
            result.append({keys[i]: result_row[i] for i in range(len(keys))})

        return result


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

        cursor.execute(querly)

        for row in cursor.fetchall():
            print(row)


def title_dict(title):
    list_dict = search_by_name()
    result = {}

    for d in list_dict:
        result.update(d)
        if title in result.values():
            return result


def title_years(year_1, year_2):
    list_dict = search_by_release_year()
    result = {}


    for d in list_dict:
        result.update(d)
        if year_1 or year_2 in result.values():
            return result

    return result

print(title_years(2006, 2010))