from flask import Flask, render_template
from flask_socketio import SocketIO

from routes.wkn1.notice_routes import notice_bp
from routes.auth_routes import auth_bp
from config import Config
from extensions import db, migrate, bcrypt, api, cors

from chat_temp.chat_module import register_chat
from chat_temp.chat_auth import chat_bp

socketio = SocketIO(cors_allowed_origins="*")


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    socketio.init_app(app)

    app.register_blueprint(notice_bp, url_prefix="/notices")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(chat_bp, url_prefix="/chat")

    register_chat(app, socketio)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app


app = create_app()

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)