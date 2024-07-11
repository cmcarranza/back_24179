from flask import jsonify,request
from app.database import get_db
from app.models import Video

def index():
    response = {"mensagge": "Hola mundo desde API Flask 👽"}
    return jsonify(response)


#funcion que busca listado de videos
def get_all_video():
    videos = Video.get_all()
    list_videos = [videos.serialize() for videos in videos]
    return jsonify(list_videos)


#funcion que busca un video
def get_video(id_video):
    video = Video.get_by_video(id_video)
    if not video:
        return jsonify({"mensagge": "Video no encontrado"}), 404
    return jsonify(video.serialize())

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
        return jsonify({"message": "Video no encontrado"}), 404
    data = request.json
    print(f"Datos recibidos para actualización: {data}")
    video.titulo = data.get("titulo", video.titulo)
    video.genero = data.get("genero", video.genero)
    video.grupo = data.get("grupo", video.grupo)
    video.anio = data.get("anio", video.anio)

    video.save()    
    return jsonify({"message": "Video actualizado exitosamente"})
    
    
 
#funcion que elimina un registro
def delete_video(id_video):
    video = Video.get_by_video(id_video)
    if not video:
        return jsonify({"message": "Video no encontrado"}), 404
    video.delete()
    return jsonify({"message": "Video eliminado exitosamente"})