import os


def fallback_to(val, default):
    if val is None or val == "":
        return default
    else:
        return val


class Meta:

    app_env_context = fallback_to(os.getenv("APP_ENV_CONTEXT"), "N/A")
    build_num = fallback_to(os.getenv("APP_VERSION_NUMBER"), "N/A")
    commit_hash = fallback_to(os.getenv("APP_GIT_COMMIT_HASH"), "N/A")
