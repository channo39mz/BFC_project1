from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def root():
    logging.info("Received request at API2")
    return "Hello from API2!"
