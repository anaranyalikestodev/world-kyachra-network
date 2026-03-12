import time
from flask import request
from flask_socketio import emit, join_room

from .chat_sessions import sessions, create_session
from .chat_storage import append_message, finalize_archive
from .chat_auth import authenticate


def register_chat(app, socketio):

    @socketio.on("chat_join")
    def join(data):

        user = data["user"]
        password = data["password"]
        session_id = data["session"]

        if not authenticate(user, password):
            emit("error", {"msg": "Authentication failed"})
            return

        result = create_session(session_id, user, request.sid)

        if result != "ok":
            emit("error", {"msg": result})
            return

        join_room(session_id)

        emit("chat_joined", {"session": session_id})


    @socketio.on("chat_message")
    def message(data):

        session_id = data["session"]
        user = data["user"]
        text = data["text"]

        msg = {
            "user": user,
            "text": text,
            "time": time.time()
        }

        session = sessions.get(session_id)

        if session:
            append_message(session, msg)

        emit("chat_message", msg, room=session_id)


    @socketio.on("disconnect")
    def handle_disconnect():

        sid = request.sid

        for session_id in list(sessions.keys()):

            session = sessions[session_id]

            if sid in session["connections"]:

                session["connections"].remove(sid)

                if len(session["connections"]) == 0:

                    finalize_archive(session["file"])

                    sessions.pop(session_id)

                    print("archived:", session_id)

                break