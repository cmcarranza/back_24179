from app.database import get_db
#from datetime import date

class Video:
    # constructor
    def __init__(self, id_video=None, titulo=None, genero=None, grupo=None, anio=None):
        self.id_video = id_video
        self.titulo = titulo
        self.genero = genero
        self.grupo = grupo
        self.anio = anio
    
    @staticmethod
     # visualiza un video de la BD
    def get_by_video(video_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM videos WHERE id_video = %s", (video_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Video(id_video=row[0], titulo=row[1], genero=row[2], grupo=row[3],anio=row[4])
        return None
    

    # visualiza todo el contenido de la BD
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM videos")
        rows = cursor.fetchall()
        videos = []
        for row in rows:
            new_videos = Video(row[0], row[1], row[2], row[3], row[4])
            videos.append(new_videos)
        cursor.close()
        return videos

    #realiza insert/update en la BD


    def save(self):
        print("entrooooooooooooooo")
        db = get_db()
        cursor = db.cursor()
        
        if self.id_video:
            print("esto es el if de update")
            query = """ UPDATE videos SET titulo= %s, genero= %s, grupo= %s, anio= %s WHERE id_video = %s """
            cursor.execute(query, (self.titulo, self.genero, self.grupo, self.anio, self.id_video))
            db.commit()
            
        else:
            cursor.execute(""" INSERT INTO videos (titulo, genero, grupo, anio) VALUES (%s,%s,%s,%s)""",
                       (self.titulo, self.genero, self.grupo, self.anio))
            self.id_video = cursor.lastrowid
            db.commit()
        cursor.close()
  
    


    #Convierte el objeto Video a un diccionario para su fácil serialización a JSON
    def serialize(self):
        return {
            "id_video": self.id_video,
            "titulo": self.titulo,
            "genero": self.genero,
            "grupo": self.grupo,
            "anio": self.anio
        }

    #elimina un video usando su id
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM videos WHERE id_video = %s", (self.id_video,))
        db.commit()
        cursor.close()