import json
import os


def get_env_file():
    conf = os.environ.get("CONF", "")
    file_ = ".env.json"
    if conf:
        file_ = f".env.{conf}.json"
    return file_


env_file = get_env_file()


def get_credentials():
    env_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(env_file_dir, env_file), "r") as f:
        creds = json.loads(f.read())
    return creds


env = get_credentials()
