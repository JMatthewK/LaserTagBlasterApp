from fastapi import FastAPI
from endpoints import registration, match

app = FastAPI()
# 127.0.0.1:8000

# Route decorator
@app.get("/")
def home():
    return {"message": "Hello, LaserTag!"}

app.include_router(match.router)
app.include_router(registration.router)
        