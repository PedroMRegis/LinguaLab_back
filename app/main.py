from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path


app = FastAPI()

# Permitir conexão com o React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# BASE_DIR aponta para a pasta app/
BASE_DIR = Path(__file__).resolve().parent

@app.get("/aulas")
def get_aulas():
    arquivo = BASE_DIR / "data" / "Aulas.csv"
    df = pd.read_csv(arquivo)
    return df.to_dict(orient="records")

@app.get("/base")
def get_base():
    # monta o path correto para o seu CSV em app/data
    arquivo = BASE_DIR / "data" / "base.csv"
    df = pd.read_csv(arquivo)
    return df.to_dict(orient="records")
