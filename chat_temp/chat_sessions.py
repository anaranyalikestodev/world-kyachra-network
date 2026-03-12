import secrets
import os

MAX_SESSIONS = 5
MAX_USERS = 5

sessions = {}

ARCHIVE_DIR = "chat_temp/archives"
os.makedirs(ARCHIVE_DIR, exist_ok=True)


def create_session(session_id, user, sid):

    if session_id not in sessions:

        if len(sessions) >= MAX_SESSIONS:
            return "Max sessions reached"

        file_name = f"{ARCHIVE_DIR}/{secrets.token_hex(6)}.dat"

        sessions[session_id] = {
            "users": set(),
            "connections": set(),
            "file": file_name
        }

    if len(sessions[session_id]["users"]) >= MAX_USERS:
        return "Session full"

    sessions[session_id]["users"].add(user)
    sessions[session_id]["connections"].add(sid)

    return "ok"