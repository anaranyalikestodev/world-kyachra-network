from flask import Flask, redirect, url_for,render_template
from routes.wkn1.notice_routes import notice_bp
from routes.auth_routes import auth_bp
from config import Config
from extensions import db, migrate, bcrypt, api, cors

from flask_socketio import SocketIO
from chat_temp.chat_module import register_chat
from chat_temp.chat_auth import chat_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load config from config.py

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    app.register_blueprint(notice_bp, url_prefix="/notices")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(chat_bp,url_prefix="/chat")

    @app.route("/")
    def home():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app=create_app()
    socket_io=SocketIO(app,cors_allowed_origins="*")
    register_chat(app,socket_io)
    socket_io.run(app,debug=True,host="0.0.0.0",port=5000)