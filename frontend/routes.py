import streamlit as st
from utils import get_data, search_song, add_new_song, validate_input
from constants import ARTIST_PATTERN, SPOTIFY_URL_PATTERN, TRACK_PATTERN, ALBUM_PATTERN, URI_PATTERN, \
    YOUTUBE_URL_PATTERN, TITLE_PATTERN, DURATION_PATTERN, ARTIST_ERROR_MESSAGE, SPOTIFY_URL_ERROR_MESSAGE, TRACK_ERROR_MESSAGE, \
    ALBUM_ERROR_MESSAGE, URI_ERROR_MESSAGE, YOUTUBE_URL_ERROR_MESSAGE, TITLE_ERROR_MESSAGE, DURATION_ERROR_MESSAGE


# Endpoint para ver el DataFrame completo
def show_dataframe_template():
    st.header("DataFrame")
    data = get_data('')
    st.table(data)


# Endpoint para obtener las canciones con más likes
def show_likes_template():
    st.header("Canciones con más Likes")
    data = get_data('likes')
    st.table(data)


# Endpoint para obtener las canciones con más comentarios
def show_comments_template():
    st.header("Canciones con más Comentarios")
    data = get_data('comments')
    st.table(data)


# Endpoint para obtener las canciones con más vistas
def show_views_template():
    st.header("Canciones con más Vistas")
    data = get_data('views')
    st.table(data)


# Endpoint para obtener las canciones con mejor rating
def show_rating_template():
    st.header("Canciones con mejor Rating")
    data = get_data('rating')
    st.table(data)


# Endpoint para obtener las canciones con mayor duración
def show_duration_template():
    st.header("Canciones con mayor Duración")
    data = get_data('duration')
    st.table(data)


# Endpoint para obtener los 10 cantantes con más vistas
def show_singers_template():
    st.header("10 Cantantes con más Vistas")
    data = get_data('singer')
    st.table(data)


# Endpoint para buscar canciones por nombre
def search_song_template():
    st.header("Buscar Canción")
    song_name = st.text_input("Ingresa el nombre de la canción:")
    if st.button("Buscar"):
        data = search_song(song_name)
        st.table(data)


# Endpoint para agregar una nueva canción
def add_new_song_template():
    st.header("Agregar Nueva Canción")

    track = st.text_input("Nombre de la Canción:")
    if not validate_input(track, TRACK_PATTERN, TRACK_ERROR_MESSAGE): return

    artist = st.text_input("Artista:")
    if not validate_input(artist, ARTIST_PATTERN, ARTIST_ERROR_MESSAGE): return

    album = st.text_input("Álbum:")
    if not validate_input(album, ALBUM_PATTERN, ALBUM_ERROR_MESSAGE): return

    duration = st.text_input("Duración (MM\:SS):")
    if not validate_input(duration, DURATION_PATTERN, DURATION_ERROR_MESSAGE): return

    url_spotify = st.text_input("URL de Spotify:")
    if not validate_input(url_spotify, SPOTIFY_URL_PATTERN, SPOTIFY_URL_ERROR_MESSAGE): return

    uri = st.text_input("URI de Spotify:")
    if not validate_input(uri, URI_PATTERN, URI_ERROR_MESSAGE): return

    url_youtube = st.text_input("URL de Youtube:")
    if not validate_input(url_youtube, YOUTUBE_URL_PATTERN, YOUTUBE_URL_ERROR_MESSAGE): return

    title = st.text_input("Título de youtube:")
    if not validate_input(title, TITLE_PATTERN, TITLE_ERROR_MESSAGE): return

    if st.button("Agregar"):
        song_data = {
            'Track': track,
            'Artist': artist,
            'Album': album,
            'Album_type': 'album',
            'Duration': duration,

            'Url_spotify': url_spotify,
            'Uri': uri,
            'Url_youtube': url_youtube,
            'Title': title,

            'Likes': 0,
            'Comments': 0,
            'Views': 0,
            'Rating': 0
        }
        data = add_new_song(song_data)
        st.table(data)
