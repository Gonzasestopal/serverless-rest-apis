import os

from fastapi import FastAPI
from mangum import Mangum

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

# Here is the magic
app = FastAPI(openapi_prefix=openapi_prefix)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def get_users():
    return {"message": "Get Users!"}

handler = Mangum(app)
