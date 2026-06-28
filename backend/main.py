from fastapi import FastAPI

app = FastAPI(title="Abanos API", version="0.1.0")

@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "project": "Abanos",
        "version": "0.1.0"
    }
