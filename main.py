from fastapi import FastAPI
from models import Musique

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Bienvenue dans le magasin de musique"}

@app.post("/musique/")
def ajouter_musique(musique: Musique):
    # À compléter avec stockage DB
    return {"message": "Musique ajoutée", "musique": musique}