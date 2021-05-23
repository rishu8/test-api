import os


def fallback_to(val, default):
    if val is None or val == "":
        return default
    else:
        return val


class Info:
    app_name = fallback_to(os.getenv("APP_NAME"), "N/A")
    app_version = fallback_to(os.getenv("APP_VERSION"), "N/A")
    commit_hash = fallback_to(os.getenv("COMMIT_HASH"), "N/A")
