from fastapi import FastAPI
from dao.database import start_engine

app = FastAPI()

start_engine()