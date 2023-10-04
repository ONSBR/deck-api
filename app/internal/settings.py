import os


class Settings:
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", "80"))
    root_path = os.getenv("ROOT_PATH", "/")

    @classmethod
    def read_environments(cls):
        cls.host = os.getenv("HOST", "localhost")
        cls.port = int(os.getenv("PORT", "80"))
        cls.root_path = os.getenv("ROOT_PATH", "/")
