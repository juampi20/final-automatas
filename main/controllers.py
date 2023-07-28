from flask import Blueprint, jsonify, request
from main.services import Service

automata = Blueprint('automata', __name__)
service = Service()  # Instancia del servicio para usar en los endpoints

@automata.route('/likes', methods=['GET'])
def get_most_like():
    data = service.get_top_n_by_column('Track', 'Likes', 5)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/comments', methods=['GET'])
def get_most_comments():
    data = service.get_top_n_by_column('Track', 'Comments', 5)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/views', methods=['GET'])
def get_most_views():
    data = service.get_top_n_by_column('Track', 'Views', 5)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/rating', methods=['GET'])
def get_most_rating():
    data = service.get_top_n_by_column('Track', 'Rating', 5)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/duration', methods=['GET'])
def get_most_duration():
    data = service.get_most_duration()
    return jsonify(data.to_dict(orient='records'))

@automata.route('/singer', methods=['GET'])
def get_most_singer():
    data = service.get_top_n_by_column('Artist', 'Views', 10)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/search', methods=['GET'])
def search_song():
    song = request.args.get('song')
    data = service.search_song(song)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/song', methods=['POST'])
def add_song():
    song_data = request.json  # Obtener datos del cuerpo de la solicitud en formato JSON
    data = service.add_song(song_data)
    return jsonify(data.to_dict(orient='records'))

@automata.route('/', methods=['GET'])
def get_df():
    data = service.get_df()
    return jsonify(data.to_dict(orient='records'))
