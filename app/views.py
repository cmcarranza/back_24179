from flask import jsonify,request
from app.database import get_db
from app.models import Video

def index():
    response = {"mensagge": "Hola mundo desde API Flask 👽"}
    return jsonify(response)

#funcion que busca un video por id
def get_video(id_video):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM videos WHERE id_video = %s", (id_video))
    row = cursor.fetchone()
    cursor.close()
    if row:
        return Video(id_video=row[0],titulo=row[1],genero=row[2],grupo=row[3],anio=row[4])
    return None


#funcion que busca listado de videos
def get_all_video():
    videos = Video.get_all()
    list_videos = [videos.serialize() for videos in videos]
    return jsonify(list_videos)

#crear nuevo video
def create_video():
    data = request.json
    #agregar despues y borrar este comentario la validacion de dato
    new_video = Video(None,data["titulo"],data["grupo"],data["genero"],data["anio"])
    new_video.save()
    return jsonify({"menssage": "Video creado con exito"}),201


#funcion que actualiza un registo
def update_video(id_video):
    video = Video.get_by_video(id_video)
    if not video:
        return jsonify({"menssage": "Video no encontrado"}),404
    data = request.json
    video.titulo = data["titulo"]
    video.genero = data["genero"]
    video.grupo = data["grupo"]
    video.anio = data["anio"]
    video.save()
    return jsonify({"menssage": "Video actualizado exitosamente"})
    
 
#funcion que elimina un registro
def delete_video(id_video):
    video = Video.get_by_video(id_video)
    if not video:
        return jsonify({"menssage": "Video no encontrado"}),404
    video.delete()
    return jsonify({"menssage": "Video eliminado exitosamente"})

