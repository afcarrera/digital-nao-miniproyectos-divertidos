
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, IntegerField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, length

EMPTY_MESSAGE = 'El campo esta vacio.'

class number_to_letters_form(FlaskForm):
    number = StringField('Número',   [
        DataRequired(message=EMPTY_MESSAGE),
        length(max=12, message='Número de máximo 12 dígitos')])
    submit = SubmitField('Convertir')
    letters = StringField('Letras')

class web_scraper_page_form(FlaskForm):
    page = IntegerField('Página',   [
        DataRequired(message=EMPTY_MESSAGE),
        length(max=4, message='Número de máximo 4 dígitos')])
    submit = SubmitField('Buscar')

class web_scraper_movie_form(FlaskForm):
    page = IntegerField('Página')
    movie = SelectField('Película')
    title = HiddenField()
    transcript = HiddenField()
    submit = SubmitField('Buscar')

class ussd_form(FlaskForm):
    ussd = StringField('USSD',   [
        DataRequired(message=EMPTY_MESSAGE),
        length(max=36, message='Número de máximo 36 dígitos')])
    submit = SubmitField('Llamar')

class ussd_options_form(FlaskForm):
    menu = HiddenField()
    ussd = HiddenField()
    option = IntegerField('Opción',   [
        DataRequired(message=EMPTY_MESSAGE),
        length(max=4, message='Número de máximo 4 dígitos')])
    send = SubmitField('Enviar')

class movies_form(FlaskForm):
    movies = SelectField('Películas')
    users = SelectField('Usuarios')
    ratings = SelectField('Rating')
    submit = SubmitField('Calificar')
    movies_list = StringField(widget=TextArea())

class hanged_game_form(FlaskForm):
    hint = StringField('Pista')
    word = StringField('Palabra' , [
        DataRequired(message=EMPTY_MESSAGE),
        length(max=1, message='Máximo una letra')])
    A = SubmitField('A')
    B = SubmitField('B')
    C = SubmitField('C')
    D = SubmitField('D')
    E = SubmitField('E')
    F = SubmitField('F')
    G = SubmitField('G')
    H = SubmitField('H')
    I = SubmitField('I')
    J = SubmitField('J')
    K = SubmitField('K')
    L = SubmitField('L')
    M = SubmitField('M')
    N = SubmitField('N')
    O = SubmitField('O')
    P = SubmitField('P')
    Q = SubmitField('Q')
    R = SubmitField('R')
    S = SubmitField('S')
    T = SubmitField('T')
    U = SubmitField('U')
    V = SubmitField('V')
    W = SubmitField('W')
    X = SubmitField('X')
    Y = SubmitField('Y')
    Z = SubmitField('Z')
    message = StringField('Mensaje')
    info = StringField('Intentos')