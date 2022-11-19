from flask import Flask, jsonify
import utils


app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Это главная страница'


@app.route('/movie/<title>')
def info_about_movie(title):

    result = utils.search_by_name(title)
    return jsonify(result)

#
# @app.route('/movie/<year>/to/<year>')
# def range_release_years():
#     pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
