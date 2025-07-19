from fastapi import FastAPI
import requests
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def root():
    logging.info("Received request at API1")
    response = requests.get("http://api2:8001/")
    logging.info(f"Response from API2: {response.text}")
    return {"from_api2": response.text}
