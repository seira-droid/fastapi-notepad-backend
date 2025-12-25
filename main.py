from fastapi import FastAPI

app = FastAPI(title="Notepad Backend API")

@app.get("/")
def root():
    return {"message": "FastAPI Notepad Backend is running"}
