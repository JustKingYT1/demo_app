from server.database.db_manager import db_manager
import settings, uvicorn
from fastapi import FastAPI
from server.router import routers
from fastapi.responses import RedirectResponse

app = FastAPI(title='Shesterochka', version='0.1 Alpha')

[app.include_router(router) for router in routers]

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')

def start_server() -> None:
    uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)


if settings.DEBUG:
    if __name__ == "__main__":
        uvicorn.run(app='start_server:app', reload=True, host=settings.HOST, port=settings.PORT)