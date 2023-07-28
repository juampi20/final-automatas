# Patrones de expresiones regulares
ARTIST_PATTERN = r'^[\w\s\d\S]{1,20}$'
SPOTIFY_URL_PATTERN = r'^(https?://)?(www\.)?open.spotify.com\/artist\/[\w]{5,22}$'
TRACK_PATTERN = r'^[\w\s\d\S]+$'
ALBUM_PATTERN = r'^[\w\s\d\S]+$'
DURATION_PATTERN = r'^([0-5][0-9]):([0-5][0-9])$'
URI_PATTERN = r'^spotify:track:[a-zA-Z0-9]{10,22}$'
YOUTUBE_URL_PATTERN = r'^(https?://)?(www\.)?youtube.com\/watch\?v=[\w_-]{5,11}$'
TITLE_PATTERN = r'^[\w\s\d\S]+$'

# Mensajes de error
ARTIST_ERROR_MESSAGE = "El nombre del artista debe tener máximo 20 caracteres y puede contener letras, números o símbolos."
SPOTIFY_URL_ERROR_MESSAGE = "La URL de Spotify debe tener el formato correcto, por ejemplo: https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ."
TRACK_ERROR_MESSAGE = "El nombre de la canción debe ser alfanumérico y puede contener letras, números o símbolos."
ALBUM_ERROR_MESSAGE = "El nombre del álbum debe ser alfanumérico y puede contener letras, números o símbolos."
URI_ERROR_MESSAGE = "La URI de Spotify debe tener el formato correcto, por ejemplo: spotify:track:0d28khcov6AiegSCpG5TuT."
YOUTUBE_URL_ERROR_MESSAGE = "La URL de Youtube debe tener el formato correcto, por ejemplo: https://www.youtube.com/watch?v=HyHNuVaZJ-k."
TITLE_ERROR_MESSAGE = "El título puede contener letras, números o símbolos."
DURATION_ERROR_MESSAGE = "La duración debe tener el formato correcto, por ejemplo: 03:45."