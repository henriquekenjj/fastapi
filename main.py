from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
from typing import Dict, Optional

app = FastAPI()

# Modelo de dados
class Usuario(BaseModel):
    log_id: int
    log_nome: str
    log_email: str
    log_senha: str
    log_cpf: Optional[int]
    log_cep: Optional[int]
    log_telefone: Optional[int]
    log_datanasc: Optional[datetime.date]

# Simulação de armazenamento de dados
db: Dict[int, Usuario] = {}

# Operação Create
@app.post("/usuarios/")
async def create_usuario(usuario: Usuario):
    db[usuario.log_id] = usuario
    return {"message": "Usuário criado"}

# Operação Read
@app.get("/usuarios/{usuario_log_id}")
async def read_usuario(usuario_log_id: int):
    usuario = db.get(usuario_log_id)
    if usuario:
        return usuario
    return {"message": "Usuário não encontrado"}

# Operação Update
@app.put("/usuarios/{usuario_log_id}")
async def update_usuario(usuario_log_id: int, usuario: Usuario):
    if usuario_log_id in db:
        db[usuario_log_id] = usuario
        return {"message": "Usuário atualizado"}
    return {"message": "Usuário não encontrado"}

# Operação Delete
@app.delete("/usuarios/{usuario_log_id}")
async def delete_usuario(usuario_log_id: int):
    if usuario_log_id in db:
        del db[usuario_log_id]
        return {"message": "Usuário excluído"}
    return {"message": "Usuário não encontrado"}
