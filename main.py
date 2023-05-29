from fastapi import FastAPI
from pydantic import BaseModel
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
    log_datanasc: Optional[str]

# Simulação de armazenamento de dados
db: Dict[int, Usuario] = {}

# Modelo de dados
class Produtos(BaseModel):
    prod_id: int
    prod_nome: str
    prod_descr: str
    prod_preco: float

# Simulação de armazenamento de dados
db: Dict[int, Produtos] = {}

    
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

# Operação Create
@app.post("/produtos/")
async def create_produto(produto: Produto):
    db[produto.log_id] = produto
    return {"message": "Usuário criado"}

# Operação Read
@app.get("/produtos/{produto_prod_id}")
async def read_produto(produto_prod_id: int):
    produto = db.get(produto_prod_id)
    if produto:
        return produto
    return {"message": "Usuário não encontrado"}

# Operação Update
@app.put("/produtos/{produto_prod_id}")
async def update_produto(produto_prod_id: int, produto: Produto):
    if produto_prod_id in db:
        db[produto_prod_id] = produto
        return {"message": "Usuário atualizado"}
    return {"message": "Usuário não encontrado"}

# Operação Delete
@app.delete("/produtos/{produto_prod_id}")
async def delete_produto(produto_prod_id: int):
    if produto_prod_id in db:
        del db[produto_prod_id]
        return {"message": "Usuário excluído"}
    return {"message": "Usuário não encontrado"}
