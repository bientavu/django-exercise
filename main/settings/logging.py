from main.jsonenv import env

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": env.get("log_formatter", "simple"),
        },
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name} {funcName}:{lineno} {message}",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{",
        },
        "simple": {
            "format": "{name} {funcName}:{lineno} {message}",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": env.get("log_level", "INFO"),
        },
        "parso": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
