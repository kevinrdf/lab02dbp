from flask import Flask, request, jsonify
app = Flask(__name__)

listaAnimes = [
        {   
        "id": 1, 
        "titulo": "Araburu Kisetsu no Otome-domo yo", 
        "rating": 7, 
        "tipo": "Serie", 
        "season": "Summer", 
        "categoria": ["Comedy", "Drama", "Romance", "Slice of Life"]
    },

        {   
        "id": 2, 
        "titulo": "Kuzu no Honkai", 
        "rating": 7, 
        "tipo": "Serie", 
        "season": "Winter", 
        "categoria": ["Drama", "Romance", "Ecchi", "Psychological"]
    },

        {   
        "id": 3, 
        "titulo": "Domestic na Kanojo", 
        "rating": 6, 
        "tipo": "Serie", 
        "season": "Winter", 
        "categoria": ["Drama", "Romance", "Ecchi"]
    },

        {   
        "id": 4, 
        "titulo": "Liz to Aoi Tori", 
        "rating": 8, 
        "tipo": "Serie", 
        "season": "Spring", 
        "categoria": ["Drama", "Music", "Slice of Life"]
    },

        {   
        "id": 5, 
        "titulo": "Koe no Katachi", 
        "rating": 9, 
        "tipo": "Serie", 
        "season": "Summer", 
        "categoria": ["Drama", "Romance", "Slice of Life"]
    }

]

@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask'

#Mostrar la lista de animes
@app.route('/anime', methods=['GET'])
def getAnimes():
    return jsonify(listaAnimes)

#Crear un nuevo anime
@app.route('/anime', methods=['POST'])
def createAnime():
    data = request.get_json()
    listaAnimes.append(data)
    return jsonify(data), 201

#Obtener un anime por ID
@app.route('/anime/<int:id>', methods=['GET'])
def getAnime(id):
    if id < len(listaAnimes):
        anime = listaAnimes[id]  
    else:
        None
    return jsonify(anime)

#Eliminar un anime por ID
@app.route('/anime/<int:id>', methods=['DELETE'])
def deleteAnime(id):
    if id < len(listaAnimes):
        deleted_anime = listaAnimes.pop(id)
        return jsonify(deleted_anime), 200
    else:
        return jsonify({"ERROR": "Anime no encontrado"}), 404

#Actualizar un anime por ID
@app.route('/anime/<int:id>', methods=['PUT'])
def updateAnime(id):
    data = request.get_json()
    if id < len(listaAnimes):
        listaAnimes[id] = data
        return jsonify(data), 200
    else:
        return jsonify({"ERROR": "Anime no encontrado"}), 404

#Actualizar parcialmente un anime por ID
@app.route('/anime/<int:id>', methods=['PATCH'])
def patchAnime(id):
    data = request.get_json()
    if id < len(listaAnimes):
        current_anime = listaAnimes[id]
        current_anime.update(data)
        return jsonify(current_anime), 200
    else:
        return jsonify({"ERROR": "Anime no encontrado"}), 404

if __name__ == '__main__':
    app.run()