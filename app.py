from flask import Flask, jsonify
import utils


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


"""
Создаём вьюшку для отображения главной страницы.
"""


@app.route('/')
def home_page():
    return 'Это главная страница'


"""
Создаём вьюшку для отображения фильма по названию.
"""


@app.route('/movie/<title>')
def info_about_movie(title):
    result = utils.search_by_name(title)
    return jsonify(result)


"""
Создаём вьюшку для отображения фильма по годам.
"""


@app.route('/movie/<int:old_year>/to/<int:new_year>')
def range_release_years(old_year, new_year):
    result =  utils.search_by_release_year(old_year, new_year)
    return jsonify(result)


"""
Создаём вьюшку для отображения фильмов по детскому рейтингу.
"""


@app.route('/movie/rating/children')
def search_movie_rating_children():
    result = utils.movie_rating_children()
    return jsonify(result)


"""
Создаём вьюшку для отображения фильмов по семейному рейтингу.
"""


@app.route('/movie/rating/family')
def search_movie_rating_family():
    result = utils.movie_rating_family()
    return jsonify(result)


"""
Создаём вьюшку для отображения фильмов по взрослому рейтингу.
"""


@app.route('/movie/rating/adult')
def search_movie_rating_adult():
    result = utils.movie_rating_adult()
    return jsonify(result)


"""
Создаём вьюшку для отображения фильмов по жанру.
"""


@app.route('/movie/genre/<genre>')
def search_movie_genre(genre):
    result = utils.title_genre(genre)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

