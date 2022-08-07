from fastapi import FastAPI

app = FastAPI()

@app.get("/database")
def get_db():
    return '[{"description":"something important","completed":false,"editing":false}]'