from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

# Configuração do CORS
origins = ["*"]  # Permitir solicitações de todas as origens

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados
class Usuario(BaseModel):
    log_id: int
    log_nome: str
    log_email: str
    log_senha: str
    log_cpf: int
    log_cep: int
    log_telefone: int

# Simulação de armazenamento de dados de usuários
db_usuarios: Dict[int, Usuario] = {}

# Modelo de dados
class Produto(BaseModel):
    prod_id: int
    prod_nome: str
    prod_descr: str
    prod_preco: float
    prod_img: str

# Simulação de armazenamento de dados de produtos
db_produtos: Dict[int, Produto] = {}

# CRUD Usuario 

# Operação Create
@app.post("/usuarios/")
async def create_usuario(usuario: Usuario):
    db_usuarios[usuario.log_id] = usuario
    return {"message": "Usuário criado"}

# Operação Read
@app.get("/usuarios/{usuario_log_id}")
async def read_usuario(usuario_log_id: int):
    usuario = db_usuarios.get(usuario_log_id)
    if usuario:
        return usuario
    return {"message": "Usuário não encontrado"}

# Operação Update
@app.put("/usuarios/{usuario_log_id}")
async def update_usuario(usuario_log_id: int, usuario: Usuario):
    if usuario_log_id in db_usuarios:
        db_usuarios[usuario_log_id] = usuario
        return {"message": "Usuário atualizado"}
    return {"message": "Usuário não encontrado"}

# Operação Delete
@app.delete("/usuarios/{usuario_log_id}")
async def delete_usuario(usuario_log_id: int):
    if usuario_log_id in db_usuarios:
        del db_usuarios[usuario_log_id]
        return {"message": "Usuário excluído"}
    return {"message": "Usuário não encontrado"}

# CRUD Produto

# Operação Create 
@app.post("/produtos/")
async def create_produto(produto: Produto):
    db_produtos[produto.prod_id] = produto
    return {"message": "Produto criado"}

# Operação Read
@app.get("/produtos/{produto_prod_id}")
async def read_produto(produto_prod_id: int):
    produto = db_produtos.get(produto_prod_id)
    if produto:
        return produto
    return {"message": "Produto não encontrado"}

# Operação Update
@app.put("/produtos/{produto_prod_id}")
async def update_produto(produto_prod_id: int, produto: Produto):
    if produto_prod_id in db_produtos:
        db_produtos[produto_prod_id] = produto
        return {"message": "Produto atualizado"}
    return {"message": "Produto não encontrado"}

# Operação Delete
@app.delete("/produtos/{produto_prod_id}")
async def delete_produto(produto_prod_id: int):
    if produto_prod_id in db_produtos:
        del db_produtos[produto_prod_id]
        return {"message": "Produto excluído"}
    return {"message": "Produto não encontrado"}
