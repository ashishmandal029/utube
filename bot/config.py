import os


class Config:

    BOT_TOKEN = os.environ.get("7672885270:AAHHvb0DKvju3OVVslKCLJp-rjY5N_He2KE")

    SESSION_NAME = os.environ.get("stkuserbot", ":memory:")

    API_ID = os.environ.get("24871620")

    API_HASH = os.environ.get("e4195bedc71234a179a3d9ac0cad6401")

    CLIENT_ID = os.environ.get("1030398326032-lplhdgttff6qjgrs30bgs24a5kav1hl8.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = os.environ.get("5728398903")

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "5728398903")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
