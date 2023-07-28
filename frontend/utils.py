import re
import streamlit as st
import requests

# Definir la URL base de la API
BASE_URL = 'http://localhost:5000/'  # Cambiar esta URL por la que corresponda a tu API

# Función para hacer una solicitud GET a la API
def get_data(endpoint):
    url = BASE_URL + endpoint
    response = requests.get(url)
    return response.json()

# Función para buscar canciones por nombre
def search_song(song_name):
    url = BASE_URL + 'search'
    params = {'song': song_name}
    response = requests.get(url, params=params)
    return response.json()

# Función para agregar una nueva canción
def add_new_song(song_data):
    url = BASE_URL + 'song'
    response = requests.post(url, json=song_data)
    return response.json()

def validate_input(value, pattern, error_message):
    if not re.match(pattern, value):
        st.error(error_message)
        return False
    return True

