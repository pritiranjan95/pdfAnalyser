from decouple import config

HOST = config("HOST")
PORT = int(config("PORT"))