from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS


app = Flask(__name__)
init_app(app)
#permite solicitudes de cualquier origen
CORS(app)

app.route("/", methods=["GET"])(index)#mensaje 👽
app.route("/api/videos/", methods=["GET"])(get_all_video)#ver todos los registros
app.route("/api/videos/", methods=["POST"])(create_video)#insertar registro
app.route("/api/videos/<int:id_video>", methods=["GET"])(get_video)#visualiza un video
app.route("/api/videos/<int:id_video>", methods=["PUT"])(update_video)#actualiza un registro
app.route("/api/videos/<int:id_video>", methods=["DELETE"])(delete_video)#elimina un registro


if __name__ == "__main__":
    app.run(debug=True)
