from main.jsonenv import env


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": env.get("db_name"),
    }
}
