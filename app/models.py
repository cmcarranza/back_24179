from app.database import get_db

class Video:
    # constructor
    def __init__(self, id_videos=None, titulo=None, genero=None, grupo=None, anio=None):
        self.id_videos = id_videos
        self.titulo = titulo
        self.genero = genero
        self.grupo = grupo
        self.anio = anio
    
    @staticmethod
     # visualiza un video de la BD
    def get_by_video(id_video):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM videos WHERE id_video = %s", (id_video))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Video(id_video=row[0],titulo=row[1],genero=row[2],grupo=row[3],anio=row[4])
        return None
    
    # visualiza todo el contenido de la BD
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROMc videos")
        rows = cursor.fetchall()
        videos = []
        for row in rows:
            new_videos = Video(row[0], row[1], row[2], row[3], row[4])
            videos.append(new_videos)
        cursor.close()
        return videos

    #realiza insert/update en la BD
    def save(self):
    
        db = get_db()
        cursor = db.cursor()
        if self.id_videos:
            query=""" UPDATE videos SET titulo= %s, genero= %s, grupo= %s, anio= %s""",(self.titulo,self.genero,self.grupo,self.anio)
            cursor.execute(query)
        else:
            cursor.execute(""" INSERT INTO videos (titulo, genero, grupo, anio) VALUES (%s,%s,%s,%s)""",
                           (self.titulo,self.genero,self.grupo,self.anio))
            self.id_videos= cursor.lastrowid
        db.commit()
        cursor.close()
   
    #para la lista de videos
    def serialize(self):
        return {
            "id_videos": self.id_videos,
            "titulo": self.titulo,
            "genero": self.genero,
            "grupo": self.grupo,
            "anio": self.anio
        }

    #elimina un video usando id_video
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM videos WHERE id_videos = %s", (self.id_videos,))
        db.commit()
        cursor.close()