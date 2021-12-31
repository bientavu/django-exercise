import sys

from main.jsonenv import env

DEBUG = env.get("debug")
TEST = len(sys.argv) > 1 and sys.argv[1] == "test"
