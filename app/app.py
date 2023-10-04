from fastapi import FastAPI

# Import dos routers específicos
import app.routers.newave.clast as clast


def get_app(root_path: str):
    app = FastAPI(root_path=root_path)
    app.include_router(clast.router)
    return app
