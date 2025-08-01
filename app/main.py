from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()

# Permitir conexão com o React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    df1 = pd.read_csv("Aulas.csv")
    df2 = pd.read_csv("base.csv")
    return { df1.to_dict(orient="records"), df2.to_dict(orient="records")}
