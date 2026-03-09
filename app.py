from flask import Flask, redirect, url_for,render_template
from routes.wkn1.notice_routes import notice_bp
from routes.auth_routes import auth_bp
from config import Config
from extensions import db, migrate, bcrypt, api, cors

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

    @app.route("/")
    def home():
        return render_template('data_teal.html')

    return app

if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)