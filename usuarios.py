import json

def carregar_dados():
    try:
        with open("dados.json", "r") as f:
            return json.load(f)
    except:
        return {}

def salvar_dados(dados):
    with open("dados.json", "w") as f:
        json.dump(dados, f, indent=4)

def criar_usuario():
    dados = carregar_dados()

    usuario = input("Novo usuário: ")
    senha = input("Senha: ")

    if usuario in dados:
        print("Usuário já existe!")
        return

    dados[usuario] = {
        "senha": senha,
        "saldo": 0,
        "historico": []
    }

    salvar_dados(dados)
    print("Conta criada com sucesso!")

def login():
    dados = carregar_dados()

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in dados and dados[usuario]["senha"] == senha:
        print("Login realizado!")
        return usuario
    else:
        print("Usuário ou senha incorretos!")
        return None