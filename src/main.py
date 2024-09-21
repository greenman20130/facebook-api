from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from src.facebook_api.router import router as router_facebook
from src.config import ALLOWED_ORIGINS


app = FastAPI()

origins = ALLOWED_ORIGINS.split(';')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'],
                   allow_headers=['*'], allow_credentials=True)

app.include_router(router_facebook)

@app.get("/")
async def root():
    return {"message": "Hello!"}



