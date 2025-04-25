from fastapi import FastAPI
from app.cv_data import cv_info

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API de CV"}

@app.get("/cv")
def get_cv():
    return cv_info
