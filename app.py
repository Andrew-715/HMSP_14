from flask import Flask
from utils import *


app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Это главная страница'


@app.route('/movie/<title>')
def info_about_movie(title):
    return title_dict(title)


@app.route('/movie/<year>/to/<year>')
def range_release_years():
    pass


if '__main__' == __name__:
    app.run(host='127.0.0.1', port=8000, debug=True)