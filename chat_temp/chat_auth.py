import os
import bcrypt
from dotenv import load_dotenv
load_dotenv()
USER_HASHES = {}

for key, value in os.environ.items():

    if key.startswith("RJN_"):

        name = key.replace("RJN_", "")
        USER_HASHES[name] = value.encode()


def authenticate(user, password):

    if user not in USER_HASHES:
        return False

    return bcrypt.checkpw(password.encode(), USER_HASHES[user])

from flask import Blueprint, render_template

chat_bp = Blueprint(
    "chat",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/chat_temp/static"
)

@chat_bp.route("/")
def chat_page():
    return render_template("chat.html")