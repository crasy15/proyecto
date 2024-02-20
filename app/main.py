from fastapi import FastAPI, requests, Response
app = FastAPI()

@app.get("/")
async def root ():
    return {"message": "la aplicacion esta en funcionamiento!"}
