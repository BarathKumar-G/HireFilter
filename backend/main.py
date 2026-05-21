from fastapi import FastAPI

from routes.screening import router

app = FastAPI(
    title="HireFilter API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "HireFilter API Running"
    }