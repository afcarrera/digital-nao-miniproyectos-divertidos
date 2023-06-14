from flask import Flask, render_template, redirect, url_for, request
from wtforms import SubmitField, HiddenField
from forms import number_to_letters_form, web_scraper_page_form, web_scraper_movie_form, ussd_form, ussd_options_form, movies_form, hanged_game_form
from apps.number_to_letters.number_to_letters import NumberToLetters
from apps.web_scraper.web_scraper import WebScraper
from apps.ussd.ussd import USSD
from apps.movie_ratings.movie_ratings import MovieRatings
from apps.hanged_game.hanged_game import HangedGame
from utils.hanged_game import hanged_game_util
from utils.ussd import ussd_util
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'acarrera'

EMPTY_MESSAGE = 'El campo esta vacio.'

_ussd = USSD()
_ussd_actual = 0

_movie_ratings = MovieRatings()

_tries = 8
_random = None
_wl = []
_word_info = None
_word_hint = None
_word = None
_goods = 0
_letters = set()

@app.route("/")
def home():    
    return render_template('index.html')

@app.route("/number_to_letters", methods = ['GET', 'POST'])
def number_to_letters():
    form = number_to_letters_form()
    if form.is_submitted() and form.number.data:
        try:
            number = float(form.number.data)
            number_to_letters = NumberToLetters()
            form.letters.label = number_to_letters.number_to_letters(number)
        except (ValueError):
            form.letters.label = 'ERROR AL CONVERTIR NÚMERO'
        except (OverflowError):
            form.letters.label = 'NÚMERO DEMASIADO GRANDE'
    return render_template('number_to_letters/number_to_letters.html', form=form)

@app.route("/web_scraper_page", methods = ['GET', 'POST'])
def web_scraper_page():
    form = web_scraper_page_form()
    if form.is_submitted() and form.page.data:
        return redirect(url_for('web_scraper_movie', page=form.page.data))
    return render_template('web_scraper/web_scraper_page.html', form=form)

@app.route("/web_scraper_movie/<page>", methods = ['GET', 'POST'])
def web_scraper_movie(page):
    web_scraper = WebScraper()
    form = web_scraper_movie_form()
    movies = web_scraper.web_scraper_page(page)
    form.movie.choices = [(key, value) for key, value in movies.items()]
    if form.is_submitted() and form.movie.data:
        title, transcript = web_scraper.web_scraper_movie(form.movie.data)
        form.title.label = title
        form.transcript.label = transcript
    return render_template('web_scraper/web_scraper_movie.html', form=form)

@app.route("/ussd", methods = ['GET', 'POST'])
def ussd():
    global _ussd_actual
    form = ussd_form()
    if form.is_submitted() and form.ussd.data:
        ussd_data = form.ussd.data
        if ussd_data in _ussd.ids:
            id_ussd = _ussd.ids[ussd_data]
            _ussd_actual = id_ussd
            return redirect(url_for('ussd_options', ussd_data=ussd_data, id_ussd=id_ussd))
    return render_template('ussd/ussd.html', form=form)

@app.route("/ussd_options/<ussd_data>/<id_ussd>", methods = ['GET', 'POST'])
def ussd_options(id_ussd, ussd_data):
    global _ussd_actual
    form = ussd_options_form()
    form.ussd.data = ussd_data
    id_ussd = int(id_ussd)
    if ussd_data in _ussd.ids and id_ussd in _ussd.root: 
        _opt_root = _ussd.root[id_ussd]
        if form.option.data:
            opt_int = int(form.option.data) - 1
            print(opt_int, _opt_root.childs)   
            if 0 <= opt_int \
                and ((opt_int< len(_opt_root.childs) - 1 and -1 in _opt_root.childs) or 
                     (opt_int< len(_opt_root.childs) and -1 not in _opt_root.childs)):
                opt_ch = _opt_root.childs[opt_int]
                opt_o = _ussd.root[opt_ch]
                form.menu.label = ussd_util.get_menu(opt_o, _ussd_actual, _ussd)
                _ussd_actual = opt_ch
                print(_ussd_actual)
                return redirect(url_for('ussd_options', ussd_data=ussd_data, id_ussd=opt_ch))
            elif opt_int == len(_opt_root.childs) - 1 and -1 in _opt_root.childs:
                form.menu.label = ussd_util.get_menu(_ussd.root[_opt_root.parent], _ussd_actual, _ussd)
                _ussd_actual = _opt_root.parent
                return redirect(url_for('ussd_options', ussd_data=ussd_data, id_ussd=_opt_root.parent))
            else:
                return redirect(url_for('ussd_options', ussd_data=ussd_data, id_ussd=_ussd_actual))
        else:
            form.menu.label = ussd_util.get_menu(_opt_root, _ussd_actual, _ussd)
    return render_template('ussd/ussd_options.html', form=form)
    
@app.route("/movie_ratings", methods = ['GET', 'POST'])
def movie_ratings():
    form = movies_form()
    form.movies.choices = [(key, value.get_name()) for key, value in _movie_ratings.get_movies().items()]
    form.users.choices = [(key, value.get_name()) for key, value in _movie_ratings.get_users().items()]
    form.ratings.choices = [(key, value) for key, value in _movie_ratings.get_ratings().items()]
    form.movies_list.data = _movie_ratings.to_string()
    if form.is_submitted() and form.movies.data and form.users.data and form.ratings.data:
        _movie_ratings.rate_movie(int(form.movies.data), int(form.ratings.data), form.users.data)
        form.movies_list.data = _movie_ratings.to_string()
    return render_template('movie_ratings/movie_ratings.html', form=form)

@app.route("/hanged_game", methods = ['GET', 'POST'])
def hanged_game():
    global _random
    global _word_info
    global _word_hint
    global _word
    global _wl
    global _goods
    global _tries
    global _letters
    space = ' '
    form = hanged_game_form()
    hanged_game = HangedGame()
    words_list = hanged_game.get_words()
    if _random is None:
        form.info.label = 'Intentos'
        _random = random.randrange(len(words_list))
        _word = words_list[_random][0]
        _word_hint = words_list[_random][1]
        _word_info = words_list[_random][2]
        _wl = ['_'] * len(_word)
        form.word.label = space.join(_wl)
        form.hint.label = _word_hint
        form.message.label = str(_tries)
        if space in _word_info:
            idx_list = _word_info[space]
            _goods += hanged_game_util.refill_phrase(_wl, idx_list, space)
    if form.hint.label != _word_hint:
        form.word.label = space.join(_wl)
        form.hint.label = _word_hint
        form.message.label = str(_tries)
    if form.is_submitted() and _tries > 0:
        form.hint.label = _word_hint
        form.word.label = space.join(_wl)
        letter = hanged_game_util.get_letter_selected(request)
        print('LETRA', letter, _goods, len(_word))
        if letter in _word_info and letter not in _letters:
            _letters.add(letter)
            idx_list = _word_info[letter]
            _goods += hanged_game_util.refill_phrase(_wl, idx_list, letter)
            form.word.label = space.join(_wl)
            if _goods == len(_word):
                form.info.label = 'FELICIDADES LO LOGRASTE'
                _goods = 0
                _random = None
                _letters = set()
                _tries = 9
        elif letter not in _letters:
            _tries -= 1
        form.message.label = str(_tries)        
    if _tries <= 0:
        form.info.label = 'PERDISTE INTENTALO DE NUEVO'
        _goods = 0
        _random = None
        _letters = set()
        _tries = 9
        
    
    return render_template('hanged_game/hanged_game.html', form=form)
if __name__ == '__main__':
    app.run(port=8000, debug=True)