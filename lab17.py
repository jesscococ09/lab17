from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

class Playlist(FlaskForm):
    song_title = StringField(
        'Song Title', 
        validators=[DataRequired()]
    )
class Genre(FlaskForm):
    genre_fill = StringField(
        'Genre', 
        validators=[DataRequired()]
    )

playlist = []
genre= []

def store_song(my_song):
    playlist.append(dict(
        song = my_song,
        date = datetime.today()
    ))
def store_genre(my_genre):
    genre.append(dict(
        genre= my_genre,
        date= datetime.today()
    ))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Playlist()
    formg = Genre()
    if form.validate_on_submit() and formg.validate_on_submit():
        store_song(form.song_title.data)
        store_genre(formg.genre_fill.data)
        return redirect('/view_playlist')
    return render_template('index.html', form=form, formg=formg)

@app.route('/view_playlist')
def vp():
    return render_template('vp.html', playlist=playlist, genre=genre)