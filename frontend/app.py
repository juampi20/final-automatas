import streamlit as st
from routes import show_likes_template, show_comments_template, show_views_template, show_rating_template, \
    show_duration_template, show_singers_template, search_song_template, add_new_song_template, show_dataframe_template

# Definir el título de la aplicación
st.title("Análisis de Canciones")

# Opciones del menú
option = st.sidebar.selectbox("Selecciona una opción:", ['Ver DataFrame', 'Canciones con más Likes',
                                                        'Canciones con más Comentarios',
                                                        'Canciones con más Vistas', 'Canciones con mejor Rating',
                                                        'Canciones con mayor Duración', '10 Cantantes con más Vistas',
                                                        'Buscar Canción', 'Agregar Nueva Canción'])

# Mostrar la información según la opción seleccionada
if option == 'Ver DataFrame':
    show_dataframe_template()
elif option == 'Canciones con más Likes':
    show_likes_template()
elif option == 'Canciones con más Comentarios':
    show_comments_template()
elif option == 'Canciones con más Vistas':
    show_views_template()
elif option == 'Canciones con mejor Rating':
    show_rating_template()
elif option == 'Canciones con mayor Duración':
    show_duration_template()
elif option == '10 Cantantes con más Vistas':
    show_singers_template()
elif option == 'Buscar Canción':
    search_song_template()
elif option == 'Agregar Nueva Canción':
    add_new_song_template()


