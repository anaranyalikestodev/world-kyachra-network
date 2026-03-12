import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///database.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get(
        "S_KEY", "super_secret_session_key"
    )
    WKN1_KEY = os.environ.get(
        "WKN1_KEY", "WeVeryMuchLoveKyachra"
    )
    WKN2_KEY=os.environ.get(
        "WKN2_KEY", "IsNotWeLoveKyachra"
    )
    TEMP_KEY=os.environ.get(
        "TEMP_KEY", "EverythingIsTemporary"
    )
