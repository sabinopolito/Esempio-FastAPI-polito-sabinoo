from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class NomePostRequest(BaseModel):
    nome: str


nomi = []


@app.post("/nome")
def post_nome(nomeReq: NomePostRequest):
    nomi.append(nomeReq.nome)


@app.get("/nome")
def get_nome():
    return nomi


@app.delete("/nome/{nome}")
def delete_nome(nome: str):
    if nome in nomi:
        nomi.remove(nome)
        return {"message": f"Nome '{nome}' eliminato"}
    return {"message": f"Nome '{nome}' non trovato"}


@app.get("/")
def saluta():
    return {"message":"Ciao!"}